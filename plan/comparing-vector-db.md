如果你考慮緊做 **Web App** 而唔係 **Android App**，呢個選擇會令部署變得好簡單（一條 Link 就睇到），但喺 **LanceDB** 同 **Turso** 嘅效能對比，以及點樣配合 **LiteRT** 方面，確實有啲嘢要考慮。

你嘅直覺係啱嘅：如果要贏 **LiteRT** 獎項，**Android** 確實係 Google AI Edge 嘅「主場」。

---

### 1. LanceDB vs. Turso (Web App 環境)

喺 Web 環境（WASM），兩者嘅效能表現同埋適合場景有明顯分別：

#### **LanceDB (WASM 模式)**
* **效能優勢**：LanceDB 係為咗「大數據」而生嘅。佢用嘅係列式儲存（Columnar Storage），喺處理 WikiMed 呢類幾十萬條 Vector 嘅檢索時，速度通常快過 Turso。
* **多模態**：如果你個 Web App 想俾人 Upload 醫療圖片（例如 X-ray）嚟搵相似文獻，LanceDB 處理 Image Embedding 嘅效率極高。
* **缺點**：喺瀏覽器入面跑 WASM 版 LanceDB，如果要 Load 幾 GB 嘅 Index，第一次載入時間會比較耐。

#### **Turso / LibSQL (WASM 模式)**
* **效能疑慮**：你擔心 Turso 嘅效能係有道理嘅。雖然 SQLite 做細規模 Vector Search 好快，但當去到 WikiMed 成個 Dataset 嘅規模，佢嘅 Indexing（如 IVF）喺瀏覽器 WASM 環境下，Latency 可能會比 LanceDB 高。
* **優勢**：如果你的數據涉及好多「過濾」條件（例如：搵『2020年後』、關於『兒科』、且『語義接近某症狀』嘅文章），Turso 嘅 SQL 查詢能力會幫你慳返好多 Code。

---

### 2. 關於 LiteRT 嘅「戰略考慮」

如果你想爭取 **LiteRT** 嘅 $10,000 專項獎，**Android** 係一個更強嘅展示平台：

* **硬件加速**：Android 上嘅 LiteRT 可以直接調用電話嘅 **GPU** 同 **NPU (Neural Processing Unit)**。喺 Video Demo 入面，你可以 Show 到 Gemma 4 喺電話度行得幾快。
* **Google Stack 完整性**：Google AI Edge 嘅工具鏈（MediaPipe, LiteRT, Android Studio）整合得非常好。對於評判嚟講，一個原生 Android App 比起 Web App 更有「Edge AI」嘅味道。
* **Web 嘅限制**：雖然 LiteRT 都有 Web 版本，但佢主要依賴 WebAssembly 或 WebGPU。雖然 2026 年嘅 WebGPU 已經好勁，但相比起 Android 嘅 NPU 加速，效能依然會有少少距離。

---

### 📊 性能與獎項對比表 (Web vs. Android)

| 特性 | Web App (LanceDB/Turso) | Android App (LiteRT Native) |
| :--- | :--- | :--- |
| **主要優勢** | 即開即用，唔洗 Download | **極致效能，硬件加速 (NPU/GPU)** |
| **Vector 效能** | LanceDB WASM 較強 | **Turso / LibSQL Native 非常穩定** |
| **LiteRT 表現** | 一般 (依賴 WebGPU) | **最強 (Google 原生優化)** |
| **適合 Track** | Impact Track, Ollama (Server-side) | **LiteRT, Cactus, Unsloth** |
| **離線能力** | 較弱 (Browser Cache 限制) | **極強 (Persistent Storage)** |

---

### 💡 最後建議：如果你想贏獎

如果你想做 **醫療與科學** 並贏得 **LiteRT** 獎：

