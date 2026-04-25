import sys
import os
from pathlib import Path

# Add the project root to sys.path so we can import llm module
sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Input, Markdown
from textual import work

from llm.utils import stream_generate_content
from llm.models import GemmaModel
from google.genai import types

load_dotenv()

class LLMTUIApp(App):
    """A Textual TUI for interacting with Gemma LLM."""

    CSS = """
    Screen {
        layout: vertical;
    }
    #chat_scroll {
        height: 1fr;
        border: solid green;
        padding: 1;
        margin: 1;
    }
    Input {
        dock: bottom;
        margin: 1;
    }
    """

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.current_content = "Welcome to **Gemma-4** TUI!\n\nType your prompt below to start.\n\n---\n\n"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with ScrollableContainer(id="chat_scroll"):
            yield Markdown(self.current_content, id="chat_output")
        yield Input(placeholder="Type your prompt here and press Enter...", id="prompt_input")
        yield Footer()

    def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one("#prompt_input").focus()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        """Handle when the user presses Enter in the Input widget."""
        if not message.value.strip():
            return
            
        prompt = message.value
        md = self.query_one("#chat_output", Markdown)
        
        # Display the user's prompt
        self.current_content += f"**You:** {prompt}\n\n**Gemma:** "
        await md.update(self.current_content)
        
        # Clear the input
        self.query_one("#prompt_input").value = ""
        
        # Start streaming response
        self.stream_response(prompt)

    @work(thread=True)
    def stream_response(self, prompt: str) -> None:
        """Stream the LLM response in a background thread."""
        model = GemmaModel.GEMMA_4_26B_A4B_IT.model_id
        tools = [
            types.Tool(googleSearch=types.GoogleSearch()),
        ]
        
        try:
            for text_chunk in stream_generate_content(
                prompt=prompt, 
                model_id=model, 
                tools=tools
            ):
                self.current_content += text_chunk
                self.call_from_thread(self.update_markdown, self.current_content)
                
            self.current_content += "\n\n---\n\n"
            self.call_from_thread(self.update_markdown, self.current_content)
                
        except Exception as e:
            self.current_content += f"\n\n**Error:** {str(e)}\n\n---\n\n"
            self.call_from_thread(self.update_markdown, self.current_content)

    async def update_markdown(self, content: str) -> None:
        """Update the markdown widget safely from the main thread."""
        md = self.query_one("#chat_output", Markdown)
        await md.update(content)
        
        # Scroll to bottom
        scroll = self.query_one("#chat_scroll", ScrollableContainer)
        scroll.scroll_end(animate=False)


if __name__ == "__main__":
    app = LLMTUIApp()
    app.run()
