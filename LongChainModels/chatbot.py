from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature = 0)

chat_history = [SystemMessage(content="You are helpful assistant")]


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = chatModel.invoke(chat_history)
    print("AI: ",result.content)
    chat_history.append(AIMessage(content=result.content))
   

print(chat_history)