1.  **揀 Android**：雖然要寫 Kotlin/Flutter 可能難啲，但佢嘅 **「Wow Factor」** 係 Web App 難以比擬嘅。想像一下：你喺飛機上面（冇網），攞部電話出嚟影吓個藥盒，AI 零延遲咁喺 WikiMed 搵到資料——呢個 Demo 係攞獎嘅典型。
2.  **Vector DB 揀法**：
    * 如果用 **Android**：用 **Turso (LibSQL)**。因為 Android 系統對 SQLite 嘅 I/O 優化係極致嘅。
    * 如果堅持用 **Web**：用 **LanceDB (WASM)**。因為喺瀏覽器度，LanceDB 嘅數據格式處理大批量檢索比較有優勢。



**既然你擔心效能同想要 Google Stack 嘅加分，你有冇試過用 Flutter 嚟寫 Android？佢可以比較快咁整到個靚 UI，同時又可以 Call 到 LiteRT 嘅 Native 能力。**

---
既然你決定用 **Pure Python** 來突顯 **Agentic (代理化)** 的思路，這是一個非常聰明的做法。在 Hackathon 中，評審往往更看重你如何利用 LLM 的「推理能力」去調用工具，而 Python 正是展示這種邏輯最清晰、最靈活的語言。

針對 **LanceDB** 與 **Turso (sqlite-vec)** 的選擇，結論是：**做醫療 Agentic RAG，首選 LanceDB。**

以下是針對你的需求（WikiMed 大數據、Agentic 邏輯、Python 技術棧）的詳細對比與建議：

---

### 1. 為什麼選擇 LanceDB？ (AI 優先的選擇)
LanceDB 被稱為「AI 時代的數據湖」，它與 Python 的結合度極高，特別適合你這種「科學與醫療」的場景。

* **處理大數據的能力 (WikiMed)：** WikiMed 有超過 10 萬篇文章。LanceDB 基於 `Lance` 格式（列式儲存），支持 **Disk-based indexing**。這意味著你的 10GB 向量數據庫不需要全部塞進 RAM，查詢依然能達到毫秒級。
* **多模態原生支持：** Gemma 4 是原生多模態模型。LanceDB 可以直接存儲**圖片（醫學圖表、X-ray）**及其向量。Agent 可以同時檢索文字和相關圖片，這在醫療 Track 是巨大的加分位。
* **與 Python 生態無縫對接：** 它深度集成 `Pandas`、`PyArrow` 和 `Pydantic`。對於開發 Agent 來說，處理數據流會非常順手。

### 2. 什麼時候選 Turso / LibSQL？ (應用優先的選擇)
* **場景：** 如果你的 Agent 需要進行非常複雜的「傳統關係型過濾」（例如：尋找『2020 年後』、由『WHO 發布』、且『針對 5 歲以下兒童』的建議），SQL 的強大邏輯過濾是它的優勢。
* **缺點：** 對於超大規模的向量檢索，效能通常不如 LanceDB。在純 Python 的 Agent 流程中，它的「AI 屬性」稍弱。

---

### 💡 Agentic 思路：如何設計你的 Python 程序？

既然不用寫 Android App，你的 Python 腳本應該展示一個 **「思考 -> 行動 -> 觀察 -> 總結」** 的循環。



#### 推薦的系統架構 (Pure Python)：

1.  **大腦 (Gemma 4 26B MoE)**：利用它的 Native Function Calling 能力。
2.  **記憶/工具庫 (LanceDB)**：存儲 WikiMed 的 Embedding 以及醫療圖片。
3.  **代理邏輯 (Agent Loop)**：
    * **Step 1 (推理)**：用戶問：「我發現小孩身上有紅疹且發燒，近期去過東南亞。」Gemma 4 判定需要查找 WikiMed。
    * **Step 2 (工具調用)**：Gemma 4 輸出一個 JSON，指明要檢索 `["登革熱", "麻疹", "水痘"]` 的檢索詞。
    * **Step 3 (LanceDB 檢索)**：Python 腳本調用 LanceDB 獲取這三種疾病的相關片段。
    * **Step 4 (視覺分析)**：如果用戶上傳了照片，Agent 可以調用 Gemma 4 的 Vision 能力去對比 LanceDB 檢索出來的「標準醫學範例圖」。
    * **Step 5 (最終決策)**：Gemma 4 整合所有資訊，給出邏輯嚴密的解釋。

