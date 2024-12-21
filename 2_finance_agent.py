from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.huggingface import HuggingFaceChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-specdec"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)
finance_agent = Agent(
    name="Finance Agent",
    role="Get Financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=['Use tables the display data.'],
)
agent_team=Agent(
    team=[web_agent,finance_agent],
    instructions=["Always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)
agent_team.print_response("Summarize  analyst recommendations and share the latest news for NVDA", stream=True)