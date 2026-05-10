from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, RichLog, Static
from textual.containers import Horizontal, Vertical

class NomadApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }

    #header {
        dock: top;
        height: 1;
        content-align: center middle;
        background: $boost;
        color: $text;
    }

    #top_panels {
        height: 1fr;
        layout: horizontal;
    }

    #agent_state {
        width: 1fr;
        height: 100%;
        border: round $primary;
    }

    #grounded_sources {
        width: 1fr;
        height: 100%;
        border: round $secondary;
    }

    #diagnostic_output {
        height: 2fr;
        border: round $accent;
    }

    #user_input_container {
        height: 4;
        border: round $success;
    }

    #user_input {
        width: 100%;
        border: none;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("🚀 NOMAD: Offline Medical Agent    [Model: Gemma-4-26b-MoE-4bit] [RAM: 82%]", id="header")
        with Horizontal(id="top_panels"):
            yield RichLog(id="agent_state")
            yield RichLog(id="grounded_sources")
        yield RichLog(id="diagnostic_output")
        with Vertical(id="user_input_container"):
            yield Input(placeholder="> _", id="user_input")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#agent_state").border_title = "[1] Agent State & Thought Process"
        self.query_one("#grounded_sources").border_title = "[3] Grounded Sources (Kiwix)"
        self.query_one("#diagnostic_output").border_title = "[2] Diagnostic Output (Gemma 4 Reasoning)"
        self.query_one("#user_input_container").border_title = "[4] User Input (Patient / Medic)"
        
        # Add some mock text
        log1 = self.query_one("#agent_state", RichLog)
        log1.write("> Analyzing patient input...")
        log1.write("> Extracting keywords:\n  (\"chest pain\" OR \"pressure\")")
        
        log2 = self.query_one("#grounded_sources", RichLog)
        log2.write("📄 Source 1: Angina Pectoris")
        
        log3 = self.query_one("#diagnostic_output", RichLog)
        log3.write("Agent: 根據本地醫療數據庫資料...")

if __name__ == "__main__":
    app = NomadApp()
    app.run()