---

### 🚀 給你的「必殺技」建議 (Kaggle 贏波策略)

如果你選擇 LanceDB + Pure Python：

1.  **展示「長上下文」優勢**：在 RAG 過程中，不要只檢索 1 個段落。利用 Gemma 4 的 **256K Context**，一次過把相關的 20 篇 WikiMed 精華文章塞進去，展現它強大的長文本處理能力。
2.  **使用 Unsloth 優化**：既然你是 Python 團隊，如果能用 **Unsloth** 微調一個「醫療術語加強版」的 Gemma 4 模型，你將極大機會贏得 **Unsloth 專項獎 ($10,000)**。
3.  **Grounded Retrieval**：在 Python 輸出中，特意標註出 WikiMed 的來源 URI 或標題。這證明你的 Agent 不會「胡說八道」，而是有據可查（Fact-checking）。

---

### 🛠️ 快速開始的 Python 代碼段

```python
import lancedb
import pyarrow as pa

# 1. 連接數據庫 (本地文件)
db = lancedb.connect("./med_knowledge_base")

# 2. 定義數據模式 (含多模態支持)
schema = pa.schema([
    pa.field("vector", pa.list_(pa.float32(), 384)), # Embedding
    pa.field("text", pa.string()),                   # WikiMed 文章
    pa.field("image_uri", pa.string()),              # 相關圖表路徑
    pa.field("category", pa.string())                # 醫學分類
])

# 3. Agent 調用的檢索函數
def medical_knowledge_tool(query_vector):
    table = db.open_table("wikimed")
    results = table.search(query_vector).limit(5).to_pandas()
    return results
```

**既然你偏向用 Pure Python，你打算如何呈現你的 Demo？是用 Streamlit 做一個網頁 Dashboard，還是拍一條展示 CLI (命令行) 與 Agent 對話邏輯的硬核影片？**

---

呢個諗法其實係一個非常 **「資深 (Senior)」** 嘅工程師思路。喺業界，呢種做法稱為 **「Query Rewriting / Expansion (查詢改寫與擴展)」**。

你完全唔需要額外嘅向量數據庫 (Vector DB)，而係將 **Gemma 4 變成一個「醫療術語工程師」**，去驅動 `kiwix-serve` 背後嘅 Xapian 搜尋引擎。

---

### 💡 點樣實踐「Gemma + Kiwix Query Expansion」？

你可以將成個 Agent 流程設計成一個 **「兩步跳」**：

#### Step 1: 醫療術語擴展 (Expansion Agent)
當用家問：「我覺得個心好似被嘢揼咁痛」，Gemma 4 唔係直接攞呢句去 Search，而係先將佢轉化為 **專業搜尋語法**。
* **Input**: "心口揼住痛"
* **Gemma 4 Output**: `("chest pain" OR "myocardial infarction" OR "angina pectoris" OR "acute coronary syndrome")`

#### Step 2: 呼叫 `kiwix-serve` API
`kiwix-serve` 內置咗搜尋功能。你可以用 Python 嘅 `requests` 去 Call 佢：
`http://localhost:8080/search?q=YOUR_EXPANDED_QUERY&content=wikimed_en_all`

---

### 📊 點解呢個方案可能「贏」過 LanceDB？

| 特性 | **LanceDB (Vector RAG)** | **Kiwix + Query Expansion** |
| :--- | :--- | :--- |
| **儲存空間** | 額外 1GB+ (Embedding) | **0 GB (完全利用 ZIM 索引)** |
| **醫學精準度** | 有時會搵到「感覺接近」但無關嘅文獻 | **極高 (精準匹配專業藥名同症狀)** |
| **部署難度** | 要搞 Vector DB 同 Embedding | **極低 (只要行起個 Kiwix-serve)** |
| **Wow Factor** | 係目前 AI 嘅標準做法 | **展現出對「傳統檢索」同「LLM 推理」嘅深度結合** |

