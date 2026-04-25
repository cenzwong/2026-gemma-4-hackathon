# To run this code you need to install the following dependencies:
# pip install google-genai

from dotenv import load_dotenv
from google.genai import types

from llm.models import GemmaModel
from llm.utils import stream_generate_content

load_dotenv()


def generate():
    model = GemmaModel.GEMMA_4_26B_A4B_IT.model_id
    prompt = "Who is Cenz?"
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]
    
    for text_chunk in stream_generate_content(
        prompt=prompt, 
        model_id=model, 
        tools=tools
    ):
        print(text_chunk, end="")
    print()

if __name__ == "__main__":
    generate()


