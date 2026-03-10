import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def build_llm(temperature: float = 0.2) -> ChatOpenAI:
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY"),
    )