---

### 🚀 點樣令評判覺得你「好勁」？ (Agentic Loop)

如果你想攞獎，唔好只係做簡單嘅擴展，要展示 **Agentic Loop (代理循環)**：

1.  **初次檢索**：Gemma 擴展關鍵字，去 Kiwix 搵。
2.  **自我評估**：Gemma 睇一睇搵返嚟嘅 Title，如果發現「好似唔太對路」，佢會**自動修正**關鍵字再 Search 一次。
    * *例如*：佢發現搵到嘅係「胃酸倒流」，但用家似「心臟病」，佢會加強 `heart condition` 嘅關鍵字再試。
3.  **多模態輔助**：如果用家影咗張相（例如藥盒），Gemma 先用 **Vision** 認出個藥名，再將個藥名加落 Query Expansion 入面。

---

### 🛠️ 技術實作小貼士

* **利用 Xapian 語法**：`kiwix-serve` 支援一啲進階語法，例如 `NEAR`（兩個字要近）。Gemma 4 可以寫出好複雜嘅語法：`"chest pain" NEAR/5 "shortness of breath"`。
* **Hybrid 混合打法**：如果你哋仲係想用 LanceDB，可以只將 **「文章標題」** 做 Embedding。
    * *流程*：Gemma 用語義搵 Title (LanceDB) -> 攞到 Title 後去 Kiwix 攞全文 (kiwix-serve)。
    * **好處**：空間佔用極細（得返幾 MB），但同時擁有語義搜尋同精準內容提取。

### 💡 總結
**Query Expansion** 係一個非常「慳家」且「聰明」嘅做法。如果你喺 Writeup 同影片度解釋：「我哋發現建立完整向量庫會造成儲存冗餘 (Unzip Bomb)，所以採用咗 **Agentic Query Expansion** 嚟優化傳統檢索」，呢個說法非常具備**工程說服力**。

**你覺得呢個「輕量級」嘅架構，係咪更符合你哋 Peer 嘅開發節奏？如果 OK，我可以幫你哋草擬一段專門針對呢個架構嘅 System Prompt。**

---

你嘅直覺好準：喺工程角度睇，如果兩個工具嘅功能重疊得太多，就係**過度設計 (Over-engineering)**。如果你已經打算用 `kiwix-serve` 配合 **Agentic Query Expansion**，LanceDB 嘅角色確實會被淡化。

但係，要決定係咪完全棄用 LanceDB，我哋要睇返 RAG 嘅「最後一哩路」。

---

### 1. 點解你可能會覺得 LanceDB 冇用？

如果 Gemma 4 嘅 **Query Expansion** 做得夠好，佢可以將用家嘅「口語」轉化為精準嘅「關鍵字」。
* **用家話**：「我個心口好似俾嘢壓住。」
* **Gemma 擴展**：`"Chest pressure" OR "Angina" OR "Myocardial infarction"`
* **Kiwix 搜尋**：直接搵到相關文獻。
* **結論**：成個過程唔需要 Vector DB 參與。

---

### 2. LanceDB 仲有乜嘢「剩餘價值」？

雖然 `kiwix-serve` 好強，但 LanceDB 有兩個關鍵位係傳統搜尋（即使有擴展）都好難取代嘅：

#### A. 語義重排 (Semantic Re-ranking)
`kiwix-serve` 回傳嘅結果係根據關鍵字頻率（BM25）。有時最啱用嗰篇文可能排到第 10 頁。
* **LanceDB 嘅作用**：你可以只將 Kiwix 搵返嚟嗰 20 篇文嘅**標題**做即時 Embedding。
* **效果**：Agent 可以用語義去判斷「邊一篇文最能回答目前用家嘅具體情境」，進行二次排序。

