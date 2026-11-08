from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

messages = [
    {
        'role': 'system',
        'content': 'You are a Python programming tutor. Provide simple answers suitable for beginners. Include code examples whenever possible.'        
    },
]


def estimate_tokens(text):
    words = len(text.split())
    return 1.3 * words


def count_tokens(messages):
    return sum(estimate_tokens(message['content']) for message in messages)


MAX_TOKEN_BUDGET = 4000



while True:
    user_question = input("Ask me anything: ")

    if user_question =='exit':
        break

    messages.append({
        'role': 'user',
        'content': user_question,
    })

    system_message = messages[0]
    conversation_history = messages[1:]
    recent_messages = conversation_history[-10:]

    if recent_messages and recent_messages[0]['role'] == 'assistant':
        recent_messages = recent_messages[1:]

    context = [system_message] + recent_messages


    while count_tokens(context) > MAX_TOKEN_BUDGET and len(context) > 3:
        context.pop(1)
        context.pop(1)
        total_tokens = count_tokens(context)



    response = client.chat.completions.create(
        model ='openai/gpt-oss-120b',
        messages = context,
    )

    print(response.choices[0].message.content)

    messages.append({
        'role': 'assistant',
        'content': response.choices[0].message.content,
    })