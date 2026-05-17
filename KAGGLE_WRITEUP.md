# Dr. Offline: The Offline Medical Reasoning Engine
## Democratizing Grounded Medical Intelligence for Edge and Disaster Response

**Track Selection:** Global Resilience: Build the systems of tomorrow—from offline, edge-based disaster response to long-range climate mitigation—that anticipate, mitigate, and respond to the world’s most pressing challenges.

---

### Introduction: The Disconnected Frontline

In disaster zones, remote mountain villages, and resource-deprived regions, reliable medical intelligence is often a matter of life and death. However, modern AI solutions overwhelmingly assume constant, high-bandwidth internet access. When the grid fails, cloud-based models become useless. 

**Dr. Offline (Offline Medical Reasoning Engine)** was built to solve this critical vulnerability. Dr. Offline is an air-gapped, fully offline medical triage and retrieval system. By engineering an intelligent Retrieval-Augmented Generation (RAG) pipeline optimized for edge computing, we demonstrate that a state-of-the-art model—**Gemma 4**—can run fluently on constrained hardware (such as a ruggedized laptop), providing grounded, hallucination-free medical guidance to frontline workers.

### System Architecture

Our application abandons the standard, cloud-heavy AI design in favor of an efficient **Edge Agentic Workflow**, orchestrated purely in Python and driven by a Finite State Machine (FSM). The architecture is divided into four main pillars:

1.  **The User Interface (`app/tui.py`)**: A lightweight Textual User Interface (TUI) provides a seamless terminal-based chat experience, ensuring the application remains highly responsive and functional in headless or low-resource OS environments.
2.  **The Agentic Engine (`FSM/engine.py`)**: Rather than a standard chatbot, Dr. Offline utilizes a strict Finite State Machine. The FSM governs the reasoning path: *Triage $\to$ Keyword Expansion Search $\to$ Reasoning $\to$ Output*. This strict workflow forces the agent to gather context before speaking, entirely eliminating "guessed" or hallucinated medical advice.
3.  **Knowledge Retrieval (`kiwix/client.py`)**: The system uses **Kiwix** (specifically the `.zim` format) as its Sole Source of Truth. Kiwix provides immense offline compression, allowing us to store the entirety of WikiMed locally, removing the need for heavy vector databases. Notably, the Kiwix server host can be as simple as an everyday Android phone with the Kiwix app installed, acting as a portable local hotspot for the reasoning engine.

### How We Specifically Used Gemma 4

To make Dr. Offline a reality, we leveraged **Gemma 4 26B MoE (Mixture of Experts)**. We specifically chose the 26B MoE over a denser architecture because of its hardware efficiency: the Router mechanism only activates roughly 4B parameters per token, drastically reducing FLOPs while retaining deep medical knowledge.

We deployed Gemma 4 in two critical phases within our pipeline:

*   **Intelligent Query Expansion & Routing**: When a user inputs a query (e.g., *"My chest feels like there's a heavy rock on it"*), Gemma 4 does not immediately search for these layman terms. Instead, it translates this symptom into clinical search queries (e.g., `chest pain OR myocardial infarction OR angina pectoris`). We utilized BAML to enforce structured outputs from Gemma 4, effectively turning the LLM into a precise semantic router.
*   **Cross-Document Reasoning**: Once our optimized keyword search retrieves the most relevant articles from Kiwix, we inject the complete text of the Top 3 articles directly into Gemma 4’s massive **256K Context Window**. Gemma 4 acts as a medical synthesizer, cross-referencing the documents, extracting the relevant treatment guidelines, and generating a highly grounded response that strictly cites the provided WikiMed text.

### Overcoming Challenges and Validating Technical Choices

Building a robust AI for air-gapped edge devices presented several significant engineering hurdles. We made strict architectural trade-offs to ensure our solution was not just a prototype, but a viable system for the field.

#### Challenge 1: The "Unzip Bomb" of Vectorizing Medical Data
**The Problem:** Traditional RAG pipelines chunk and embed the entirety of their knowledge bases. Vectorizing hundreds of thousands of WikiMed articles creates an enormous index (an "unzip bomb"), which would consume excessive disk space and cause severe latency when querying on edge CPUs with limited RAM.
**The Solution:** We abandoned vector embeddings entirely. Instead of introducing a heavy vector database like FAISS or LanceDB, we leaned into the native search capabilities of `kiwix-serve`. This radically simplified our architecture, dropping our storage and memory footprint to the absolute minimum required for the raw `.zim` files and the LLM itself.

#### Challenge 2: The Semantic Gap in Local Search
**The Problem:** Using pure keyword search on the Kiwix API often fails due to the "semantic gap" (e.g., a patient complaining of "brain on fire" will not easily match an article on "Encephalitis"). Without a vector database, how do we bridge this gap?
**The Solution:** We engineered an **LLM-Driven Query Expansion System**. We use Gemma 4 to translate layman terms and feelings into highly precise clinical keywords *before* querying Kiwix. By utilizing BAML to enforce structured JSON outputs, Gemma 4 reliably maps "brain on fire" to `["Encephalitis", "Meningitis", "Cerebral inflammation"]`. These terms are then fed directly into Kiwix, ensuring high-quality retrieval without the overhead of maintaining semantic vector spaces.

#### Challenge 3: Hardware Portability and Compute Limits
**The Problem:** Serving a 26B parameter model typically requires expensive, high-end cloud GPUs—resources that are non-existent in disaster zones.
**The Solution:** While our existing development harness utilizes the online Google API for rapid prototyping and validation, our production deployment architecture is designed entirely for on-device inference using **Ollama**. By utilizing Ollama to serve a 4-bit quantized version of the model, we compress the Gemma 4 26B MoE's VRAM requirements from over 50GB down to roughly 15-18GB. This ensures that the entire intelligence pipeline—LLM and Kiwix server—can execute fluently on consumer-grade hardware in the field, fulfilling our mission for the Global Resilience track.

### Conclusion

Dr. Offline proves that advanced medical reasoning no longer requires a lifeline to the cloud. By intelligently combining the high-efficiency Gemma 4 26B MoE and the offline robustness of Kiwix, we have built a resilient, hallucination-free medical engine that runs entirely on edge devices. When disaster strikes and communications fall, Dr. Offline ensures that world-class medical intelligence remains available at the edge—where it is needed most.

### Attachments / Project Links

*   **Video Demo:** [YouTube](https://www.youtube.com/watch?v=R3nA1u5oLrQ)
*   **Public Code Repository:** [GitHub](https://github.com/cenzwong/2026-gemma-4-hackathon)
*   **Live Demo:** Follow the instructions in the **README.md** file in the [Public Code Repository](https://github.com/cenzwong/2026-gemma-4-hackathon) to run the application locally.
