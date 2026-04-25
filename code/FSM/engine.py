from enum import Enum, auto
from typing import Dict, Any

class State(Enum):
    IDLE = auto()
    TRIAGE = auto()
    SEARCH_VEC = auto()
    SEARCH_KIWIX = auto()
    REASONING = auto()
    OUTPUT = auto()

class MedicalAgentFSM:
    def __init__(self):
        self.state = State.IDLE
        self.context: Dict[str, Any] = {}

    def run(self, user_input: str):
        """
        Main loop to run the Finite State Machine.
        """
        print(f"--- Starting FSM with input: '{user_input}' ---")
        self.context['user_input'] = user_input
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
        """
        State: TRIAGE (預檢)
        判斷係咪醫療問題。
        """
        print("[State: TRIAGE] Analyzing if query is medical-related...")
        user_input = self.context.get('user_input', '')
        
        # TODO: call LLM to triage
        is_medical = True # Dummy check
        
        if not is_medical:
            print("-> Not a medical query.")
            self.context['final_response'] = "請詢問與醫療相關的問題。"
            self.state = State.OUTPUT
        else:
            print("-> Medical query confirmed. Moving to Query Expansion and Search.")
            self.state = State.SEARCH_VEC

    def _handle_search_vec(self):
        """
        State: SEARCH_VEC (語義搜索)
        Call LanceDB 搵 Tag/Title。
        """
        print("[State: SEARCH_VEC] Querying LanceDB for semantic tags and titles...")
        
        # TODO: Call LanceDB
        self.context['vec_results'] = [{"title": "Example Disease", "tag": "disease"}]
        
        print("-> Found relevant vectors. Moving to Full Text Search.")
        self.state = State.SEARCH_KIWIX

    def _handle_search_kiwix(self):
        """
        State: SEARCH_Kiwix (全文檢索)
        Call Android 嗰邊個 kiwix-serve API 攞 Full Text。
        """
        print("[State: SEARCH_KIWIX] Fetching full text from kiwix-serve API...")
        
        # TODO: Call kiwix-serve API
        self.context['kiwix_full_texts'] = ["Full text context for the disease..."]
        
        print("-> Full text retrieved. Moving to Reasoning.")
        self.state = State.REASONING

    def _handle_reasoning(self):
        """
        State: REASONING (推理與校對)
        Gemma 4 對比兩邊資料。如果資料不足，轉返去 TRIAGE 問用家攞更多病徵。
        """
        print("[State: REASONING] Gemma 4 reasoning based on grounded context...")
        
        # TODO: Call Gemma 4 LLM to reason and check if more info is needed
        needs_more_info = False # Dummy check
        
        if needs_more_info:
            print("-> Insufficient information. Asking user for more details.")
            self.context['final_response'] = "資料不足，請提供更多病徵 (例如：有冇發燒？痛咗幾耐？)。"
            self.state = State.OUTPUT
        else:
            print("-> Reasoning successful. Moving to Output.")
            self.context['final_response'] = "根據 WikiMed 資料，您的情況可能是... (此為 AI 建議，請尋求專業醫生協助)"
            self.state = State.OUTPUT

    def _handle_output(self):
        """
        State: OUTPUT (回覆)
        標明 WikiMed 出處並回覆。
        """
        print("[State: OUTPUT] Generating final response to user...")
        response = self.context.get('final_response', '')
        
        # 確保標明出處
        if "WikiMed" not in response and "請詢問與醫療相關" not in response:
            response = f"[Source: WikiMed] {response}"
            
        print(f"> Agent Response: {response}")
        
        # 完成任務，回到 IDLE
        self.state = State.IDLE

if __name__ == "__main__":
    # 測試
    fsm = MedicalAgentFSM()
    fsm.run("我今日有啲頭痛同發燒")
