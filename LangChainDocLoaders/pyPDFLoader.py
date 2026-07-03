from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("dl-curriculum.pdf")

model = ChatGroq(model="llama-3.3-70b-versatile")
 
docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)