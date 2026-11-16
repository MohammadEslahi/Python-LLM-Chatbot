
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_message = {
    'role': 'system',
    'content': 'You are a Python programming tutor. Provide simple answers suitable for beginners. Include code examples whenever possible. Give only one sentence answers.'
}

recent_messages = []

while True:
    user_question = input("Ask me anything: ")

    if user_question == 'exit':
        break

    recent_messages.append({
        'role': 'user',
        'content': user_question
    })

    # Keep only the 10 most recent messages
    recent_messages = recent_messages[-10:]

    # Build context
    context = [system_message] + recent_messages

    # Send request to Groq
    response = client.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=context
    )

    assistant_response = response.choices[0].message.content

    print(assistant_response)

    # Save assistant response
    recent_messages.append({
        'role': 'assistant',
        'content': assistant_response
    })
