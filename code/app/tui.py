import sys
import os
from pathlib import Path

# Add the project root to sys.path so we can import llm module
sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer, Horizontal, Vertical
from textual.widgets import Header, Footer, Input, Markdown, RichLog, Static
from textual import work

from llm.utils import stream_generate_content
from llm.models import GemmaModel
from google.genai import types

from FSM.engine import MedicalAgentFSM

load_dotenv()

class AgentStatePanel(RichLog):
    """Panel for displaying the agent's state and thought process."""
    def on_mount(self) -> None:
        self.border_title = "[1] Agent State & Thought Process"

    def log_action(self, text: str) -> None:
        self.write(text)

class GroundedSourcesPanel(RichLog):
    """Panel for displaying grounded sources from Kiwix."""
    def on_mount(self) -> None:
        self.border_title = "[3] Grounded Sources (Kiwix)"

    def log_source(self, text: str) -> None:
        self.write(text)

class DiagnosticOutputPanel(Vertical):
    """Panel for displaying the main diagnostic reasoning output."""
    def on_mount(self) -> None:
        self.border_title = "[2] Diagnostic Output (Gemma 4 Reasoning)"

    def compose(self) -> ComposeResult:
        with ScrollableContainer(id="diagnostic_scroll"):
            yield Markdown(id="diagnostic_output")

    async def update_content(self, content: str) -> None:
        md = self.query_one("#diagnostic_output", Markdown)
        await md.update(content)
        scroll = self.query_one("#diagnostic_scroll", ScrollableContainer)
        scroll.scroll_end(animate=False)

class UserInputPanel(Vertical):
    """Panel for user input."""
    def on_mount(self) -> None:
        self.border_title = "[4] User Input (Patient / Medic)"

    def compose(self) -> ComposeResult:
        yield Input(placeholder="> Doctor, my chest feels like it's being crushed, and I'm sweating a bit._", id="prompt_input")

    def get_input(self) -> Input:
        return self.query_one("#prompt_input", Input)

class DrOfflineApp(App):
    """Dr. Offline: Offline Medical Agent TUI"""
    
    TITLE = "Dr. Offline: Offline Medical Agent"
    CSS_PATH = "tui.tcss"

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
        ("ctrl+n", "new_patient", "New Patient"),
    ]

    def __init__(self):
        super().__init__()
        self.current_content = ""
        self.fsm = None

    def init_fsm(self):
        callbacks = {
            'log_action': self.log_action_callback,
            'log_source': self.log_source_callback,
            'update_output': self.update_output_callback,
        }
        self.fsm = MedicalAgentFSM(callbacks=callbacks)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Static("🚀 Dr. Offline: Offline Medical Agent    [Model: Gemma-4-26b-MoE-4bit] [RAM: 82%]", id="header_bar")
        
        with Horizontal(id="top_panels"):
            yield AgentStatePanel(id="agent_state", wrap=True, markup=True)
            yield GroundedSourcesPanel(id="grounded_sources", wrap=True, markup=True)
            
        yield DiagnosticOutputPanel(id="diagnostic_output_container")
        yield UserInputPanel(id="user_input_container")
            
        yield Footer()

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.init_fsm()
        self.query_one("#prompt_input").focus()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        """Handle when the user presses Enter in the Input widget."""
        if not message.value.strip():
            return
            
        prompt = message.value
        diag_panel = self.query_one("#diagnostic_output_container", DiagnosticOutputPanel)
        
        # Clear existing logs for new prompt
        self.query_one("#agent_state", AgentStatePanel).clear()
        self.query_one("#grounded_sources", GroundedSourcesPanel).clear()
        
        # Display the user's prompt
        self.current_content = f"**User:** {prompt}\n\n**Agent:** "
        await diag_panel.update_content(self.current_content)
        
        # Clear the input
        self.query_one(UserInputPanel).get_input().value = ""
        
        # Start FSM response
        self.run_fsm(prompt)

    def log_action_callback(self, text: str) -> None:
        agent_log = self.query_one("#agent_state", AgentStatePanel)
        self.call_from_thread(agent_log.log_action, text)

    def log_source_callback(self, text: str) -> None:
        source_log = self.query_one("#grounded_sources", GroundedSourcesPanel)
        self.call_from_thread(source_log.log_source, text)

    def update_output_callback(self, text: str, append: bool = False) -> None:
        diag_panel = self.query_one("#diagnostic_output_container", DiagnosticOutputPanel)
        if append:
            self.current_content += text
        else:
            self.current_content = text
        self.call_from_thread(diag_panel.update_content, self.current_content)

    @work(thread=True)
    def run_fsm(self, prompt: str) -> None:
        """Run the FSM in a background thread."""
        self.call_from_thread(self._set_loading, True)
        try:
            if self.fsm is None:
                self.init_fsm()
            self.fsm.run(prompt)
        finally:
            self.call_from_thread(self._set_loading, False)

    def _set_loading(self, is_loading: bool) -> None:
        """Toggle loading state and UI indicators."""
        user_input_panel = self.query_one(UserInputPanel)
        user_input_panel.loading = is_loading
        
        agent_panel = self.query_one("#agent_state", AgentStatePanel)
        if is_loading:
            agent_panel.border_title = "[1] Agent State & Thought Process (Working...)"
            agent_panel.border_subtitle = "⏳"
        else:
            agent_panel.border_title = "[1] Agent State & Thought Process"
            agent_panel.border_subtitle = ""

    async def action_new_patient(self) -> None:
        """Clear the UI for a new patient session."""
        self.query_one("#agent_state", AgentStatePanel).clear()
        self.query_one("#grounded_sources", GroundedSourcesPanel).clear()
        
        diag_panel = self.query_one("#diagnostic_output_container", DiagnosticOutputPanel)
        self.current_content = ""
        await diag_panel.update_content(self.current_content)
        
        input_widget = self.query_one(UserInputPanel).get_input()
        input_widget.value = ""
        input_widget.focus()
        self.init_fsm()

if __name__ == "__main__":
    app = DrOfflineApp()
    app.run()
