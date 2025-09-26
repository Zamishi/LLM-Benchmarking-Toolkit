import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_KEY")
openai.api_key = OPENAI_API_KEY

def ask_openai(prompt):
    # Placeholder: use actual API call for research or mock
    # return response text
    return f"OpenAI response for: {prompt[:50]}..."
