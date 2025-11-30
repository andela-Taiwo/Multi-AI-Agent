# Multi-AI Agent

A multi-agent system for AI-powered decision-making using Groq LLM and Tavily web search capabilities. This project provides a FastAPI backend with a Streamlit frontend interface for interacting with AI agents that can optionally perform web searches to enhance their responses.

## Features

- 🤖 **AI Agent System**: Powered by LangChain and LangGraph for intelligent agent orchestration
- 🔍 **Web Search Integration**: Optional Tavily search integration for real-time information retrieval
- 🚀 **FastAPI Backend**: RESTful API for chat interactions with AI agents
- 🎨 **Streamlit Frontend**: User-friendly web interface for interacting with the AI agent
- 🔧 **Configurable Models**: Support for multiple LLM models (currently Groq's Llama 3.3 70B)
- 📝 **System Prompts**: Customizable system prompts for agent behavior
- 🐳 **Docker Support**: Containerized deployment ready

## Prerequisites

- Python 3.13 or higher
- Groq API key ([Get one here](https://console.groq.com/))
- Tavily API key ([Get one here](https://tavily.com/))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd multi-ai-agent
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```
   
   Or using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## Usage

### Running the Application

The application consists of two components that run simultaneously:
- **Backend API**: FastAPI server on `http://127.0.0.1:8000`
- **Frontend UI**: Streamlit app (typically on `http://localhost:8501`)

**Start both services:**
```bash
python app/main.py
```

This will automatically start both the backend API and the Streamlit frontend.

### Running Components Separately

**Backend only:**
```bash
uvicorn app.api.api:app --host 127.0.0.1 --port 8000
```

**Frontend only:**
```bash
streamlit run app/frontend/ui.py
```

## API Documentation

Once the backend is running, you can access:
- **Interactive API docs**: `http://127.0.0.1:8000/docs`
- **Alternative docs**: `http://127.0.0.1:8000/redoc`

### Chat Endpoint

**POST** `/api/v1/chat`

Request body:
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a helpful AI assistant.",
  "messages": ["Your question here"],
  "allow_search": true
}
```

Response:
```json
{
  "response": "AI agent's response text"
}
```

## Project Structure

```
multi-ai-agent/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── api.py              # FastAPI routes
│   ├── core/
│   │   ├── __init__.py
│   │   └── ai_agent.py         # AI agent implementation
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py         # Configuration settings
│   ├── frontend/
│   │   └── ui.py               # Streamlit UI
│   └── utils/
│       ├── __init__.py
│       ├── logger.py           # Logging utilities
│       └── custom_exception.py # Custom exceptions
├── logs/                       # Application logs
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── pyproject.toml              # Project metadata
└── README.md                   # This file
```

## Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t multi-ai-agent .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 -p 8501:8501 --env-file .env multi-ai-agent
   ```

   Make sure your `.env` file contains the required API keys.

## Configuration

The application configuration is managed in `app/config/settings.py`. Key settings include:

- `ALLOWED_MODEL_LIST`: List of supported LLM models
- `GROQ_API_KEY`: Groq API key (from environment)
- `TAVILY_API_KEY`: Tavily API key (from environment)

## Development

### Code Quality

This project uses `ruff` for code linting and formatting. Install dev dependencies:

```bash
pip install -e ".[dev]"
```

Run linting:
```bash
ruff check .
```

## Logging

Application logs are stored in the `logs/` directory with daily rotation. Log files follow the pattern: `log_YYYY-MM-DD.log`.

## License

[Add your license here]

## Author

**Taiwo Sokunbi**
- Email: sokunbitaiwo82@gmail.com
- GitHub: [andela-Taiwo](https://github.com/andela-Taiwo)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

