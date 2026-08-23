# openai_client.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_false_premise(premise: str, model: str = "gpt-4o-mini") -> str:
    """
    Present a false premise and observe the model's response.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": premise}],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content
