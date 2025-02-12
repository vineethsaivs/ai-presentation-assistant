import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not SERPER_API_KEY or not GROQ_API_KEY:
    raise Exception("API keys missing. Please set them in the .env file.")

print("API Keys Loaded Successfully.")
