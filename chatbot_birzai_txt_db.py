import os
from openai import OpenAI
from dotenv import load_dotenv

# Load data from birzai.txt
def load_birzai_db(file_path="C:\\GEN-AI MOKYMAI 2025\\GIT_Gediminas811\\Repo_Python_codes\\birzai.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Load credentials
def load_credentials():
    load_dotenv()
    token = os.getenv("SECRET")
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1-nano"
    return token, endpoint, model

# Create OpenAI client
def create_client(api_key, base_url):
    return OpenAI(api_key=api_key, base_url=base_url)

# Ask questions using the same context
def chat_with_context(client, model, context):
    print("Klauskite apie Biržus. Norėdami išeiti, rašykite 'exit' arba 'quit'.")
    while True:
        try:
            question = input("Jūsų klausimas: ").strip()
            if question.lower() in ["exit", "quit"]:
                print("Iki pasimatymo!")
                break

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are very useful assistant. Do not use any tools. Answer in Lithuanian only."},
                    {"role": "user", "content": f"{context}\nKlausimas: {question}"}
                ],
                temperature=1.0,
                top_p=1.0
            )
            print("Atsakymas:\n", response.choices[0].message.content)

        except Exception as e:
            print("Klaida:", str(e))

# Main
def main():
    birzai_text = load_birzai_db()
    token, endpoint, model = load_credentials()
    client = create_client(token, endpoint)
    chat_with_context(client, model, birzai_text)

if __name__ == "__main__":
    main()
