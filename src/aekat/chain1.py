from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

# 1. Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful technical writer."),
    ("human", "Explain {topic} in three sentences.") ])

# 2. Initialize the model
model = ChatOpenAI(model="gpt-4o", temperature=0)

# 3. Compose with LCEL pipe operator
chain = prompt | model | StrOutputParser()

# 4. Run the chain
result = chain.invoke({"topic": "vector databases"})
print(result)