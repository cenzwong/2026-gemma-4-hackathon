### **Detailed Technical Breakdown**

#### **1. Cactus (The Mobile Router)**
* **What it is:** A specialized framework for **Intelligent Routing** on mobile and wearable devices.
* **The Problem it Solves:** Mobile devices have limited battery and heat constraints. You can't run a 26B model 24/7.
* **How it Works:** Cactus acts as a traffic controller. It evaluates a user's query:
    * *Simple Task:* Routes to a tiny, ultra-fast on-device model.
    * *Complex Task:* Routes to Gemma 4 26B (if a local server is available) or a cloud endpoint.
* **Best for:** Projects involving smartwatches, medical sensors, or Android/iOS apps where battery life is critical.

#### **2. LiteRT (The Edge Optimizer)**
* **What it is:** Google AI Edge’s successor to TensorFlow Lite (TFLite) for LLMs.
* **The Problem it Solves:** Standard Python-based AI stacks are too heavy for mobile OS environments.
* **How it Works:** It converts Gemma 4 into a highly optimized format that can talk directly to a phone's **NPU (Neural Processing Unit)** or GPU. It focuses on low-latency inference on "bare-metal" or mobile platforms.
* **Best for:** Creating a native Android/iOS medical app that works 100% offline without needing a Python backend.

#### **3. llama.cpp (The Foundation of Portability)**
* **What it is:** A C++ implementation of the Gemma/Llama architecture designed for CPU-first inference.
* **The Problem it Solves:** GPUs are expensive. Most people in "AI for Good" scenarios have standard laptops with CPUs.
* **How it Works:** It uses **GGUF quantization**. It allows you to run Gemma 4 26B on a standard Mac or PC by offloading parts of the model to System RAM instead of just VRAM.
* **Best for:** The "Project NOMAD" approach. If you want to run Gemma 4 on a ruggedized laptop in a disaster zone, this is the engine you use.

#### **4. Ollama (The User Experience Layer)**
* **What it is:** A user-friendly wrapper built (mostly) on llama.cpp.
* **The Problem it Solves:** Managing model weights, environment variables, and API endpoints is a headache.
* **How it Works:** It bundles everything into a single service. You run `ollama run gemma4` and it handles the rest. It provides a local REST API that your "Orchestrator" (from our architecture diagram) can talk to easily.
* **Best for:** Rapid prototyping. If you want to get your medical assistant running in 5 minutes and focus on the **Kiwix** integration rather than the C++ compiler, pick Ollama.

#### **5. Unsloth (The Efficiency Specialist)**
* **What it is:** A library designed to make **Fine-Tuning** incredibly fast and memory-efficient.
* **The Problem it Solves:** Fine-tuning a 26B or 31B model usually requires massive GPU clusters ($$$).
* **How it Works:** It uses specialized kernels to reduce memory usage by up to 70%. You can fine-tune Gemma 4 on a single consumer GPU (like an RTX 3090/4090).
* **Best for:** If you find that the base Gemma 4 doesn't understand specific medical terminology in your **WikiMed** files, you use Unsloth to "teach" it that specific data before you deploy it.

---

### **Technology Stack Comparison**

| Feature | **LiteRT** | **llama.cpp** | **Ollama** | **Unsloth** |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Goal** | Mobile Inference | Hardware Portability | Ease of Use | Fine-Tuning |
| **Platform** | Android, iOS, IoT | PC, Mac, Linux | PC, Mac, Linux | GPU Servers |
| **Language** | C++, Java, Swift | C++ | Go, Python (via API) | Python (PyTorch) |
| **Best Hardware** | Phone NPU/GPU | CPU + RAM | Consumer GPU/CPU | High-end GPU |
| **Use Case** | Wearable health monitor | Ruggedized medical server | Quick prototype app | Specialized "Expert" model |

---

### **Strategic Recommendation for Your Project**

If you are following our plan of an **Offline Medical Oracle using Kiwix**, here is your winning tech-stack combination:

1.  **Fine-tuning (Optional but high-impact):** Use **Unsloth** to fine-tune Gemma 4 on a subset of the Hesperian Health Guides. This makes your model a "Medical Specialist" rather than a "Generalist."
2.  **Inference Engine:** Use **Ollama** or **llama.cpp**. 
    * If you want to win the **Ollama** track ($10k), focus on the ease of deployment and the API integration.
    * If you want to win the **llama.cpp** track ($10k), focus on how you've optimized the model to run on a low-resource "constrained" laptop (e.g., using 4-bit or 1.5-bit quantization).

