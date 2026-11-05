from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

messages = [
    {
        'role': 'system',
        'content': 'You are a Python programming tutor. Provide simple answers suitable for beginners. Include code examples whenever possible.'        },
]


while True:
    user_question = input("Ask me anything: ")

    if user_question =='exit':
        break

    messages.append({
        'role': 'user',
        'content': user_question,
    })

    response = client.chat.completions.create(
        model ='openai/gpt-oss-120b',
        messages = messages,
        # stream = True
    )

    print(response.choices[0].message.content)

    messages.append({
        'role': 'assistant',
        'content': response.choices[0].message.content,
    })