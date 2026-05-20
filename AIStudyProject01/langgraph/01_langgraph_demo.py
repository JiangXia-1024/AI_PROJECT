from langgraph import LangGraph
from langchain_community.llms import DashScopeLLM

agent = create_react_agent(
    model = llm,
    tools=[get_current_weather],
    prompt = "you are a helpful assistant."
)

agent.invoke({"message":[{"role":"user","content":"你是谁，能帮我解决什么问题"}]})