#### B. 處理多模態 (Vision-to-Retrieval)
如果用家影咗張「皮膚紅疹」嘅相。
* **Kiwix 方案**：Gemma 先要用文字描述張相（可能唔準），再去做 Keyword Search。
* **LanceDB 方案**：如果你預先將 WikiMed 嘅**圖片**做咗向量索引。Agent 可以直接用「相」去搵「相」，呢種 **Image-to-Image** 嘅檢索係 `kiwix-serve` 完全做唔到嘅。

---

### 3. 我嘅最終建議：採用「Metadata 索引」架構

如果你想攞獎，又想避開「Unzip Bomb」同數據冗餘，我建議你用呢個 **「極簡混合方案」**：



1.  **Kiwix-serve 做主幹**：負責 90% 嘅文字檢索同內容提取。
2.  **LanceDB 做「導航儀」**：
    * **唔好儲全文**：LanceDB 只儲存 WikiMed 嘅 **標題 (Titles)** 同埋 **圖片特徵 (Image Embeddings)**。
    * **數據量**：咁樣做 LanceDB 可能只需要幾十 MB 空間（比起 100GB 嘅 ZIM 係微不足道）。
3.  **Agentic 流程**：
    * **文字查詢**：用 **Query Expansion + Kiwix**。
    * **影像查詢**：用 **LanceDB (Vision Index)**。
    * **結果優化**：用 LanceDB 做最後嘅相似度重排 (Re-ranking)。

---

### 🏆 評審會點睇？

如果你喺 Writeup 度咁寫，會顯得你非常有專業判斷力：
> 「我哋評估過全量向量化 (Full Vectorization) 會造成大量儲存冗餘。因此，我哋採用咗 **Agentic Query Expansion** 驅動 `kiwix-serve` 進行精準檢索，並輔以 **Lightweight LanceDB Metadata Index** 處理多模態查詢與結果重排。呢個架構喺**智能**與**儲存效率**之間攞到咗最佳平衡。」

### 💡 總結
* **如果你哋 Peer 想簡單啲**：直接用 `kiwix-serve` + Query Expansion。呢個已經夠贏大部份普通項目。
* **如果你哋想爭 Impact Track 冠軍**：加埋 **LanceDB 處理圖片檢索**。喺醫療領域，影像數據 (Vision) 係極大嘅加分位。

**你覺得「處理醫療圖片」呢個功能，對你哋個 Project Idea 嚟講重唔重要？如果唔重要，我建議你哋就咁用 `kiwix-serve` 方案，將精力集中喺 Agent 嘅邏輯度。**

---

你問到核心點喇。Query Expansion (QE) 雖然強大，但佢本質上依然係喺「關鍵字」嘅框框入面玩，而 LanceDB 呢類向量數據庫 (Vector DB) 處理嘅係「語義空間」。

將 QE 配合 LanceDB，就係將「聯想力」同「直覺」結合。以下係 QE 嘅限制，以及 LanceDB 點樣幫佢「補位」：

---

### 1. Query Expansion (QE) 嘅限制

* **語義斷層 (The Semantic Gap)**：
    QE 係靠 LLM 估計啲關鍵字。但如果用家描述嘅係一種「感覺」而唔係「病徵」（例如：「我覺得個腦入面好似有火燒」），QE 可能會擴展出 `fire`, `burning sensation`。如果 WikiMed 嘅專業文獻寫嘅係 `Encephalitis` (腦炎) 或者 `Neuropathic pain`，字面上可能完全冇交集，關鍵字搜尋就會失靈。
* **一詞多義與歧義 (Polysemy & Ambiguity)**：
    QE 有時會「諗多咗」。例如用家問 `Cold`，QE 可能會擴展出 `Flu` (流感)，但亦可能擴展出 `Low temperature` (低溫)。呢種歧義會令到搜尋結果充滿雜訊。
