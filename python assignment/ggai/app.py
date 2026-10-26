
from google import genai

from settings import GEMINI_API_KEY


genai.api_key = GEMINI_API_KEY

def generate_response(prompt):
    client = genai.Client()
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=prompt
    )
    return interaction.output_text


def main():

    print("="*20)
    print("Welcome to the Gemini AI Chatbot!")
    print("="*20)

    while True:
        prompt = input("chatbot: ")

        response = generate_response(prompt)
        print(f"chatbot: {response}")


        choice = input("Do you want to continue chatting? (y/n): ").lower()

        if choice == "no" or choice == "n":
            print("Thank you for chatting with Gemini AI. Goodbye!")
            break

if __name__ == "__main__":
    main()       