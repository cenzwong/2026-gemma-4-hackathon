# Project NOMAD: 離線醫療推理引擎 (Offline Medical Reasoning Engine) - Onboarding Guide

歡迎加入 Project NOMAD 嘅開發 Team！呢份 document 係專為新同事同未來嘅 AI Agent 準備嘅 Onboarding Guide。我哋參加緊 **2026 Gemma 4 Good Hackathon**，目標係要打造一個完全 offline 嘅醫療 RAG 系統。

---

## 🏆 Project Overview (專案定位)

我哋嘅項目主要瞄準 **Global Resilience (全球韌性)** 呢個 Hackathon Track。
我哋嘅核心理念係：**喺斷網嘅偏遠山區、災難現場或者資源匱乏嘅環境，提供一個無網絡依賴嘅「全知醫學專家」。**
我哋要證明，透過高超嘅 Edge AI 工程優化，Gemma 4 配合離線資料庫，可以喺普通嘅 Edge Device 上流暢行到，為前線醫護人員提供 Grounded 嘅醫療建議，同時避免 AI 產生幻覺 (Hallucination)。

---

## 🏗️ Core Tech Stack (官方核心技術棧)

經過多次架構討論，我哋最終決定採用 **Pure Python + LanceDB** 作為主要架構。

* **LLM 引擎 (The Brain)**: **Gemma 4 26B MoE (4-bit Quantization)**。我哋放棄 31B Dense 模型，轉用 MoE，配合 4-bit 量化，將 VRAM 需求由 ~52GB 壓榨到 15-18GB。可以使用 **llama.cpp** 或者 **Ollama** 嚟行。如果想進一步 optimize，我哋亦會考慮用 **Unsloth** 做微調 (Fine-tuning)，令個 model 更加熟悉醫療知識。
* **資料來源 (Sole Source of Truth)**: **Kiwix (ZIM 格式) + WikiMed**。Kiwix 提供極高壓縮比嘅本地 `.zim` 檔案，完美解決斷網環境下幾十 GB 醫療百科嘅儲存問題。我哋會用 `kiwix-serve` (透過 Docker deployment) 嚟做底層嘅全文檢索。
* **向量數據庫 (Vector DB)**: **LanceDB**。LanceDB 原生支援 Python (`Pandas`, `PyArrow`)，Zero-copy reads 效能極高，而且支援多模態 (Multimodal)，可以儲存圖片 Embedding。

---

## 🗂️ Indexing Strategy (官方索引策略)

要對十幾萬篇 WikiMed 文章建立 Vector DB 會有「Unzip Bomb」效能崩潰嘅風險，所以我哋**唔會**做 Full-text vectorization。我哋採用 **Pre-indexed Metadata (預索引輕量化標題/摘要)** 策略：

1. **Pre-processing (離線預處理)**:
   - 淨係從 ZIM 檔案度抽每一篇文章嘅 `Title` (標題) 同 `Abstract` (摘要)。
   - 我哋仲會用 Gemma 4 離線跑一次 AI-driven Tagging，幫每篇文生成「感覺 (Layman Feelings)」(例如："心口大石壓") 同「病徵 (Clinical Symptoms)」(例如："胸骨後疼痛")。
2. **Embedding**: 將 Title + Feelings Tag + Symptoms Tag 一齊做 Embedding，存入 LanceDB，並綁定對應嘅 `zim_id` / URL。
3. **Storage Efficiency**: 咁做 LanceDB Index 可能只係佔幾十 MB，完美避開大數據儲存瓶頸。

---

## 🤖 Agentic Workflow (代理工作流實戰示範)

我哋嘅系統唔係一個普通嘅 chatbot，而係一個有思考能力嘅 Agent。以下係一個用家問 "心口揼住痛" 嘅 workflow：

