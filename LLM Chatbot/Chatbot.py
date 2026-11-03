
# Simple LLM Chatbot Project
# A beginner-friendly conversational chatbot

def chatbot_response(user_message):
    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"

    elif "how are you" in message:
        return "I'm doing well! Thanks for asking."

    elif "your name" in message:
        return "I'm a simple chatbot built with Python."

    elif "ai" in message:
        return "AI is an exciting field. Let's explore it together!"

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return "That's interesting! Tell me more."


def main():
    print("Welcome to the Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("\nYou: ")

        response = chatbot_response(user_message)

        print("Bot:", response)

        if "bye" in user_message.lower():
            break


if __name__ == "__main__":
    main()
