from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal

from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda

load_dotenv()

model1 = ChatGroq(model = "llama-3.3-70b-versatile")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give sentiment of feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of following feedback weither positive or negative\n {feedback}\n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template="Write a appropriate response to this positive feedback {feedback}",
    input_variables=["feedback"]
)
prompt3 = PromptTemplate(
    template="Write a appropriate response to this negitive feedback {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model1 | parser),
    (lambda x:x.sentiment == "negative",prompt3 | model1 | parser),
    RunnableLambda(lambda x : "coult not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":"This is terrible phone"})

print(result)

chain.get_graph().print_ascii()



