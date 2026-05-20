

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
import os

'''
在langchain中，消息是通过message对象来表示的，每个message对象都有一个content属性，用于存储消息的内容
消息包含以下内容的对象：
    角色：标识消息类型（system、user、assistant）
    内容：消息的具体内容（文本、图像、音频、文档等）
    元数据：可选字段，例如响应消息、消息id和令牌的使用情况
langchain提供了一种适用于所有模型提供程序的标准消息类型，确保无论调用哪个模型，行为都保持一致
'''

'''
messages = [
    SystemMessage(content="你是一个诗歌专家"),
    HumanMessage(content="请写一篇关于春天的七言绝句"),
    AIMessage(content="桃花盛开...."),
]
'''

# 字典格式
'''
messages=[
    {"role": "system", "content": "你是一个诗歌专家"},
    {"role": "user", "content": "请写一篇关于春天的七言绝句"},
    {"role": "assistant", "content": "桃花盛开...."}
]
'''

# 消息元数据
messages = [
    HumanMessage(
        content="Hello!",
        name = 'alice', # 可选：用来区别不同的用户
        id="msg_123456",# 可选：用来区别不同的消息 跟踪的唯一标识符
    )
]

# 聊天模型调用
qwen = ChatOpenAI(
    model_name="qwen2.5-72b-instruct",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = qwen.invoke(messages)
print(response.content)