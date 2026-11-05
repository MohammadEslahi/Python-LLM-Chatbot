# Python LLM Chatbot

A simple conversational AI chatbot built with Python and the Groq API, powered by OpenAI GPT-OSS 120B.

## Features

- Integration with Groq API
- Multi-turn conversations
- In-memory conversation history
- System prompt customization
- Beginner-friendly Python programming assistant
- Exit command to end the conversation

## Tech Stack

- Python
- Groq API
- OpenAI GPT-OSS 120B
- python-dotenv

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Install dependencies:

```bash
pip install groq python-dotenv
```

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
python main.py
```

## Usage

Start asking questions in the terminal.

Type `exit` to end the conversation.

## How It Works

The chatbot maintains conversation history using a Python list.

Previous user messages and assistant responses are sent to the LLM with each new request, allowing the model to understand conversational context.

Conversation history is stored in memory and is lost when the application terminates.

## Future Improvements

- Context window management
- Streaming responses
- Prompt engineering
- Tool calling
- RAG integration
- Persistent conversation storage

## Author

Mohammad Eslahi

