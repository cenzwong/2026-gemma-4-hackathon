import os
from typing import Optional, List, Generator
from google import genai
from google.genai import types

def get_client() -> genai.Client:
    """Returns a configured Gemini client."""
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def stream_generate_content(
    prompt: str, 
    model_id: str, 
    tools: Optional[List[types.Tool]] = None, 
    thinking_level: Optional[str] = "HIGH"
) -> Generator[str, None, None]:
    """Streams generated content from the model."""
    client = get_client()
    
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    
    config_args = {}
    if thinking_level:
        config_args["thinking_config"] = types.ThinkingConfig(thinking_level=thinking_level)
    if tools:
        config_args["tools"] = tools

    generate_content_config = types.GenerateContentConfig(**config_args)

    response = client.models.generate_content_stream(
        model=model_id,
        contents=contents,
        config=generate_content_config,
    )
    
    for chunk in response:
        if text := chunk.text:
            yield text
