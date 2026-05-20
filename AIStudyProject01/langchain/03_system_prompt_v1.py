import os
from typing import TypedDict
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 初始化通义千问模型
qwen = ChatTongyi(
    model="qwen-plus",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    temperature=0.7
)

# 1、系统提示词 system prompt
system_prompt = "你是一个智能助手，回答问题要简洁明了。"
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    ("user", "{input}")
])
chain_v1 = prompt | qwen | StrOutputParser()

# 测试基础系统提示词
response_v1 = chain_v1.invoke({"input": "你是谁？"})
print("基础系统提示词:")
print(response_v1)
print("=" * 50)

#-----------------------------------------------------------------#
'''
动态系统提示词
    对于需要根据运行时上下文或agent状态修改系统提示符的更高级用例
    可以通过在调用时动态构建提示词来实现
'''

#2、自定义context格式
class Context(TypedDict):
    user_role: str

def get_system_prompt(context: Context) -> str:
    """根据用户角色来生成系统提示词"""
    user_role = context.get("user_role", "user")
    base_prompt = f"你是一个{user_role}，回答问题要简洁明了。"
    
    if user_role == "专家助手":
        return f"{base_prompt}提供详细的技术回应。"
    elif user_role == "智能助手":
        return f"{base_prompt}提供一般信息，简单地解释概念，避免行话。"

    return base_prompt

# 动态构建提示词的函数
def create_dynamic_chain(user_role: str):
    system_prompt = get_system_prompt({"user_role": user_role})
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        ("user", "{input}")
    ])
    return prompt | qwen | StrOutputParser()

# 测试动态系统提示词
chain_v2 = create_dynamic_chain("专家助手")
response_v2 = chain_v2.invoke({"input": "你是谁？"})
print("\n动态系统提示词(专家助手):")
print(response_v2)
print("=" * 50)

# 测试另一个角色
chain_v3 = create_dynamic_chain("智能助手")
response_v3 = chain_v3.invoke({"input": "你是谁？"})
print("\n动态系统提示词(智能助手):")
print(response_v3)
