'''
langchain 访问大语言模型
'''
import os
import sys
import datetime
from langchain_community.chat_models import ChatTongyi
from langchain.agents import create_agent
from langchain.tools import tool

# 设置标准输出编码为 UTF-8
sys.stdout.reconfigure(encoding='utf-8')

llm = ChatTongyi(
    model="qwen-plus",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
)

print(llm.invoke("你是谁？"))
print(llm.invoke("上海有哪些著名景点？"))

@tool
def get_current_date(location: str = "") -> str:
    """
    获取当前日期
    
    Args:
        location: 查询的地点（可选）
    """
    return f"当前日期是{datetime.datetime.now().strftime('%Y-%m-%d')}"

agent = create_agent(
    model=llm,
    tools=[get_current_date],
    system_prompt="you are a helpful assistant."
)

print(agent.invoke({"messages": [{"role": "user", "content": "你是谁，能帮我解决什么问题"}]}))
print(agent.invoke({"messages": [{"role": "user", "content": "今天的日期是？"}]}))
