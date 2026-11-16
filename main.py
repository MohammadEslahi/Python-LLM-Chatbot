from groq import Groq
from dotenv import load_dotenv
import os


# Configuration
MODEL_NAME = 'openai/gpt-oss-120b'
MAX_HISTORY_MESSAGES = 10

SYSTEM_MESSAGE = {
    'role': 'system',
    'content': (
        'You are a Python programming tutor. '
        'Provide simple answers suitable for beginners. '
        'Include code examples whenever possible. '
        'Give only one sentence answers.'
    )
}


# Conversation management
def add_message(messages, role, content):
    messages.append({
        'role': role,
        'content': content
    })


def trim_history(messages):
    return messages[-MAX_HISTORY_MESSAGES:]


def build_context(system_message, messages):
    return [system_message] + messages


# AI communication
def get_ai_response(client, context):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=context
        )

        return response.choices[0].message.content

    except Exception as error:
        print(f'An error occurred: {error}')
        return None


# Main application
def run_chatbot(client):
    recent_messages = []

    while True:
        user_question = input("Ask me anything: ")

        if user_question == 'exit':
            print("Goodbye!")
            break

        add_message(recent_messages, 'user', user_question)

        recent_messages = trim_history(recent_messages)

        context = build_context(SYSTEM_MESSAGE, recent_messages)

        assistant_response = get_ai_response(client, context)

        if assistant_response is None:
            continue

        print(assistant_response)

        add_message(recent_messages, 'assistant', assistant_response)

        recent_messages = trim_history(recent_messages)


def main():
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("Error: GROQ_API_KEY was not found.")
        return

    client = Groq(api_key=api_key)

    run_chatbot(client)


if __name__ == "__main__":
    main()
