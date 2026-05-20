# 使用 LangChain 调用通义千问大模型

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# 设置通义千问 API 密钥
# 你需要从阿里云获取 API 密钥并设置为环境变量
# 或者直接在这里设置：
# os.environ["DASHSCOPE_API_KEY"] = "your_api_key_here"

# 方法 1: 基本使用
print("=== 方法 1: 基本使用 ===")
chat_model = ChatTongyi(
    model="qwen2.5-72b-instruct",  # 模型名称
    temperature=0.7,  # 温度参数，控制输出的随机性
    top_p=0.9,  # 控制采样范围
)

# 发送消息
messages = [
    SystemMessage(content="你是一个智能助手，回答问题要简洁明了。"),
    HumanMessage(content="什么是 LangChain？")
]

response = chat_model.invoke(messages)
print("回答:", response.content)
print()

# 方法 2: 使用 PromptTemplate
# print("=== 方法 2: 使用 PromptTemplate ===")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是一个专业的{subject}专家，回答要详细专业。"),
#     ("human", "请解释{topic}")
# ])

# # 组合模型和输出解析器
# chain = prompt | chat_model | StrOutputParser()

# # 调用链
# result = chain.invoke({
#     "subject": "人工智能",
#     "topic": "大语言模型的工作原理"
# })
# print("回答:", result)
# print()

# # 方法 3: 流式输出
# print("=== 方法 3: 流式输出 ===")
# def stream_response():
#     messages = [
#         HumanMessage(content="请详细解释 LangChain 的主要组件和用途。")
#     ]
    
#     print("流式回答:")
#     for chunk in chat_model.stream(messages):
#         print(chunk.content, end="", flush=True)
#     print()

# stream_response()

# print("\n=== 模型信息 ===")
# print(f"模型名称: {chat_model.model_name}")
# print(f"支持的模型: 通义千问系列 (qwen2.5-72b-instruct, qwen2.5-32b-instruct 等)")
# print("\n注意：使用前请确保已设置 DASHSCOPE_API_KEY 环境变量")
