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

class NomadApp(App):
    """NOMAD: Offline Medical Agent TUI"""
    
    TITLE = "NOMAD: Offline Medical Agent"
    CSS_PATH = "tui.tcss"

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.current_content = ""

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Static("🚀 NOMAD: Offline Medical Agent    [Model: Gemma-4-26b-MoE-4bit] [RAM: 82%]", id="header_bar")
        
        with Horizontal(id="top_panels"):
            yield AgentStatePanel(id="agent_state", wrap=True, markup=True)
            yield GroundedSourcesPanel(id="grounded_sources", wrap=True, markup=True)
            
        yield DiagnosticOutputPanel(id="diagnostic_output_container")
        yield UserInputPanel(id="user_input_container")
            
        yield Footer()

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one("#prompt_input").focus()
        await self._add_mock_data()

    async def _add_mock_data(self) -> None:
        """Populates the TUI with the initial mock data to match the design."""
        agent_log = self.query_one("#agent_state", AgentStatePanel)
        agent_log.log_action("> Analyzing patient input...")
        agent_log.log_action("> Extracting keywords:\n  (\"chest pain\" OR \"pressure\")")
        agent_log.log_action("> Querying Kiwix-serve (Local)...")
        agent_log.log_action("> Found 3 relevant articles.")
        agent_log.log_action("> Reading context & reasoning...")
        agent_log.log_action("  [████████████░░░░] Processing Context")

        source_log = self.query_one("#grounded_sources", GroundedSourcesPanel)
        source_log.log_source("📄 Source 1: Angina Pectoris")
        source_log.log_source("   Relevance Score: High")
        source_log.log_source("   Match: \"pressure in chest...\"\n")
        source_log.log_source("📄 Source 2: Myocardial Infarction")
        source_log.log_source("   Relevance Score: Medium")
        source_log.log_source("   Match: \"pain radiating to...\"")
        
        self.current_content = (
            "Agent: Based on the local medical database, the \"crushing chest pain\" you described could be related to the following conditions:\n\n"
            "1. Angina Pectoris [Source 1]\n"
            "   This is usually caused by reduced blood flow to the heart muscles, often described as a heavy pressure or squeezing in your chest.\n\n"
            "2. Heart Attack (Myocardial Infarction) [Source 2]\n"
            "   If the pain radiates to your left arm or jaw, and is accompanied by a cold sweat or shortness of breath, this is a medical emergency.\n\n"
            "⚠️ Note: I am an offline AI assistant. If your symptoms persist or worsen, please seek immediate physical medical assistance.\n█"
        )
        diag_panel = self.query_one("#diagnostic_output_container", DiagnosticOutputPanel)
        await diag_panel.update_content(self.current_content)

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
        
        # Start streaming response
        self.stream_response(prompt)

    @work(thread=True)
    def stream_response(self, prompt: str) -> None:
        """Stream the LLM response in a background thread."""
        model = GemmaModel.GEMMA_4_26B_A4B_IT.model_id
        tools = [
            types.Tool(googleSearch=types.GoogleSearch()),
        ]
        
        agent_log = self.query_one("#agent_state", AgentStatePanel)
        diag_panel = self.query_one("#diagnostic_output_container", DiagnosticOutputPanel)
        
        self.call_from_thread(agent_log.log_action, "> Analyzing patient input...")
        
        try:
            for text_chunk in stream_generate_content(
                prompt=prompt, 
                model_id=model, 
                tools=tools
            ):
                self.current_content += text_chunk
                self.call_from_thread(diag_panel.update_content, self.current_content)
                
            self.current_content += "\n\n---\n\n"
            self.call_from_thread(diag_panel.update_content, self.current_content)
            self.call_from_thread(agent_log.log_action, "> Generation complete.")
                
        except Exception as e:
            self.current_content += f"\n\n**Error:** {str(e)}\n\n---\n\n"
            self.call_from_thread(diag_panel.update_content, self.current_content)

if __name__ == "__main__":
    app = NomadApp()
    app.run()
