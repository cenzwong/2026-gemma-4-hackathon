import os
import time
from datetime import datetime
from enum import Enum, auto
from typing import Dict, Any, Callable, Optional
from baml_client.sync_client import b
from kiwix import Kiwix
from llm.utils import stream_generate_content
from llm.models import GemmaModel

class State(Enum):
    IDLE = auto()
    TRIAGE = auto()
    SEARCH_VEC = auto()
    SEARCH_KIWIX = auto()
    REASONING = auto()
    OUTPUT = auto()

class MedicalAgentFSM:
    def __init__(self, callbacks: Optional[Dict[str, Callable]] = None):
        self.state = State.IDLE
        self.context: Dict[str, Any] = {'history': []}
        self.callbacks = callbacks or {}
        
        self.action_callback = self.callbacks.get('log_action')
        self.source_callback = self.callbacks.get('log_source')
        self.output_callback = self.callbacks.get('update_output')

        # Setup file logging
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = f"logs/session_{timestamp}.log"
        self._write_log(f"--- Session Started at {timestamp} ---\n")

    def _write_log(self, text: str):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(text + "\n")
        except Exception:
            pass

    def _log_action(self, msg: str):
        self._write_log(f"[ACTION] {msg}")
        if self.action_callback:
            self.action_callback(msg)
        else:
            print(msg)

    def _log_source(self, msg: str):
        self._write_log(f"[SOURCE] {msg}")
        if self.source_callback:
            self.source_callback(msg)
        else:
            print(msg)

    def run(self, user_input: str):
        self._log_action(f"> Starting FSM with input: '{user_input}'")
        self.context['history'].append(f"User: {user_input}")
        self.context['user_input'] = user_input
        self._log_action("\n[🔄 STATE: TRIAGE] Initiating medical triage process...")
        self.state = State.TRIAGE

        while self.state != State.IDLE:
            if self.state == State.TRIAGE:
                self._handle_triage()
            elif self.state == State.SEARCH_VEC:
                self._handle_search_vec()
            elif self.state == State.SEARCH_KIWIX:
                self._handle_search_kiwix()
            elif self.state == State.REASONING:
                self._handle_reasoning()
            elif self.state == State.OUTPUT:
                self._handle_output()
            else:
                raise ValueError(f"Unknown state: {self.state}")

    def _handle_triage(self):
        self._log_action("> [Thought] Analyzing patient input for sufficient medical context...")
        history_str = "\n".join(self.context['history'])
        
        eval_result = b.EvaluateInformation(history_str)
        
        if not eval_result.has_enough_info:
            symptoms = b.ExtractSymptoms(history_str)
            symptoms_str = ", ".join(symptoms.symptoms) if symptoms.symptoms else "none explicit"
            self._log_action(f"> [Reasoning] Insufficient info detected. Current known symptoms: ({symptoms_str})")
            self._log_action("> [Action] Asking follow-up question to gather more details.")
            
            followup = b.AskFollowUpQuestion(symptoms_str, history_str)
            self._write_log(f"[OUTPUT] {followup}")
            if self.output_callback:
                self.output_callback(followup, True)
            self.context['history'].append(f"Agent: {followup}")
            self._log_action("> [Status] Generation complete.")
            self._log_action("\n[🔄 STATE: IDLE] Waiting for patient response.")
            self.state = State.IDLE
        else:
            self._log_action("> [Reasoning] Sufficient medical info confirmed. We can proceed with diagnosis.")
            self._log_action("\n[🔄 STATE: SEARCH_KIWIX] Initiating offline medical database search...")
            self.state = State.SEARCH_KIWIX

    def _handle_search_vec(self):
        self._log_action("> [State: SEARCH_VEC] Querying LanceDB for semantic tags and titles...")
        self.context['vec_results'] = [{"title": "Example Disease", "tag": "disease"}]
        self._log_action("  [Action] Found relevant vectors. Moving to Full Text Search.")
        self._log_action("\n[🔄 STATE: SEARCH_KIWIX] Searching Kiwix databases...")
        self.state = State.SEARCH_KIWIX

    def _handle_search_kiwix(self):
        history_str = "\n".join(self.context['history'])
        
        self._log_action("> [Thought] Generating search keywords based on dialogue history...")
        keywords = b.DecodeQuestion(history_str)
        if not keywords:
            self._log_action("> [Warning] Could not extract structured keywords. Using raw input.")
            keywords = [self.context.get('user_input', '')]
        else:
            self._log_action(f"> [Reasoning] Generated keywords: {', '.join(keywords)}")
            
        base_url = os.getenv("KIWIX_SERVER_URL", "http://192.168.8.152:8080").rstrip('/')
        
        try:
            self._log_action(f"> [Action] Checking Kiwix server heartbeat at {base_url}...")
            kiwix_client = Kiwix(base_url)
            if not kiwix_client.is_online():
                self._log_action("  [WARNING] Kiwix server heartbeat failed. Server is offline.")
                self.context['kiwix_full_texts'] = []
                self._log_action("\n[🔄 STATE: REASONING] Proceeding without Kiwix sources...")
                self.state = State.REASONING
                return
            books = kiwix_client.get_kiwix_book()
        except Exception as e:
            self._log_action(f"  [ERROR] Cannot connect to Kiwix server: {e}")
            self.context['kiwix_full_texts'] = []
            self._log_action("> [Status] Skipping Kiwix search due to connection error.")
            self._log_action("\n[🔄 STATE: REASONING] Proceeding to reasoning phase...")
            self.state = State.REASONING
            return
            
        example_book = next((b for b in books if "medicine" in (b.name or "").lower()), books[0] if books else None)
        
        if not example_book:
            self._log_action("  [Warning] No medical books found in Kiwix. Falling back to general knowledge.")
            self.context['kiwix_full_texts'] = []
            self._log_action("\n[🔄 STATE: REASONING] Proceeding to reasoning phase...")
            self.state = State.REASONING
            return
            
        articles = []
        for query in keywords:
            self._log_action(f"> [Action] Querying Kiwix-serve for keyword: '{query}'...")
            try:
                articles = example_book.search_article(query)
                if articles:
                    self._log_action(f"> [Success] Found {len(articles)} relevant articles for '{query}'.")
                    break
                else:
                    self._log_action(f"  [Info] No articles found for '{query}', trying next keyword...")
            except Exception as e:
                self._log_action(f"  [ERROR] Search failed for '{query}': {e}")
                
        if not articles:
            self._log_action("  [Warning] No articles found for any keyword in the medical database.")
            self.context['kiwix_full_texts'] = []
            self._log_action("\n[🔄 STATE: REASONING] Proceeding to reasoning phase...")
            self.state = State.REASONING
            return
            
        full_texts = []
        self._log_action("> [Thought] Extracting full text from relevant Kiwix articles...")
        for idx, article in enumerate(articles[:3]):
            # Make the title a clickable terminal link
            # article.url from python-kiwix is usually a relative path starting with /
            url = f"{base_url}{article.url}" if str(article.url).startswith('/') else f"{base_url}/{article.url}"
            source_msg = f"📄 Source {idx+1}: [link={url}]{article.title}[/link]"
            if article.snippet:
                source_msg += f"\n   Match: \"{article.snippet[:100]}...\"\n"
            self._log_source(source_msg)
            
            if article.path:
                html, headers = article.get_article()
                exclude_headers = ["References", "External links", "Further reading", "Notes"]
                filtered_headers = [h for h in headers if h.name not in exclude_headers]
                
                article_text = f"Title: {article.title}\n"
                for h in filtered_headers[:3]:
                    article_text += f"{h.name}: {h.text[:500]}\n"
                full_texts.append(article_text)
                
        self.context['kiwix_full_texts'] = full_texts
        self._log_action("> [Status] Full text successfully retrieved.")
        self._log_action("\n[🔄 STATE: REASONING] Proceeding to final medical reasoning...")
        self.state = State.REASONING

    def _handle_reasoning(self):
        self._log_action("> [Thought] Reading context & formulating final response...")
        self._log_action("  [████████████░░░░] Prompting Gemma-4-26b-MoE-4bit...")
        
        context_texts = self.context.get('kiwix_full_texts', [])
        context_str = "\n\n".join(context_texts)
        user_input = self.context.get('user_input', '')
        
        prompt = f"You are a helpful offline medical assistant named Dr. Offline. Use the provided medical reference texts to answer the user's query.\n\nMedical Reference:\n{context_str}\n\nUser Query: {user_input}\n\nProvide a concise, helpful, and grounded answer. If you use information from the references, mention the source title. ALWAYS include a disclaimer that you are an AI and they should seek professional medical help."
        
        model = GemmaModel.GEMMA_4_26B_A4B_IT.model_id
        
        try:
            final_resp = ""
            for chunk in stream_generate_content(prompt=prompt, model_id=model, thinking_level=None):
                final_resp += chunk
                if self.output_callback:
                    self.output_callback(chunk, True)
            self._write_log(f"[OUTPUT] {final_resp}")
            self.context['history'].append(f"Agent: {final_resp}")
            self._log_action("> [Status] Diagnosis generation complete.")
        except Exception as e:
             if self.output_callback:
                 self.output_callback(f"\n\n**Error:** {str(e)}", True)
             self._log_action(f"> [ERROR] Generation failed: {str(e)}")
                 
        self._log_action("\n[🔄 STATE: IDLE] Waiting for next input.")
        self.state = State.IDLE

    def _handle_output(self):
        self.state = State.IDLE

if __name__ == "__main__":
    fsm = MedicalAgentFSM()
    fsm.run("I have a severe headache and nausea.")
