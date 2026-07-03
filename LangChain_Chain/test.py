from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model2 = ChatGroq(model = "llama-3.3-70b-versatile")

result = model2.invoke("What is capital of Rajasthan")

print(result.content)