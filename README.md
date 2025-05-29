# AI Chatbot Flask Application

A modern, responsive web-based AI chatbot built with Flask and powered by Groq's language models. Features a beautiful glassmorphism UI design with real-time chat functionality.

![Chatbot Preview](https://img.shields.io/badge/Flask-Chat%20App-blue?style=for-the-badge&logo=flask)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Groq-orange?style=for-the-badge)

## Features

- 🤖 **AI-Powered Conversations**: Integrates with Groq's Gemma2-9B model via LangChain
- 💬 **Real-time Chat Interface**: Smooth, responsive chat experience
- 🎨 **Modern UI Design**: Beautiful glassmorphism design with gradient backgrounds
- 📱 **Mobile Responsive**: Works perfectly on all devices
- 🔄 **Session Management**: Maintains conversation history during your session
- 🧹 **Clear Chat Function**: Easy way to start fresh conversations
- ⚡ **Fast Response Times**: Optimized for quick AI responses
- 🔒 **Secure**: Proper environment variable handling for API keys

## Screenshots

The application features a modern chat interface with:
- Gradient background with glassmorphism effects
- Animated status indicators
- Auto-scrolling chat messages
- Responsive design for mobile and desktop
- Intuitive send and clear buttons

## Tech Stack

- **Backend**: Flask (Python web framework)
- **AI/ML**: LangChain + Groq API (Gemma2-9B model)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern gradients and animations
- **Environment**: Python-dotenv for configuration management

## Project Structure

```
ai-chatbot-flask/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env                       # Environment variables (create this)
├── .env.example              # Environment template
├── README.md                 # This file
├── templates/
│   └── index.html            # Chat interface template
└── src/
    ├── __init__.py
    ├── utils.py              # Chat model utilities
    └── components/
        ├── __init__.py
        └── chat_bot.py       # Main chatbot class
```

## Prerequisites

- Python 3.11 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com))
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <https://github.com/nubbot77/ChatBot-Application.git>
   cd ai-chatbot-flask
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the required directories and files**
   ```bash
   # Create empty __init__.py files for Python packages
   touch src/__init__.py
   touch src/components/__init__.py
   ```

5. **Set up environment variables**
   ```bash
   # Copy the environment template
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   nano .env  # or use your preferred editor
   ```

6. **Configure your `.env` file**
   ```env
   # Your Groq API Key (required)
   GROQ_API_KEY=your_groq_api_key_here
   
   # Flask Secret Key (optional - app will generate one if not provided)
   FLASK_SECRET_KEY=your_flask_secret_key_here
   ```

## Getting Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy the key and paste it into your `.env` file

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Start chatting**
   - Type your message in the input field
   - Press Enter or click the send button
   - Use "Clear Chat" to start a new conversation

## API Configuration

The chatbot uses the following Groq model configuration:

- **Model**: `gemma2-9b-it`
- **Temperature**: 0.7 (balanced creativity/consistency)
- **Max Tokens**: 512 (moderate response length)

You can modify these settings in `src/utils.py` if needed.

## Customization

### Changing the AI Model
Edit `src/utils.py` and modify the model configuration:
```python
self.chat = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192",  # Change model here
    temperature=0.5,              # Adjust creativity
    max_tokens=1024,              # Adjust response length
)
```

### Customizing the System Prompt
Edit `src/components/chat_bot.py` and modify the system message:
```python
self.system_message = SystemMessage(content="Your custom system prompt here")
```

### Styling Changes
The CSS is embedded in `templates/index.html`. You can modify:
- Colors and gradients
- Font sizes and families
- Animation effects
- Layout and spacing

## Troubleshooting

### Common Issues

**"Chat model not initialized properly"**
- Check your Groq API key in the `.env` file
- Ensure you have an active internet connection
- Verify your Groq account has API access

**"Module not found" errors**
- Make sure you've installed all requirements: `pip install -r requirements.txt`
- Check that `__init__.py` files exist in the `src/` directories
- Verify you're running from the correct directory

**Template not found**
- Ensure the `templates/` directory exists
- Check that `index.html` is in the `templates/` folder
- Verify file permissions

**Sessions not working**
- The app will use a default secret key if none is provided
- For production, always set a secure `FLASK_SECRET_KEY`

### Debug Mode

The application runs in debug mode by default. To disable for production:

```python
# In app.py, change:
app.run(debug=False, host='0.0.0.0', port=5000)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

- [Groq](https://groq.com) for providing fast AI inference
- [LangChain](https://langchain.com) for the AI framework
- [Flask](https://flask.palletsprojects.com) for the web framework
- Modern CSS techniques for the beautiful UI design

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the [Groq documentation](https://console.groq.com/docs)
3. Check [LangChain documentation](https://python.langchain.com/docs/get_started/introduction)
4. Open an issue in this repository

---