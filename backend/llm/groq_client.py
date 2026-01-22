import os
from groq import Groq

def call_groq(prompt: str, model: str = "llama-3.3-70b-versatile"):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI CRM assistant for life science field representatives."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
