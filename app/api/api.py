from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import AIAgent
from app.utils.logger import get_logger
from app.utils.custom_exception import CustomException
from app.config.settings import settings

logger = get_logger(__name__)
agent = AIAgent()
agent_response = agent.get_response_from_ai_agent
app = FastAPI(
    title="MULTI-AI AGENT",
    version="0.1.0",
    description="A multi-agent system for AI-powered decision-making",
)


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.post("/api/v1/chat")
async def chat_endpoint(request_state: RequestState):
    try:
        if request_state.model_name not in settings.ALLOWED_MODEL_LIST:
            logger.error(f"Invalid model name: {request_state.model_name}")
            raise HTTPException(status_code=400, detail="Invalid model name")
        if not request_state.system_prompt:
            logger.error("System prompt is required")
            raise HTTPException(status_code=400, detail="System prompt is required")
        if not request_state.messages:
            logger.error("Messages are required")
            raise HTTPException(status_code=400, detail="Messages are required")

        response = agent_response(
            request_state.model_name,
            request_state.allow_search,
            request_state.messages,
            request_state.system_prompt,
        )
        logger.info(f"Received response from AI agent: {request_state.model_name}")
        return {"response": response}
    except CustomException as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))
