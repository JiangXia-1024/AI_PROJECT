from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os



qwen = ChatOpenAI(
    model_name="qwen2.5-72b-instruct",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

'''
chatPromptTemplate : 提供角色设置：
    system:系统角色
    user：用户角色
    assistant：大模型回复
'''
prompt = ChatPromptTemplate([
    ("system", "你是一个智能助手，回答问题要简洁明了。"),
    ("human", "{input}")
])

prompt = prompt.format(input="你是 LangChain 的作者吗？")
print(prompt)

response = qwen.invoke(prompt)
print(response.content)