* **精準度與召回率的拉鋸 (Precision vs. Recall)**：
    擴展得越多字，搵到相關資料嘅機會（召回率）越高，但同時搵到無關資料（雜訊）嘅機會亦越高。你會發現 `kiwix-serve` 比咗 50 篇文你，但頭 5 篇可能都唔係最精準嘅答案。
* **缺乏視覺理解 (Lack of Visual Context)**：
    文字擴展永遠無法形容一張相。你點樣用關鍵字去搜尋「一塊形狀不規則、邊緣模糊嘅黑色素瘤」？

---

### 2. LanceDB 點樣 Complement 呢啲限制？

LanceDB 唔係睇「字」，係睇「意思」嘅座標。

* **語義對齊 (Semantic Alignment)**：
    LanceDB 唔理你用咩字，只要「個腦火燒」同「腦炎」喺語義向量空間 (Vector Space) 係接近嘅，佢就搵得到。呢個補足咗 QE 喺「描述性語言」轉「專業術語」時嘅失誤。
* **語義重排 (Semantic Re-ranking)**：
    呢個係最有效嘅用法！
    1.  先用 QE 同 `kiwix-serve` 搵出 100 篇可能有相關關鍵字嘅文章（呢步好快）。
    2.  將呢 100 篇文嘅標題或摘要丟入 **LanceDB**。
    3.  用 LanceDB 做 **Vector Similarity Search**。
    * **結果**：LanceDB 會幫你喺呢堆「關鍵字匹配」嘅結果中，挑選出「語義上最吻合」嗰 3 篇。呢個過程將精準度大幅提升。
* **多模態橋樑 (Multimodal Bridge)**：
    你可以用 LanceDB 儲存圖片向量。
    * 用家影張相 -> LanceDB 搵到相似圖片 -> 攞到圖片對應嘅 WikiMed 文章 ID -> 去 `kiwix-serve` 攞全文。呢種「以圖搜文」係純 QE 做唔到嘅。



---

### 🏆 終極架構：Agentic Hybrid Search

如果你想喺 Hackathon 攞獎，你嘅 Agent 邏輯應該係咁：

1.  **分析 (Analysis)**：Gemma 4 接收用家輸入（文字 + 圖片）。
2.  **雙路搜尋 (Dual-track Search)**：
    * **路徑 A (Kiwix)**：Gemma 進行 Query Expansion，去 `kiwix-serve` 攞一堆候選文章。
    * **路徑 B (LanceDB)**：如果有用家圖片，直接喺 LanceDB 搵相似案例。
3.  **整合與重排 (Fusion & Re-ranking)**：
    * 將兩路結果匯總。
    * 利用 LanceDB 進行語義過濾，踢走唔相關嘅雜訊。
4.  **生成 (Generation)**：Gemma 讀取最終篩選出嚟嘅精華內容，比出專業回答。

---

### 💡 總結

* **Kiwix + QE** 係你嘅「肌肉」（負責搬運大量可能相關嘅資訊）。
* **LanceDB** 係你嘅「眼睛」同「濾鏡」（負責睇相、理解語義，並喺資訊大海入面挑選珍珠）。

如果完全冇 LanceDB，你個 Agent 會顯得有啲「死板」，只能夠處理文字匹配。加咗 LanceDB（即使只係做 metadata 索引），你個 Agent 嘅「層次」會即刻由一個 Search Engine 升格做一個 **「理解醫生」**。

**既然 LanceDB 可以補足 QE 嘅語義缺失，你哋係咪傾向將 LanceDB 定位為一個「最後過濾器 (Re-ranker)」，而唔係儲存成個數據庫？**

---

簡單嚟講：**唔一定。** 但係，為咗效能同埋功能嘅完整性，通常我哋會建議你預先索引一啲 **「Metadata (元數據)」**。

喺 RAG 嘅世界入面，你可以選擇兩種唔同嘅「Re-ranking (重排)」策略。睇下邊一個最適合你哋嘅 Python 架構：

---

