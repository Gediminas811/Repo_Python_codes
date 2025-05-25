import os  # Accessing environment variables
from openai import OpenAI  # OpenAI client for API interaction
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load API credentials and configuration
def load_credentials():
    load_dotenv()  # Load environment variables from .env file 
    token = os.getenv("SECRET")  # Retrieve the API key 
    endpoint = "https://models.github.ai/inference"  # API endpoint URL
    model = "openai/gpt-4.1-nano"  # Model to be used
    return token, endpoint, model  # Return the credentials and configuration

# Create and return an OpenAI API client
def create_client(api_key, base_url):
    return OpenAI(
        base_url=base_url,  # Set the base URL for the API
        api_key=api_key,    # Set the API key for authentication
    )

# Send a user question to the model and return the response
def ask_question(client, model, user_input):
    response = client.chat.completions.create(
        model=model,  # Specify which model to use
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
        temperature=1.0,  # Controls randomness of output (higher = more creative)
        top_p=1.0,        # Controls nucleus (top_p) sampling - how model chooses words when generating text
    )
    return response.choices[0].message.content  # Returns AI assistant reply text

# Chat loop until "exit" is chosen by the user
def chat_loop(client, model):
    print("Hello! Ask your question in any language and you'll receive an answer in Lithuanian. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ").strip()  # Gets user input and removes extra whitespace
            if user_input.lower() in ["exit", "quit"]:  # Checks if user inputs "exit"
                print("Iki!")  
                break  
            reply = ask_question(client, model, user_input)  
            print(reply)  
        except Exception as e:
            print("Klaida:", str(e))  

# Main function to run the chatbot
def main():
    token, endpoint, model = load_credentials()  # Load API token, endpoint, and model name
    client = create_client(token, endpoint)  # Create OpenAI client using credentials
    chat_loop(client, model)  # Start chat loop

# Only run the app if this script is executed directly
if __name__ == "__main__":
    main()  # Start the chatbot app
    