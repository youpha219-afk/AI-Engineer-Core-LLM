
import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def chatbot_response(user_message):
    response = client.responses.create(
        model="gpt-5.5",
        input=user_message
    )

    return response.output_text


def main():
    print("Welcome to the LLM Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "bye":
            print("Bot: Goodbye!")
            break

        try:
            response = chatbot_response(user_message)
            print("Bot:", response)

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
