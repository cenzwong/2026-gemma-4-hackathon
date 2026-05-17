# Dr. Offline: Video Demo Script

**Target Length:** ~2-3 Minutes
**Tone:** Urgent, Technical, Impactful
**Track:** Global Resilience

---

### Scene 1: The Problem (0:00 - 0:30)

**[Visual]**
*   *B-roll footage or striking images: Natural disasters, remote clinics, disconnected regions.*
*   *Text overlay: "When the grid fails, cloud AI fails."*
*   *Cut to a person typing into a standard AI chatbot on a phone, receiving a "No internet connection" error.*

**[Audio/Voiceover]**
"In disaster zones and remote regions, access to reliable medical intelligence is often a matter of life and death. Modern AI models are incredibly powerful, but they share one fatal flaw: they assume you have high-bandwidth internet. When the grid fails, cloud-based models become useless. The people who need intelligence the most are completely cut off."

---

### Scene 2: The Solution (0:30 - 0:50)

**[Visual]**
*   *Transition to the Dr. Offline logo or title card.*
*   *Show a ruggedized laptop or a simple field device running the Textual UI.*
*   *Text overlay: "Dr. Offline: Edge Medical Reasoning Engine / Powered by Gemma 4"*

**[Audio/Voiceover]**
"Enter Dr. Offline. We've built an air-gapped, fully offline medical triage and retrieval system. By engineering an intelligent Retrieval-Augmented Generation pipeline optimized for edge computing, we're bringing the power of Google's Gemma 4 26B MoE model directly to the disconnected frontline—running entirely on local hardware."

---

### Scene 3: How It Works & Demo (0:50 - 1:45)

**[Visual]**
*   *Screen recording of the Dr. Offline Textual User Interface (TUI).*
*   *User types a vague layman symptom: "My chest feels like there's a heavy rock on it."*
*   *Split screen or overlay showing the FSM (Finite State Machine) workflow lighting up: TRIAGE -> SEARCH -> REASONING -> OUTPUT.*

**[Audio/Voiceover]**
"Let's see it in action. Dr. Offline abandons the standard chatbot design for a strict Agentic Workflow governed by a Finite State Machine. This prevents the model from guessing or hallucinating medical advice.

When a user inputs a layman symptom, Gemma 4 doesn't just start talking. First, it acts as an intelligent semantic router. Using BAML to enforce structured JSON outputs, Gemma 4 translates 'heavy rock on chest' into precise clinical search terms."

**[Visual]**
*   *Highlight the TUI's "Agent State" or "Thought Process" panel showing the BAML extraction of terms like `myocardial infarction` or `angina pectoris`.*
*   *Show the Kiwix server rapidly retrieving offline WikiMed articles.*

**[Audio/Voiceover]**
"Next, instead of a massive, memory-hogging vector database, we use Kiwix to search an offline, highly compressed copy of WikiMed. We completely avoided the 'unzip bomb' of vectorizing hundreds of thousands of articles, keeping our storage footprint incredibly light."

**[Visual]**
*   *Show the final output streaming into the UI, with clear citations to the WikiMed articles.*

**[Audio/Voiceover]**
"Finally, we inject the complete text of the top retrieved articles straight into Gemma 4's massive 256K Context Window. Gemma cross-references the documents and generates a grounded, life-saving response that strictly cites the provided text."

---

### Scene 4: Hardware Efficiency (1:45 - 2:15)

**[Visual]**
*   *Diagram showing Gemma 4 26B MoE routing mechanism (highlighting the ~4B active parameters).*
*   *Show a terminal window running the 4-bit quantized model via Ollama.*

**[Audio/Voiceover]**
"Running a 26 billion parameter model at the edge sounds impossible. But we specifically chose the Gemma 4 MoE architecture for its hardware efficiency—the Router mechanism only activates about 4 billion parameters per token.

By deploying via Ollama with 4-bit quantization, we compressed the VRAM requirements from over 50 gigabytes down to roughly 15. This allows the entire intelligence pipeline to run fluently on consumer-grade laptops in the field."

---

### Scene 5: Conclusion (2:15 - 2:30)

**[Visual]**
*   *Final shot of the laptop in a field setting or the Dr. Offline title screen.*
*   *Text overlay: "Dr. Offline / Global Resilience Track"*

**[Audio/Voiceover]**
"Dr. Offline proves that world-class medical reasoning no longer requires a lifeline to the cloud. By intelligently combining the hardware efficiency of Gemma 4 with the offline robustness of Kiwix, we are democratizing medical intelligence for the edge—where it's needed most."