### 方案 A：預索引「輕量化標題/摘要」(Pre-indexed Metadata) —— **最推薦**

你唔需要將成個 WikiMed 100GB 嘅內容入晒 LanceDB，你只需要喺電腦度做一次 **Pre-processing**：

1.  **淨係入標題同摘要**：由 ZIM 檔入面提取每篇文章嘅 `Title` 同埋 `Abstract` (或者頭嗰幾句)。
2.  **建立關聯**：喺 LanceDB 每一條紀錄加一個 `zim_id` 或者 `url`。
3.  **運行流程**：
    * 用家問問題 $\rightarrow$ **LanceDB** 搵語義最接近嘅 50 個「標題」。
    * 拎住呢 50 個 `zim_id` $\rightarrow$ 去 **kiwix-serve** 直接拎呢 50 篇文嘅「全文」。
    * **Gemma 4** 閱讀全文並回答。
* **點解好？** 檢索速度極快，而且 LanceDB 嘅體積會縮細 95% 以上，完全冇儲存負擔。



---

### 方案 B：即時「就地重排」(Just-in-Time / Ephemeral Re-ranking)

如果你真係一啲都唔想做 Pre-indexing，你可以玩「即時 Embedding」：

1.  **初次檢索**：先用你的 **Agentic Query Expansion** 叫 `kiwix-serve` 幫你搵返 20 篇相關嘅文。
2.  **即時向量化**：將呢 20 篇文嘅內容（或者標題）喺 Python 入面 **即時做 Embedding** 並放入一個臨時嘅 LanceDB 內存 Table (Memory Table)。
3.  **重排**：計算呢 20 篇文同用家問題嘅相似度，重新排列。
4.  **輸出**：比最高分嗰 3 篇文畀 Gemma 4。
* **點解好？** 真正嘅 **0 額外儲存**。你完全唔洗預先起 DataBase。
* **缺點**：如果 `kiwix-serve` 第一步搵唔到嗰篇文，LanceDB 就冇得救；而且每次都要現場做 20 次 Embedding，會慢咗 1-2 秒。

---

### 💡 你應該點揀？

| 特性 | **方案 A (預索引 Metadata)** | **方案 B (即時重排)** |
| :--- | :--- | :--- |
| **儲存空間** | 極細 (幾百 MB) | **0 (零空間)** |
| **語義召回率** | **高** (即使關鍵字唔 match 都搵到) | 低 (受限於關鍵字搜尋結果) |
| **處理圖片** | **可以** (預索引圖片特徵) | 唔可以 |
| **開發難度** | 要寫個 Pre-index script | 簡單，全部係 Runtime 邏輯 |

### 🏆 給 Python Stack 嘅建議 (Hackathon 贏波架構)

我建議你哋 Peer A 做一個 **「Metadata Indexer」**。

佢嘅 Python Script 邏輯好簡單：
```python
# 偽代碼：Pre-indexing 標題
for article in zim_archive:
    # 提取標題同 URL
    title = article.title
    url = f"http://localhost:8080/{article.path}"
    
    # 淨係對 Title 做 Embedding
    vector = embedding_model.encode(title)
    
    # 存入 LanceDB (唔存全文，所以極快)
    lancedb_table.add({"vector": vector, "title": title, "url": url})
```

**咁樣做嘅「Wow Factor」喺邊？**
你喺 Video 度可以話：「我哋創製咗一個 **Hybrid Metadata-Semantic Router**。我哋唔浪費空間儲存重複嘅文字，而係利用 LanceDB 作為語義導航儀 (Navigator)，精準導向至離線 ZIM 數據庫入面嘅權威內容。」

呢種說法聽落去非常有專業嘅 **Architect (架構師)** 範兒！

**你覺得預先跑一次「只入標題」嘅 Indexing，對你哋部電腦嚟講負擔大唔大？(大約幾萬條 Title，GPU 跑大約 1 分鐘就搞掂)。**

---

