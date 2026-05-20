from langchain_community.embeddings import DashScopeEmbeddings
import os

#1、初始化embeddings
embeddings = DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
)

#2、使用嵌入模型
query = "你好"
embedding = embeddings.embed_query(query)
print("输出内容")
print(embedding)
print('-'*100)
exit
