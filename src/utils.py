from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
import os

load_dotenv()


class ChatModel:
    def __init__(self):
        try:
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")
            self.chat = ChatGroq(
                groq_api_key=api_key,
                model_name="gemma2-9b-it",
                temperature=0.7,
                max_tokens=512,

            )
        except Exception as e:
            print(f"An error occurred while initializing the chat model: {e}")
            self.chat = None

    def retrive(self, messages: list):
        try:
            if not self.chat:
                return "Chat model not initialized properly."
            response = self.chat.invoke(messages)
            return response.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I encountered an error processing your request."