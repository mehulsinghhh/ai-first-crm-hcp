from groq import Groq

# IMPORTANT:
# Replace YOUR_GROQ_API_KEY_HERE later with your real Groq API key
client = client = Groq(api_key="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")

def call_groq(prompt: str, model: str = "llama-3.1-8b-instant"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an AI CRM assistant for life science field representatives."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content