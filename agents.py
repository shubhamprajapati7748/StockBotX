import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables
load_dotenv()

# Initialize Groq Model
groq_api_key = os.getenv("GROQ_API_KEY")
model = Groq(id="llama3-groq-8b-8192-tool-use-preview", api_key=groq_api_key)

# Initialize Tools
duck_duck_go = DuckDuckGo()
yfinance_tools = YFinanceTools(
    stock_price=True,
    analyst_recommendations=True,
    stock_fundamentals=True,
    company_info=True,
    company_news=True
)

# Define Agents
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=model,
    tools=[duck_duck_go],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    model=model,
    tools=[yfinance_tools],
    instructions=["Use table to display data"],
    show_tool_calls=True,
    markdown=True
)

# Create a team of agents
agents = Agent(
    team=[web_search_agent, finance_agent],
    model=model,
    instructions=["Always include sources", "Use table to display data"],
    show_tools_calls=True,
    markdown=True
)