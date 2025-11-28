from langchain_groq import ChatGroq
from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage
from app.config.settings import settings
from app.utils.logger import get_logger
from app.utils.custom_exception import CustomException

logger = get_logger(__name__)


class AIAgent:
    def __init__(self):
        self.groq_client = ChatGroq(api_key=settings.GROQ_API_KEY)
        self.tavily_client = TavilySearchResults(api_key=settings.TAVILY_API_KEY)
        self.model = settings.ALLOWED_MODEL_LIST[0]
        self.tools = [TavilySearchResults()]
        self.agent = create_react_agent(self.groq_client, self.model, self.tools)

    def run(self, prompt: str):
        return self.agent.invoke({"input": prompt})

    def get_response_from_ai_agent(
        self, llm_model: str, allow_search: bool, user_query: str, prompt: str
    ):
        try:
            if allow_search:
                tools = [TavilySearchResults()]
            else:
                tools = []
            llm_client = ChatGroq(api_key=settings.GROQ_API_KEY, model=llm_model)
            agent = create_react_agent(llm_client, tools, state_modifier=prompt)
            state = {"messages": user_query}
            response = agent.invoke(state)
            messages = response.get("messages")
            ai_message = [msg for msg in messages if isinstance(msg, AIMessage)]
            if ai_message:
                return ai_message[-1].content
            else:
                return "No response from the agent"
        except Exception as e:
            logger.error(f"Error in get_response: {e}")
            raise CustomException(f"Error in get_response: {e}")
