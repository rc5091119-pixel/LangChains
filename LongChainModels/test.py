from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Create client directly - it automatically picks up GOOGLE_API_KEY from env
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
print("Available embedding models:")
for model in client.models.list():
    if "embed" in model.name.lower():
        print(f"✓ {model.name}")