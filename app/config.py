import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

DEBUG = True

print("=" * 50)
print("API KEY =", GEMINI_API_KEY)
print("=" * 50)