from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Review (TypedDict):
    Key_themes: Annotated[list[str],"write down all the key themes discuss in review"]
    summary: Annotated[str,"A brief summary of review"] # tell implecitly
    sentiment: str
    pros:Annotated[Optional[list[str]],"Write down all the pros of review"]
    cons:Annotated[Optional[list[str]],"Write down all the cons of review"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also, the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

print(result)