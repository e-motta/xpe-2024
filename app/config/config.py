import os
from dotenv import load_dotenv

load_dotenv()

# App
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")

# Database
MONGODB_URI = (
    os.getenv("MONGODB_URI_DEV")
    if FLASK_ENV == "development"
    else os.getenv("MONGODB_URI_PROD")
)

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompts
INITIAL_PROMPT: str = os.getenv(
    "INITIAL_PROMPT",
    default="Você é um especialista em finanças pessoais. Eu não tenho conhecimento em finanças.",
)
MESSAGES_LIMIT: int = int(os.getenv("MESSAGES_LIMIT", default=10))
ANSWER_SENTENCE_LIMIT: int = int(os.getenv("ANSWER_SENTENCE_LIMIT", default=2))
