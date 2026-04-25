# Project NOMAD - TODO List

This document tracks our development progress based on the `ONBOARDING.md` and `plan/` documents.

## Phase 1: Foundation & Data Ingestion (LanceDB + Kiwix)
- [x] Build basic Kiwix Python Client (`kiwix/client.py`, `book.py`, `article.py`)
- [ ] Offline Pre-processing Script: Extract `Title` and `Abstract` from Kiwix `.zim` files
- [ ] LLM Data Annotation: Use Gemma 4 to generate "Feelings Tag" & "Symptoms Tag" for articles
- [ ] LanceDB Setup: Embed `Title + Feelings + Symptoms` and store with `zim_id` / URL to avoid "Unzip Bomb"

## Phase 2: Agentic Workflow Integration (FSM)
- [x] Create FSM skeleton (`FSM/engine.py`)
- [ ] FSM: Implement `TRIAGE` state logic (Call LLM to classify if query is medical)
- [ ] FSM: Implement `SEARCH_VEC` state logic (LanceDB Semantic Vector Retrieval)
- [ ] FSM: Implement `SEARCH_KIWIX` state logic (Connect `Book.search_article` to FSM)
- [ ] FSM: Implement `REASONING` state logic (Combine retrieved contexts, call Gemma 4 for grounded reasoning)
- [ ] FSM: Implement `OUTPUT` state logic (Ensure citations and avoid hallucinations)

## Phase 3: User Interface (TUI & App)
- [x] Build basic Textual UI (`app/tui.py`)
- [ ] Integrate FSM Engine into TUI (Replace direct streaming with Agentic Workflow steps)
- [ ] Display Agent thought process (e.g., "Triaging...", "Searching Vector DB...", "Reasoning...") in UI

## Phase 4: Edge Deployment Optimization (llama.cpp / LiteRT)
- [ ] Obtain Gemma 4 26B MoE in GGUF format (4-bit quantization)
- [ ] Setup `llama.cpp` Python bindings (or Ollama API) for offline local execution
- [ ] Test system in a completely air-gapped environment
- [ ] Benchmark "Time to First Token" and Memory usage (Target VRAM: 15-18GB)

## Phase 5: Hackathon Deliverables
- [ ] Prepare demo video (Focus on Edge / Offline capabilities and Agent reasoning)
- [ ] Draft submission write-up: Focus on Technical Depth (llama.cpp optimizations & Groundedness)
- [ ] Finalize "Impact Story" (Global Resilience / Offline Medical Aid in disaster zones)
