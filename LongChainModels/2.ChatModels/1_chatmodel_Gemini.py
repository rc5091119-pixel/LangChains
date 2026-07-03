from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature = 0)

result = chatModel.invoke("What is capital of India")
print(result.content)