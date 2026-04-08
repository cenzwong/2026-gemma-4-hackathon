一份完整嘅 **Gemma 4 Good Hackathon 參賽企劃與架構決策紀錄 (Architectural Decision Record, ADR)**。呢份清單紀錄咗我哋對於效能、成本同內部機制嘅技術取捨。

### 🏆 專案定位：離線醫療推理引擎 (Offline Medical Reasoning Engine)
* **目標賽道 (Target Tracks)：** Global Resilience (全球韌性) / Health & Sciences (醫療與科學)。
* **核心理念：** 借鑑 Project NOMAD 嘅離線基建概念，但將大腦升級為具備深度醫療推理、防幻覺能力嘅 Gemma 4 邊緣端 AI。

---

### 🏗️ 核心架構與技術取捨 (Architectural Decisions & Trade-offs)

#### 1. 大型語言模型 (LLM) 引擎：Gemma 4 26B MoE (4-bit 量化)
* **決策：** 選擇 26B MoE，捨棄 31B Dense。
* **內部機制與推理 (Architectural Reasoning)：** * MoE 架構雖然總參數量達 26B，但 Router 機制令每次 Token 生成只啟動約 4B 參數。這在極大降低 FLOPs（浮點運算次數）的同時，保持了模型對廣泛醫療知識的理解深度。
    * 配合 4-bit Quantization，可以將 VRAM 需求從 ~52GB 壓榨到 15-18GB，令系統能夠喺 Kaggle 免費嘅雙 T4 GPU，或者消費級 Edge Device (如低配伺服器) 上流暢運行。
* **Trade-off：** 犧牲了 Dense 模型喺極端複雜邏輯推演上嘅絕對穩定性，換取了離線部署嘅可行性與超低延遲。

#### 2. 數據存儲與知識庫：Kiwix (ZIM 格式) + WikiMed
* **決策：** 採用 ZIM 格式作為 Sole Source of Truth。
* **內部機制與推理：** * 醫療應用最忌幻覺 (Hallucination)。ZIM 格式自帶極高壓縮比與本地索引，完美解決了幾十 GB 醫療百科喺無網絡環境下嘅儲存與讀取瓶頸。
    * 不依賴模型自身的預訓練權重來回答醫學問題，而是嚴格限制其基於 Kiwix 提取出的文本進行推斷 (Groundedness)。

#### 3. 檢索與增強生成 (Retrieval Strategy)：LLM-Driven Query Expansion 
* **決策：** 優先採用「代理搜尋 (Agentic Search) 配合 Kiwix 原生 API」，而非預設使用 Vector Database (如 LanceDB)。
* **內部機制與推理：**
    * **精確度優先：** 醫療文獻充滿專有名詞，Keyword 搜尋喺特定藥物或病症匹配上，往往比 Semantic Vector Search 更具備高 Precision（精確度）。
    * **資源極致最佳化：** 放棄 Vector DB 意味著零 Embedding 運算成本、零額外 Vector 儲存空間，進一步降低 Edge Device 的硬件門檻。
    * **長文本推理發揮：** 系統流程改為：User 提問 -> Gemma 4 生成多組精準醫學 Keyword -> Kiwix API 檢索原文 -> 將海量原文直接塞入 Gemma 4 的 **256K Context Window** 進行跨文件綜合分析。
* **Trade-off：** 增加了一次 LLM API Call（用來生成關鍵字），導致整體反應時間（Latency）略微上升，但大幅節省了磁碟空間並提高了專有名詞的命中率。

---

### 🚀 開發階段規劃 (Development Phases)

* **Phase 1: Proof of Concept (概念驗證)**
    * 硬件：暫時唔搞 Local 部署，直接用 Google AI Studio API 測試。
    * 目標：寫好 Gemma 4 嘅 System Prompt，測試佢「根據病徵生成精準醫學搜尋 Keyword」嘅能力。
* **Phase 2: Data Retrieval Pipeline (數據管道)**
    * 架構：安裝 `kiwix-serve`，用 Python 寫一個簡單嘅 Wrapper 函數，輸入 Keyword，回傳乾淨嘅 WikiMed Text 內容。
* **Phase 3: Integration & Context Window Testing (系統整合)**
    * 架構：將 Phase 2 攞到嘅幾萬字長文本，配合 User 嘅原始問題，一併送入 Gemma 4，觀察其能否喺超長 Context 中準確抽絲剝繭給出建議。
* **Phase 4: Edge Deployment (邊緣部署優化)**
    * 架構：轉移至 Kaggle Notebook 或本地機器，利用 `llama.cpp` 載入 4-bit 量化版的 Gemma 4 26B MoE，測試離線運作的真實效能 (Tokens per second)。
