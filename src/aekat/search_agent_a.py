from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

# Initialize the GPT-4o mini model with a factual temperature (0.0)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0
)

# Tavily as the web search tool
# max_results=3 limits the context size to keep input token costs very low
search_tool = TavilySearch(
    max_results=3
)
tools = [search_tool]

# Create the agent using LangGraph's prebuilt ReAct agent executor
agent_executor = create_react_agent(llm, tools)

# Run a low-volume web search query
query = "What were the major tech updates announced this week?"
print(f"Sending query: '{query}'...\n")

response = agent_executor.invoke({"messages": [("user", query)]})

# Print the final answer from the assistant
final_answer = response["messages"][-1].content
print("Answer:")
print(final_answer)