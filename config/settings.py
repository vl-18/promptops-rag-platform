import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    # LLM
    MODEL_NAME = "gpt-4o-mini"

    # Embeddings
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # RAG settings
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100
    TOP_K_RETRIEVAL = 3

    # Data path (UPDATED)
    DATA_PATH = "data"

    DEMO_MODE = True

    # API keys
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()