# Dr. Offline: The Offline Medical Reasoning Engine

**2026 Gemma 4 Good Hackathon Submission**  
**Track**: Global Resilience

Dr. Offline is an air-gapped, fully offline medical triage and retrieval system designed for disaster zones, remote villages, and resource-deprived environments. Powered by **Gemma 4 26B MoE** and a **Kiwix** offline knowledge base, this application provides grounded, hallucination-free medical guidance without requiring any internet connection.

📖 **[Read our full technical Writeup here](./KAGGLE_WRITEUP.md)**
🏆 **[View our Kaggle Submission](https://kaggle.com/competitions/gemma-4-good-hackathon/writeups/dr-offline-the-offline-medical-reasoning-engine)**

---

## 🚀 How to Install and Run (For Judges)

We have designed the setup process to be as lightweight and straightforward as possible.

### 1. Prerequisites

- Python 3.10+
- A local Kiwix server running (serving a WikiMed `.zim` file). 
  *💡 **Recommendation**: We highly recommend using an Android phone with the [Kiwix app](https://play.google.com/store/apps/details?id=org.kiwix.kiwixmobile&hl=en&pli=1) installed to act as the server—it is by far the easiest setup method. Simply download the WikiMed library in the app and tap "Host on Local Network". (Alternatively, you can run `kiwix-serve` locally via Docker).*
- Set up your `.env` file inside the `code/` directory (you can copy `.env.example` to `.env` and fill in the values) if you are using cloud inference for testing. The final system is designed for local inference via `llama.cpp`.

### 2. Installation

First, clone the repository and navigate into it:

```bash
git clone <repository-url>
cd 2026-gemma-4-hackathon
```

Next, create a virtual environment and install the required dependencies:

```bash
# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r code/requirements.txt
```

### 3. Running the Application

To launch the Dr. Offline Textual User Interface (TUI) and interact with the Medical Agent:

```bash
cd code
python app/tui.py
```

This will launch a seamless terminal-based chat interface. From here, you can input colloquial symptoms (e.g., *"My chest feels heavy and it hurts when I breathe"*), and watch the Agentic Engine autonomously expand your query, search the local Kiwix database, and stream a grounded, hallucination-free medical response.

---

## 🏗️ Project Structure Overview

- **`code/app/`**: The lightweight Textual User Interface (`tui.py`).
- **`code/FSM/`**: The Medical Agent Engine that governs the strict reasoning path (Triage -> Keyword Expansion Search -> Reasoning -> Output).
- **`code/kiwix/`**: Knowledge Retrieval module that interfaces directly with your local Kiwix server to act as the sole source of truth.
- **`code/llm/`**: Model integration wrapping the Gemma 4 SDK.
