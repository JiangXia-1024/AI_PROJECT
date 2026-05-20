import chromadb
from langchain_community.embeddings import DashScopeEmbeddings
import os

# 嵌入模型
embaddings = DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
)

# 评分方式
score_measures = [
    "default", # 默认使用l2
    "cosine",
    "ip", # 点积相似度
    "euclidean",
    "manhattan",
    "l1",
    "l2",  # 欧式距离
    "pearson",
    "spearman",
    "kendall",
    "pearsonr",
    "spearmanr",
    "kendallr",
    "pearsonr",
    "spearmanr",
    "kendallr",
    "pearsonr",
    "spearmanr",
    "kendallr",
]

# 初始化Chroma数据库
client = chromadb.Client()
collection = client.create_collection(collection_name="rag_collection", embedding_function=embaddings, collection_metadata={"hnsw:space": "l2"}, persist_directory="./chromadb_db1")

# 提供文档
documents = [
    Document(page_content="这个手机苹果很好用"),
    Document(page_content="我国山东地区盛产苹果")
]

# 插入文档
collection.add_documents(documents)
print("输出内容")
print(collection)
print('-'*100)

# 检索
result = collection.similarity_search_with_score(query="我想买苹果手机")
for doc,score in result:
    print(doc.page_content,end="\t")
    print(f"score:{score}")

