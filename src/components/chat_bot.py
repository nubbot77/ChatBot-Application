from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from src.utils import ChatModel

class ChatBot:
    def __init__(self):
        try:
            self.model = ChatModel()
            self.chat_history = []
            self.system_message = SystemMessage(content="You are a helpful AI assistant. Answer the questions to the best of your abilities. Don't give wrong information. If you don't know the answer, say you don't know.")
            self.chat_history.append(self.system_message)
        except Exception as e:
            print(f"An error occurred while initializing the chat model: {e}")
            self.model = None
            self.chat_history = []

    def ask(self, query: str):
        try:
            if not self.model or not self.chat_history:
                return "Chat model not initialized properly."
            self.chat_history.append(HumanMessage(content=query))
            response = self.model.retrive(self.chat_history)
            self.chat_history.append(AIMessage(content=response))
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I encountered an error processing your request."

# if __name__ == "__main__":
#     chat_bot = ChatBot()
#     response = chat_bot.ask("What is the capital of France?")
#     print(response)  # Should print the response from the chat model