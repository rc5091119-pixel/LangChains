from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader

loader = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
) 

locs = loader.load()

print(len(locs))
