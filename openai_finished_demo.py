import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

print("Hello! Ask your question in any language and you'll receive an answer in Lithuanian. Type 'exit' to quit.")

while True:
    try:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Iki!")
            break
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Always reply in Lithuanian language.",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            temperature=1.0,
            top_p=1.0,
        )
        
        print(response.choices[0].message.content)

    except Exception as e:
        print("Klaida:", str(e))
