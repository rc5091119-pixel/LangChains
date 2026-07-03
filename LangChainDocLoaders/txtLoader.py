from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template='Write a summary on poem {poem}',
    input_variables=['poem']
)
loader = TextLoader(file_path="cricket.txt", encoding="utf8")

docs = loader.load()
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})
print(result)   

chain.get_graph().print_ascii()