> **Expert Guide Note:** Given your interest in the "Project NOMAD" concept, focusing on the **llama.cpp** or **Ollama** tracks provides the most direct path to success because they are designed for the "local-first" philosophy you've chosen.

Which of these technical "challenges" sounds most interesting to you: **optimizing the model for the weakest possible hardware** (llama.cpp) or **fine-tuning it to be a medical expert** (Unsloth)?


---

呢五個 **Special Technology Track** 係呢次 Hackathon 嘅「技術加分區」。如果你個 project 可以一邊解決社會問題（例如離線醫療），一邊用到呢啲工具去優化效能，你就有機會同時攞埋呢 $10,000 美金嘅專項獎。

以下係呢五套技術棧 (Tech Stack) 嘅深度對比同分析：

---

### **1. 核心技術介紹**

#### **🌵 Cactus (智能任務路由)**
* **定位：** 行動裝置/穿戴裝置嘅「交通指揮官」。
* **核心功能：** 佢可以自動判斷一個任務應該喺本地（細模型）行，定係交畀雲端（大模型）行。
* **點解揀佢：** 如果你個醫療 project 涉及用智能手錶監測病人，Cactus 可以幫你慳電，得喺有危險嗰陣先啟動 Gemma 4 做深度分析。

#### **📱 LiteRT (Google AI Edge 官方方案)**
* **定位：** 以前叫 TensorFlow Lite，係 Google 官方針對 Android/iOS 硬件優化嘅推理引擎。
* **核心功能：** 直接調用手機嘅 **NPU (神經處理單元)**。
* **點解揀佢：** 如果你想整一個原生嘅 Android App，而且想發揮手機粒 chip 嘅最高效能，LiteRT 係最穩陣嘅「親生仔」選擇。

#### **🏗️ llama.cpp (跨平台、低配硬件救星)**
* **定位：** 將大模型變做純 C++ 實作，唔洗 GPU 都可以喺 CPU 同 RAM 上面行。
* **核心功能：** 支援 **GGUF** 格式同埋極致嘅量化技術 (Quantization)。
* **點解揀佢：** **最夾 Project NOMAD。** 如果你想喺一部舊嘅電腦或者 Raspberry Pi 上面行 Gemma 4 26B，呢個係唯一可以將模型壓到極細、同時維持速度嘅工具。

#### **🦙 Ollama (最易用嘅本地 API 封裝)**
* **定位：** 基於 llama.cpp 嘅一個「包裝盒」，令你可以好似用 Docker 咁管理 AI 模型。
* **核心功能：** 提供一鍵部署同埋現成嘅 REST API。
* **點解揀佢：** 如果你想專注寫 Python 邏輯去玩 **Kiwix/ZIM**，而唔想搞編譯 (Compiling) 嘅嘢，用 Ollama 最快手。

#### **🦥 Unsloth (Fine-tuning 煉丹神器)**
* **定位：** 專門優化微調 (Fine-tuning) 過程，將速度提升 2 倍，VRAM 需求減低 70%。
* **核心功能：** 支援 QLoRA 技術，等你可以喺一張平價顯卡度幫 Gemma 4 做「特訓」。
* **點解揀佢：** 如果你發現 Gemma 4 唔太識醫學專有名詞，你可以用 Unsloth 餵佢食 WikiMed 嘅數據，整一個「專業版」模型。

---

### **📊 技術棧對比表 (Comparison)**

| 技術工具 | 適用平台 | 最大賣點 | 硬件需求 | 適合邊個 Track？ |
| :--- | :--- | :--- | :--- | :--- |
| **Cactus** | 手機、穿戴裝置 | 任務分流、慳電 | 低 (Mobile) | Health (監測類) |
| **LiteRT** | Android, iOS | Google 官方 NPU 加速 | 中 (High-end Phone) | Equity (手機應用) |
| **llama.cpp** | PC, Mac, Linux | **唔洗 GPU** 都行到 | 中 (需要多啲 RAM) | **Global Resilience** |
| **Ollama** | PC, Mac, Linux | 最快建立 Local API | 中 (GPU/CPU) | Education (教學 Bot) |
| **Unsloth** | Server (GPU) | **微調最快**、最慳 VRAM | 高 (需要 GPU) | Safety (專業化模型) |

---

### **💡 針對你 Project 嘅策略建議**

如果你係想跟返我哋之前傾嗰個「離線醫療百科」計劃，我有以下建議：