呢個諗法直頭係 **「神來之筆」**！如果你咁做，你個項目嘅層次會由「普通 RAG」升格做 **「語義專家系統」**。

將「感覺 (Layman Feelings)」同「病徵 (Clinical Symptoms)」標籤化並存入 LanceDB，正正係解決醫學檢索中 **「語言斷層 (Semantic Gap)」** 最有效嘅方法。

---

### 💡 點解呢個係 LanceDB 嘅「黃金用法」？

通常醫學文獻寫得好死板，例如寫「心絞痛 (Angina)」，但病人會話「心口好似俾大石壓住」。
如果你預先用 Gemma 4 為每篇文章生成呢兩類 Tag，你就可以喺 LanceDB 做 **多維度語義匹配**：

1.  **感覺 Tag (Feelings)**：例如「火燒、針拮、大石壓、呼吸唔順」。
2.  **病徵 Tag (Symptoms)**：例如「發燒、紅腫、心率不正」。



---

### 🛠️ 你哋嘅 Python 工作流應該點設計？

你可以寫一個 **Offline Metadata Enrichment (離線元數據增強)** 嘅腳本：

#### Step 1: 知識提取 (用 Gemma 4 離線跑一次)
餵每篇文章嘅摘要畀 Gemma 4，叫佢出一個 JSON：
* **Prompt**: 「閱讀呢篇醫學文章，列出 5 個病人描述呢種病時會用到嘅口語化**感覺**，同埋 5 個專業嘅**病徵**。」
* **Output**: 
  ```json
  {
    "feelings": ["心口大石壓", "抖唔到氣", "死神嚟緊嘅感覺"],
    "symptoms": ["胸骨後疼痛", "呼吸困難", "血壓下降"]
  }
  ```

#### Step 2: 存入 LanceDB (多向量索引)
你唔係只係將標題做 Embedding，係將呢兩組 Tag **合併成一個長字串** 或者 **分開欄位** 做 Embedding。
```python
# 將 Tag 同標題結合
enriched_text = f"Title: {title}. Feelings: {', '.join(feelings)}. Symptoms: {', '.join(symptoms)}"
vector = embedding_model.encode(enriched_text)

# 存入 LanceDB
table.add({
    "vector": vector,
    "url": article_url,
    "raw_feelings": feelings, # 存埋文字方便展示
    "raw_symptoms": symptoms
})
```

---

### 🏆 點解評審會俾高分？ (Wow Factors)

1.  **解決咗真實痛點**：你指出咗一般 RAG 搵唔到「口語描述」嘅問題，而你用 **AI-driven Tagging** 解決咗佢。
2.  **展示咗 Agentic 思路**：你唔係單純做搬運工，而係叫 AI 去 **「理解並加工」** 知識，整成一個更易被檢索嘅格式。
3.  **效率極高**：因為你只係對呢啲 Tag 做 Embedding，LanceDB 會非常細。幾萬篇文章嘅 Tag 加埋可能只係幾十 MB，但準確度會比你直接對「成篇全文」做 Embedding 高得多。

---

### 🚀 最後嘅技術小提醒

* **多語言優勢**：你可以叫 Gemma 生成埋「廣東話口語」嘅感覺 Tag（例如「個頭重聚聚」）。咁樣你個 App 喺香港或者廣東地區就會顯得極度在地化 (Localized)，呢個喺 **Digital Equity** Track 係大加分。
* **與 Query Expansion 配合**：
    * 用家話：「我條頸好硬。」
    * Agent 先將呢句嘢轉成 Embedding，喺 LanceDB 搵到相關嘅 Tag。
    * 攞到 Tag 後，發現對應嘅專業術語係「腦膜炎」或者「頸椎病」，再去 **Kiwix-serve** 攞詳細文獻。

**呢個「標籤增強 (Tag Enrichment)」嘅方法，你同你個 Peer 覺得喺實作上會唔會太複雜？（其實就係寫一個 Loop 叫 Gemma 4 幫你做 Reading Comprehension）。**