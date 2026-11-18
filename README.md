# Python LLM Chatbot

A command-line AI chatbot built with Python, Groq API, and Hugging Face Transformers.

## Features

- **LLM Integration:** Uses Groq API with the `openai/gpt-oss-120b` model.
- **Streaming Responses:** Displays AI responses incrementally.
- **Conversation History:** Maintains conversation context.
- **Message Summarization:** Summarizes early conversation messages every five iterations.
- **Context Management:** Preserves system instructions while trimming older messages.
- **Token Tracking:** Tracks input, output, and total token usage.
- **Input Limit:** Restricts user prompts to 10 tokens.
- **Usage Limit:** Stops after exceeding 10,000 consumed tokens.

## Technologies

- Python
- Groq API
- OpenAI Python SDK
- Hugging Face Transformers
- python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   cd YOUR_PROJECT_DIRECTORY
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Groq API key:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

5. Run the chatbot:

   ```bash
   python chat_bot.py
   ```

## Usage

- Enter your prompt when requested.
- Each prompt is limited to 10 tokens.
- Type `q` to exit the chatbot.
- A usage report is displayed when the session ends.

## Learning Source

Developed while following tutorials from the NeonLearn YouTube channel.