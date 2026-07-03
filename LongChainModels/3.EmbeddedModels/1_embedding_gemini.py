from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Use gemini-embedding-001 (stable) or gemini-embedding-2 (newer)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

result = embeddings.embed_query(
    "Delhi is capital of India"
)

print(str(result))