1. **Analysis & Query Expansion (分析與擴展)**:
   - 用家輸入 (Input): "醫生，我個心口好似被嘢揼咁痛。"
   - Gemma 4 唔會直接去 search 呢句，佢會先將口語化嘅「感覺」轉化做 Query Expansion。
   - Gemma Output (Search terms): `("chest pain" OR "myocardial infarction" OR "angina pectoris")`。

2. **Dual-track Search (雙路搜尋)**:
   - **Path A (Kiwix + Query Expansion)**: Python script call `kiwix-serve` API，攞返一堆可能相關嘅候選文章。
   - **Path B (LanceDB Semantic Search)**: 同時間，Python script 將用家嘅問題變做 Embedding，去 LanceDB 搵最 match 嘅 Metadata (Title / Tag)，攞到對應嘅 `zim_id`。如果用家有 upload X-Ray 或者皮膚紅疹相 (Vision input)，都會喺 LanceDB 做 Image-to-Image 檢索。

3. **Fusion & Re-ranking (整合與重排)**:
   - 將 Kiwix 搵返嚟嘅 full text 同 LanceDB 搵到嘅 result 進行匯總。
   - 利用 LanceDB 做最後嘅 Semantic Re-ranking，篩選出最高分 (例如 Top 3) 嘅精華文章。

4. **Generation (增強生成)**:
   - 將呢 Top 3 文章嘅 Full-text 塞入 Gemma 4 嘅 256K Context Window。
   - Gemma 4 根據 WikiMed 嘅內容，做 cross-document reasoning，並標明出處 (Grounded output)，比出最終、防幻覺嘅醫療建議俾用家。

---

## 🗑️ Discarded Approaches (被棄用嘅方案與原因)

喺 pre-planning 階段，我哋諗過好多 approach，以下係我哋 discard 咗嘅 idea 以及原因：

### 1. Android App + Turso (LiteRT Track)
* **Idea**: 做一個原生 Android App，用 Turso (LibSQL) 存 Vector，再透過 LiteRT 用電話 NPU 跑 model。
* **點解唔用 (Reason)**: 雖然對角逐 LiteRT 獎項極有利，但開發成本極高。我哋 Team 比較擅長 Pure Python，而 Web App / Pure Python API architecture 配合 LanceDB 喺處理 RAG logic 同 Agentic framework 上面會靈活好多。為咗 project 嘅完整性同埋 Agent reasoning 嘅複雜度，我哋選擇咗 Python。

### 2. FAISS / ChromaDB 作為 Vector DB
* **Idea**: 用傳統嘅 FAISS 或 Chroma 做檢索。
* **點解唔用 (Reason)**: 呢啲 DB 通常需要將成個 Index load 入 RAM，對於 Edge device (得 4GB-8GB RAM) 嚟講會死機。LanceDB 係 Disk-based indexing (Zero-copy read)，效能更高，更啱 Offline / Edge computing 環境。

### 3. 全量文本向量化 (Full Text Embedding)
* **Idea**: 將 WikiMed 幾十萬篇文章切 chunk，全部做 embedding 入 Vector DB。
* **點解唔用 (Reason)**: 會造成 "Unzip Bomb"，Embedding size 可能大過 1GB，兼且喺手機/普通 CPU 做 retrieval 會極慢。所以我哋轉用 **Metadata Indexing (只入 Title/Tag)**。

### 4. Pure Query Expansion (完全唔用 Vector DB)
* **Idea**: 單靠 Gemma 4 做 Keyword Expansion，然後直接 call `kiwix-serve`，完全飛走 LanceDB。
* **點解唔用 (Reason)**: 呢個係一個極度輕量嘅方案，但純 Keyword Search 會遇到「語義斷層」(Semantic Gap) 嘅問題 (例如 "個腦火燒" 同 "腦炎" 關鍵字上無關聯)。冇 LanceDB 做 Semantic Re-ranking 同埋處理 Vision 多模態數據，個 Agent 會變得太過「死板」，所以最終保留 LanceDB 做 Navigator。

---

祝各位喺 Project NOMAD 開發順利！Let's win this hackathon! 🚀
