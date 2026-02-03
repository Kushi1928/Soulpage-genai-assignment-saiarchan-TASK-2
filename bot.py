from langchain_google_genai import ChatGoogleGenerativeAI
from tools import web_search
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def chat_with_bot(user_input: str, chat_history: str) -> str:
    search_result = web_search(user_input)

    prompt = f"""
You are a conversational knowledge bot.
You remember previous conversation context.

Conversation so far:
{chat_history}

Relevant web information:
{search_result}

User question:
{user_input}

Give a clear, factual, and contextual answer.
"""

    response = llm.invoke(prompt)
    return response.content
