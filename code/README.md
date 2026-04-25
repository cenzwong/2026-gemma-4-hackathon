# 2026 Gemma 4 Hackathon - Edge Medical Agent

This directory contains the source code for an Edge-deployed Medical AI Agent, built for the Gemma 4 for Good Hackathon.
The goal of this project is to run a local LLM agent to assist users with medical triage and information retrieval without requiring an internet connection.

## Architecture & Modules

The codebase is structured into four main components:

1. **`app/` (User Interface)**
   - Contains a Textual User Interface (TUI) in `tui.py`.
   - Provides a terminal-based chat interface to interact with the Gemma 4 model seamlessly.

2. **`FSM/` (Medical Agent Engine)**
   - Houses the core Finite State Machine in `engine.py`.
   - Controls the agentic workflow: Triage -> Semantic Search (LanceDB) -> Full Text Search (Kiwix) -> Reasoning -> Output.
   - Ensures the agent follows a strict reasoning path to avoid hallucinations and ground answers in factual data.

3. **`kiwix/` (Knowledge Retrieval)**
   - A Python wrapper for the local `kiwix-serve` API.
   - `client.py`: Interacts with the Kiwix server to fetch available books/catalogs.
   - `book.py`: Represents a ZIM file and allows full-text searching (HTML/XML formats).
   - `article.py`: Fetches and parses article HTML content into structured headers.

4. **`llm/` (LLM Integration)**
   - `models.py` & `utils.py`: Wrappers around the Google GenAI SDK (Gemini / Gemma 4).
   - Provides streaming responses and tool integrations for the TUI and FSM.

## Getting Started

1. Set up your `.env` file with the required API keys (e.g., `GEMINI_API_KEY` for testing/cloud inference).
2. Install the required dependencies from `requirements.txt`.
3. Make sure a local Kiwix server is running if testing knowledge retrieval.
4. Run the TUI:
   ```bash
   python app/tui.py
   ```

## Design Philosophy

- **Edge Deployment**: We aim to run this entirely on-device (e.g., a low-end Android phone via LiteRT) to show the value of a small footprint Gemma 4 model.
- **Agentic Workflow**: The agent doesn't just chat; it actively searches, parses, and reasons over the local WikiMed database using a defined Finite State Machine.
- **Grounding**: Medical domain demands accuracy. All responses must be grounded in search results fetched via Kiwix and LanceDB.