1.  **想贏 llama.cpp 獎 ($10,000)：** 專注做「硬件優化」。證明你點樣用 4-bit GGUF 格式，令 Gemma 4 26B 喺一部 16GB RAM 嘅普通手提電腦度都能夠順暢讀取 WikiMed。
2.  **想贏 Unsloth 獎 ($10,000)：** 做「垂直領域微調」。你可以攞 Hesperian 或者 WikiMed 入面最精華嘅幾千條問答，用 Unsloth 嚟 fine-tune 一個專門針對「災難急救」嘅 Gemma 4，咁樣會比通用模型強好多。
3.  **想贏 Ollama 獎 ($10,000)：** 做「系統整合」。利用 Ollama 嘅 API 嚟串連你個 **Orchestrator** 同 **Kiwix**，展示一個完整、易於安裝嘅「醫學離線盒子」方案。

**總結：** 你可以同時揀 **llama.cpp** 做推理引擎，並用 **Unsloth** 做微調，咁你就有機會同時角逐兩份技術獎同埋一份 Impact Track 獎！

你覺得對於你嚟講，係**「將模型行得順」 (llama.cpp)** 定係 **「將模型教得更專業」 (Unsloth)** 比較吸引？


---

While you *can* use multiple technologies in your project, the most successful strategy for a $200,000 hackathon is to **lead with one and support with others.**

In a competitive field (already over 4,600 entrants in early April 2026), judges for the **Special Technology Track** are looking for "Technical Mastery." A project that uses everything superficially will likely be overlooked in favor of a project that pushes the absolute limits of one specific tool.

Here is the strategic breakdown for your Kiwix + Gemma 4 RAG project:

---

## 1. The "Lead" Strategy (Pick Your $10,000 Target)
Since you are building an **air-gapped RAG solution**, your project naturally aligns with three specific prizes. Choose the one that matches your strongest engineering skill:

### Option A: The "llama.cpp" Path (The Hardcore Engineer)
* **The Pitch:** "The most efficient, high-performance RAG on a $100 Raspberry Pi 5."
* **Why for you:** Since you're focused on air-gapped environments, the **llama.cpp** prize is your best bet. You can showcase custom GGUF quantization levels for Gemma 4 and how you optimized the `libzim` extraction to not starve the CPU while the LLM is inferencing.
* **Winning Move:** Demonstrate sub-2 second "Time to First Token" on a device with no GPU.

### Option B: The "Unsloth" Path (The Data Scientist)
* **The Pitch:** "Gemma 4 fine-tuned specifically to understand the internal structure of ZIM/Wikipedia archives."
* **Why for you:** If you want to improve the **Main Track** score (Accuracy), fine-tuning is key. You can use Unsloth to train Gemma 4 on "Retrieval-Specific" tasks (e.g., learning to ignore HTML noise or citing sources correctly).
* **Winning Move:** Show a benchmark where your "Gemma-4-ZIM" model outperforms the base model at extracting facts from your ZIM data.

### Option C: The "Cactus" Path (The Systems Architect)
* **The Pitch:** "A resilient RAG that seamlessly switches between a local Kiwix cache and a remote server."
* **Why for you:** This fits if your project isn't *always* air-gapped but needs to be "offline-ready."
* **Winning Move:** Film a demo where you pull the Ethernet cable mid-query, and Cactus routes the rest of the task to the local `kiwix-serve` instance without crashing.

---

## 2. The "Support" Tech (Don't Mention it for the Prize)
You can still use the other tools to make your life easier, but don't waste your 1,500-word writeup describing them in detail.
* **Use Ollama** to quickly prototype your RAG logic.
* **Use LiteRT** if you need a quick mobile interface for the demo.
* **BUT**, in your submission, frame these as "utility tools" while focusing your "Technical Depth" section (30 points) on your **Lead** technology.

---

## 3. Recommended Roadmap (5 Weeks Remaining)

| Week | Task | Strategy |
| :--- | :--- | :--- |
| **Week 1** | **Ingestion Engine** | Build the `libzim` $\to$ **LanceDB** pipeline. |
| **Week 2** | **Deep Dive (Lead Tech)** | Spend the entire week on your chosen prize (e.g., optimizing llama.cpp kernels). |
| **Week 3** | **RAG Integration** | Connect Gemma 4 to the context provided by Kiwix. |
| **Week 4** | **Impact Story** | Finalize your "Global Resilience" use case (Education/Disaster response). |
| **Week 5** | **The Video** | Remember: The video is **70% of the weight** (Impact + Storytelling). |

### My Professional Advice:
Given that you are new to Kiwix but want an air-gapped solution, aim for the **llama.cpp prize**. It is the most "honest" implementation for air-gapped hardware, and it demonstrates a high level of technical execution that judges in the **Safety & Trust** or **Global Resilience** impact tracks will respect.

Which of those three "Options" (llama.cpp, Unsloth, or Cactus) sounds like the most fun for you to build?
