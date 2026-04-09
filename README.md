# 2026-gemma-4-hackathon
Planning Stage &amp; Code


https://www.kaggle.com/competitions/gemma-4-good-hackathon

- 解決「細」嘅大問題
- Unsloth 微調
- llama.cpp 優化 量化（Quantization）過程
- 展示到 Gemma 4 處理影像（Vision）
- 唔好只係 Demo 畫面，要講出一個故事, 影片係靈魂
- 強調「邊緣運算」 (Edge Deployment)
- 突出 Agent 屬性

- Agentic Workflow (代理工作流)： 唔好只係問答。要 show 到你個 Agent 會「思考 -> 拆解任務 -> 調用工具 (Function Calling) -> 檢查結果 -> 完成」。

- Edge Architecture (邊緣架構)： 比賽非常睇重 Gemma 係開源且輕量 呢個點。所以，如果你能證明你個 App 喺一部 $2000 蚊嘅舊 Android 電話度行到（用 LiteRT），評判會覺得你真正發揮咗 Gemma 嘅價值。

- 醫學倫理說明： 喺影片或 Writeup 結尾，加一小段關於「AI 點樣輔助醫生而非取代醫生」嘅說明，呢點對醫療 Track 嘅評審（如 Google DeepMind 嘅醫學專家）好重要。
- Demo 完整性： 唔好只係 show 一個 Jupyter Notebook。整一個簡單嘅 Streamlit 或 Flutter App 界面，展示成個 Agent 點樣「接收相片 -> 思考 -> 查資料 -> 比出建議」。
- 如果要贏 LiteRT 獎項，Android 確實係 Google AI Edge 嘅「主場」。



Reference project:
- https://www.threads.com/@akilife3386/post/DWwTGpPlIV3?xmt=AQF08IAigEGEUUEbMG3UuyBw0I8iFz5hxu1fPsOuSy6D2Iegqn3GYebNASMUjH4DStW2G9M&slof=1
- https://github.com/Crosstalk-Solutions/project-nomad
