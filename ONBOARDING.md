# Dr. Offline: 離線醫療推理引擎 (Offline Medical Reasoning Engine) - Onboarding Guide

歡迎加入 Dr. Offline 嘅開發 Team！呢份 document 係專為新同事同未來嘅 AI Agent 準備嘅 Onboarding Guide。我哋參加緊 **2026 Gemma 4 Good Hackathon**，目標係要打造一個完全 offline 嘅醫療 RAG 系統。

---

## 🏆 Project Overview (專案定位)

我哋嘅項目主要瞄準 **Global Resilience (全球韌性)** 呢個 Hackathon Track。
我哋嘅核心理念係：**喺斷網嘅偏遠山區、災難現場或者資源匱乏嘅環境，提供一個無網絡依賴嘅「全知醫學專家」。**
我哋要證明，透過高超嘅 Edge AI 工程優化，Gemma 4 配合離線資料庫，可以喺普通嘅 Edge Device 上流暢行到，為前線醫護人員提供 Grounded 嘅醫療建議，同時避免 AI 產生幻覺 (Hallucination)。

---

## 🏗️ Core Tech Stack (官方核心技術棧)

經過多次架構討論，我哋最終決定採用 **Pure Python + Kiwix** 作為主要架構。

* **LLM 引擎 (The Brain)**: **Gemma 4 26B MoE (4-bit Quantization)**。我哋放棄 31B Dense 模型，轉用 MoE，配合 4-bit 量化，將 VRAM 需求由 ~52GB 壓榨到 15-18GB。可以使用 **llama.cpp** 或者 **Ollama** 嚟行。如果想進一步 optimize，我哋亦會考慮用 **Unsloth** 做微調 (Fine-tuning)，令個 model 更加熟悉醫療知識。
* **資料來源 (Sole Source of Truth)**: **Kiwix (ZIM 格式) + WikiMed**。Kiwix 提供極高壓縮比嘅本地 `.zim` 檔案，完美解決斷網環境下幾十 GB 醫療百科嘅儲存問題。我哋會用 `kiwix-serve` (透過 Docker deployment) 嚟做底層嘅全文檢索。

---

## 🤖 Agentic Workflow (代理工作流實戰示範)

我哋嘅系統唔係一個普通嘅 chatbot，而係一個有思考能力嘅 Agent。以下係一個用家問 "心口揼住痛" 嘅 workflow：

1. **Analysis & Query Expansion (分析與擴展)**:
   - 用家輸入 (Input): "醫生，我個心口好似被嘢揼咁痛。"
   - Gemma 4 唔會直接去 search 呢句，佢會先將口語化嘅「感覺」轉化做 Query Expansion。
   - Gemma Output (Search terms): `("chest pain" OR "myocardial infarction" OR "angina pectoris")`。

2. **Kiwix Search (Kiwix 搜尋)**:
   - **Path A (Kiwix + Query Expansion)**: Python script call `kiwix-serve` API，利用 Gemma 4 生成嘅 keyword，準確搵出相關嘅 WikiMed 文章。

3. **Generation (增強生成)**:
   - 將搵到嘅 Top 3 文章嘅 Full-text 塞入 Gemma 4 嘅 256K Context Window。
   - Gemma 4 根據 WikiMed 嘅內容，做 cross-document reasoning，並標明出處 (Grounded output)，比出最終、防幻覺嘅醫療建議俾用家。

---

## 🗑️ Discarded Approaches (被棄用嘅方案與原因)

喺 pre-planning 階段，我哋諗過好多 approach，以下係我哋 discard 咗嘅 idea 以及原因：

### 1. Android App + Turso (LiteRT Track)
* **Idea**: 做一個原生 Android App，用 Turso (LibSQL) 存 Vector，再透過 LiteRT 用電話 NPU 跑 model。
* **點解唔用 (Reason)**: 雖然對角逐 LiteRT 獎項極有利，但開發成本極高。我哋 Team 比較擅長 Pure Python，而 Web App / Pure Python API architecture 配合 LanceDB 喺處理 RAG logic 同 Agentic framework 上面會靈活好多。為咗 project 嘅完整性同埋 Agent reasoning 嘅複雜度，我哋選擇咗 Python。

### 2. LanceDB / Vector DB 向量數據庫
* **Idea**: 用 LanceDB 或傳統嘅 FAISS 或 Chroma 做檢索。
* **點解唔用 (Reason)**: 我哋原本打算用 LanceDB 做 Semantic Re-ranking，但後來發現純粹依靠 Gemma 4 做 Query Expansion 再配合 Kiwix 原生搜索已經可以達到非常高嘅準確率。加入 LanceDB 反而會增加架構複雜度同資源消耗，對 Edge Device 唔夠 friendly，所以我哋最終放棄咗 Vector DB，實現一個更簡潔、更輕量嘅架構。

---

祝各位喺 Dr. Offline 開發順利！Let's win this hackathon! 🚀
