# Agent Instructions & Codebase Guide

Welcome to the Edge Medical Agent project. This file is intended for AI coding assistants to quickly understand the codebase's architecture, conventions, and current state.

## Project Structure

```text
code/
├── app/
│   └── tui.py             # Textual User Interface (Terminal chat UI)
├── FSM/
│   └── engine.py          # Finite State Machine for Medical Reasoning Workflow
├── kiwix/                 # Client for kiwix-serve API (Local Offline Wikipedia)
│   ├── __init__.py
│   ├── client.py          # Kiwix API client (fetch catalog/books)
│   ├── book.py            # Book object (search articles within a ZIM)
│   └── article.py         # Article object (fetch and parse HTML into Headers)
├── llm/
│   ├── __init__.py
│   ├── models.py          # Gemma Model definitions
│   └── utils.py           # GenAI API wrappers (stream_generate_content)
├── .env                   # Environment variables (e.g., GEMINI_API_KEY)
└── requirements.txt       # Python dependencies
```

## Core Workflows

### 1. Kiwix Offline Knowledge Retrieval
The `kiwix` module handles querying a local `kiwix-serve` instance.
- **Fetching Catalogs**: `Kiwix.get_kiwix_book()` fetches available ZIM files. It attempts to parse XML first, falling back to JSON.
- **Searching**: `Book.search_article()` hits the `/search` endpoint to find articles in the ZIM file. Supports both XML and HTML search result parsing.
- **Content Parsing**: `Article.get_article()` fetches the raw HTML from Kiwix and uses `BeautifulSoup` to parse `mw-parser-output` content into structured `Header` objects (ignoring metadata).

### 2. Finite State Machine (FSM)
The Medical Agent's logic is tightly controlled by `MedicalAgentFSM` in `FSM/engine.py`.
- **States**: `IDLE` -> `TRIAGE` -> `SEARCH_VEC` -> `SEARCH_KIWIX` -> `REASONING` -> `OUTPUT`.
- **Goal**: Prevent hallucinations. The agent must first confirm a medical query (Triage), search semantic vector space (LanceDB), retrieve full text (Kiwix), reason over the context (using Gemma 4), and output a response citing the source.
- *Note:* The FSM logic is currently implemented with dummy conditionals (`TODO` comments) and needs further integration with the `llm` and `kiwix` modules.

### 3. Language Model Integration
`llm/utils.py` contains the `stream_generate_content` function using the `google.genai` SDK.
- It supports tool-use and thinking levels (e.g., `thinking_level="HIGH"`).
- Currently, `app/tui.py` uses this to stream responses into a Textual markdown chat interface.

## Conventions & Rules for AI Agents

1. **Specific APIs Over Bash Tools**: When searching or modifying code, use provided API tools (`grep_search`, `replace_file_content`, etc.) rather than generic bash utilities like `cat`, `grep`, or `sed`.
2. **Modularization**: Keep components decoupled. The FSM engine shouldn't contain raw HTTP request logic; use the `kiwix` and `llm` wrappers.
3. **No Placeholders in Development**: Provide fully working implementations. When writing new FSM logic or Kiwix parsing code, ensure all edge cases (e.g., missing HTML tags, API failures) are handled gracefully.
4. **Offline First**: The primary deployment target is an offline edge device (LiteRT). Avoid assuming the availability of internet APIs beyond the local Kiwix and Vector databases, except during the current prototyping phase where the Gemini API might be used.
5. **Types and Dataclasses**: Use `dataclass` and explicit type hints (e.g., `Optional[List[Article]]`) extensively for code clarity.
