from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    PROJECT_NAME: str = "MULTI-AI AGENT"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "A multi-agent system for AI-powered decision-making"
    PROJECT_AUTHOR: str = "Taiwo Sokunbi"
    PROJECT_AUTHOR_EMAIL: str = "taiwo.sokunbi@gmail.com"
    PROJECT_AUTHOR_URL: str = "https://github.com/taiwo-sokunbi"
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_LIST: list[str] = ["llama-3.3-70b-versatile"]


settings = Settings()
