import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN_TG_BOT")
AI_KEY = os.getenv("AI_API_KEY")

if not TOKEN:
    raise ValueError("TOKEN_TG_BOT variable is missing inside your .env file!")
if not AI_KEY:
    raise ValueError("AI_API_KEY variable is missing inside your .env file!")