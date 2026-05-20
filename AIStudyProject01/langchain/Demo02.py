import os

from langchain.chat_models import init_chat_model
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 方式一、chattongyi
# client = ChatTongyi(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     model="qwen2.5-72b-instruct"
# )

# messages = [
#     SystemMessage(content="你是一个智能助手，回答问题要简洁明了。"),
#     HumanMessage(content="什么是 LangChain？")
# ]

# response = client.invoke("你是谁？")
# print(response.content)




# 方式二、创建模型对象，基于openai
'''
chat_model = ChatOpenAI(
    model_name="qwen2.5-72b-instruct",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = chat_model.invoke("你是谁？")
print(response.content)
'''

# 方式三、init_chat_model:对于不兼容openai的模型，可以使用
# 参数1：model 模型名称
# 参数2：model_privider 模型提供者
client = init_chat_model(
    model="openai",
    model_provider="langchain-openai",
)
messages = [
    SystemMessage(content="你是一个智能助手，回答问题要简洁明了。"),
    HumanMessage(content="你是谁？")
]
response = client.invoke(messages)
print(response.content)
