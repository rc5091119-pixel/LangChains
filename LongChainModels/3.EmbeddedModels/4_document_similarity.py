from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    dimensions=300 
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about virat kohli'

doc_embedding = embeddings.embed_documents(documents)
que_embedding = embeddings.embed_query(query)


result = cosine_similarity([que_embedding],doc_embedding)[0] # both should be 2 d vector
index , score = sorted(list(enumerate(result)),key=lambda x:x[1])[-1]


print(query)
print(documents[index])
print("similarity score is: ",score)
