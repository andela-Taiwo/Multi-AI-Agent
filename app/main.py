import subprocess
import threading
import time
from app.utils.logger import get_logger
from app.utils.custom_exception import CustomException

logger = get_logger(__name__)


def start_server():
    try:
        logger.info("Starting server...")
        subprocess.run(
            ["uvicorn", "app.api.api:app", "--host", "127.0.0.1", "--port", "8000"]
        )
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        raise CustomException(f"Error starting server: {e}")


def start_frontend():
    try:
        logger.info("Starting frontend...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"])
    except Exception as e:
        logger.error(f"Error starting frontend: {e}")
        raise CustomException(f"Error starting frontend: {e}")


if __name__ == "__main__":
    try:
        threading.Thread(target=start_server).start()
        time.sleep(2)
        start_frontend()
    except Exception as e:
        raise CustomException(f"Error starting the application: str{e}")
