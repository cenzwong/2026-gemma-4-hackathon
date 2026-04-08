It is **both**. `kiwix-serve` is fundamentally a **standalone CLI binary** written in C++, but it is almost always deployed as a **Docker service** in modern data engineering stacks to simplify dependency management (like `libzim` and `xapian`).

Since you are building an **air-gapped RAG solution**, understanding the difference is crucial for how you move files across the "air-gap."

---

## 1. The CLI Approach (Bare Metal)
In this mode, you run a single compiled binary on your host OS.

* **What it looks like:** A single file (e.g., `kiwix-serve.exe` or `kiwix-serve` for Linux) that you execute via terminal.
* **Deployment:** You download the `kiwix-tools` archive, extract it, and run it against a `.zim` file.
* **Best for:** Extremely resource-constrained hardware (e.g., small IoT devices) where the overhead of a container engine is too high.
* **Command:**
    ```bash
    ./kiwix-serve --port 8080 /path/to/your/knowledge_base.zim
    ```

## 2. The Docker Approach (Containerized)
In this mode, the CLI binary is "baked" into a Linux image along with all its required libraries.

* **What it looks like:** A `docker-compose.yml` file or a `docker run` command.
* **Deployment:** You "pull" the image (or save it as a `.tar` file to move to your air-gapped machine) and let the container engine manage the networking.
* **Best for:** Your RAG setup. It ensures that the specific version of `libzim` used by Kiwix matches the one you use in your Python code for LanceDB indexing.
* **Command:**
    ```bash
    docker run -d -p 8080:8080 -v /mnt/data/zims:/data kiwix/kiwix-tools kiwix-serve --port 8080 /data/wikipedia.zim
    ```

---

## Comparison for Air-Gapped RAG

| Feature | CLI Binary | Docker Service |
| :--- | :--- | :--- |
| **Portability** | Requires matching OS libraries (glibc, etc.) | Fully self-contained; runs anywhere with Docker/Podman. |
| **Networking** | Harder to isolate; runs on host network by default. | Easy to put on a private internal network with your LLM. |
| **Updating** | Replace the binary file. | `docker load` a new image version. |
| **RAG Integration** | Fast, but library conflicts are common. | **Recommended.** Guarantees environment parity. |

---

## How to "Deploy" in your Air-Gapped Environment

Since you are air-gapped, you can't just `docker pull`. Your deployment workflow should look like this:

### Step 1: Prepare (On an Internet-Connected Machine)
1.  Download the Kiwix Docker image: `docker pull ghcr.io/kiwix/kiwix-tools:latest`.
2.  Save it to a file: `docker save ghcr.io/kiwix/kiwix-tools:latest > kiwix_image.tar`.
3.  Download your `.zim` files (e.g., Wikipedia, StackOverflow).
4.  Move the `.tar` and the `.zim` files to your air-gapped machine via physical media.

### Step 2: Launch (On the Air-Gapped Machine)
1.  Load the image: `docker load < kiwix_image.tar`.
2.  Launch the service using **Docker Compose** (recommended) so your Gemma 4 backend and LanceDB script can "see" Kiwix by its container name:

```yaml
# docker-compose.yml
services:
  kiwix:
    image: kiwix/kiwix-tools
    command: kiwix-serve --port 8080 /data/wiki_2026.zim
    volumes:
      - ./my_zims:/data
    ports:
      - "8080:8080"
      
  rag-backend:
    build: ./my-gemma4-app
    depends_on:
      - kiwix
    environment:
      - KIWIX_URL=http://kiwix:8080
      - LANCEDB_PATH=/app/data/lancedb
```



**Pro Tip:** For your **LanceDB** metadata search, make sure you mount the same `./my_zims` folder to your RAG backend container. Your indexing script needs direct file access to the `.zim` to build the LanceDB index, but your Gemma 4 model will use the `kiwix-serve` HTTP API to "read" the articles during the RAG loop.

Does your air-gapped environment allow for Docker, or are you restricted to running pure binaries?
