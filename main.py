from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

user_question = input("Ask me anything: ")

response = client.chat.completions.create(
    model ='openai/gpt-oss-120b',
    messages = [
        {
            'role': 'user',
            'content': user_question,
        }
    ]
)

print(response.choices[0].message.content)