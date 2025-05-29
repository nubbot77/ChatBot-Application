from flask import Flask, request, render_template, redirect, session
import os
from dotenv import load_dotenv
from src.components.chat_bot import ChatBot

load_dotenv()
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here-change-this')

@app.route("/")
def index():
    # Initialize chat history in session if it doesn't exist
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template("index.html", chat_history=session['chat_history'])

@app.route("/chat", methods=['POST'])
def chat():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input and user_input.strip():
            # Initialize chat history in session if it doesn't exist
            if 'chat_history' not in session:
                session['chat_history'] = []
            
            # Get response from chatbot
            chat_bot = ChatBot()
            response = chat_bot.ask(user_input)  # Fixed method name
            
            # Add user message and bot response to chat history
            session['chat_history'].append({'type': 'user', 'message': user_input})
            session['chat_history'].append({'type': 'bot', 'message': response})
            session.modified = True
            
            return render_template("index.html", chat_history=session['chat_history'])
    
    return redirect("/")

@app.route("/clear", methods=['POST'])
def clear_chat():
    # Clear chat history
    session['chat_history'] = []
    session.modified = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)  # Run the app on all interfaces