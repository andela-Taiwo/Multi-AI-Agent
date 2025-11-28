import streamlit as st
import requests

from app.config.settings import settings
from app.utils.logger import get_logger
from app.utils.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="MULTI-AI AGENT", page_icon=":robot:", layout="centered")
st.title("MULTI-AI AGENT using Groq and Tavily")

sytem_prompt = st.text_area("Define the system prompt for the AI agent", height=70)
selected_model = st.selectbox("Select the AI model to use", settings.ALLOWED_MODEL_LIST)
allow_search = st.checkbox("Allow search", value=True)
user_query = st.text_area("Enter your query: ", height=150)

API_URL = "http://localhost:8000/api/v1/chat"

if st.button("Submit") and user_query.strip():
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "model_name": selected_model,
        "system_prompt": sytem_prompt,
        "messages": [],
        "allow_search": allow_search,
    }
    try:
        logger.info(f"Submitting request to the AI agent: {API_URL}")

        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            agent_response = result.get("response", None)
            if agent_response:
                st.subheader("Agent Response")
                st.markdown(
                    agent_response.replace("\n", "<br>"), unsafe_allow_html=True
                )

        else:
            st.error(f"Error: {response.status_code}")
            st.error(f"Error: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(str(CustomException("Faled to communicate with the AI agent")))
