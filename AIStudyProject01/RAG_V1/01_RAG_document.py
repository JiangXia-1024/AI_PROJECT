from langchain_community.document_loaders import WebBaseLoader,Docx2txtLoader
import bs4
# from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

'''
文档加载
'''
# 1、文档加载器：网页
# web_path = "https://www.toutiao.com/article/7636038308010689064/?log_from=ca798e84665c_1777951693221"

# loader = WebBaseLoader(
#     web_paths = [web_path],
#     bs_kwargs = dict(parse_only = bs4.SoupStrainer(class_ = "comment-list"))
#     )

# docs = loader
# print("输出内容")
# print(docs)
# print('-'*100)
# exit

#2、文档加载器：txt
# txt_path = "01_RAG_document.txt"
# loader = TextLoader(txt_path)
# docs = loader.load()
# print("输出内容")
# print(docs)
# print('-'*100)
# exit

# 3、文档加载器：docx
docx_path = "01_RAG_document.docx"
loader = Docx2txtLoader(docx_path)
docs = loader.load()
print("输出内容")
print(docs)
print('-'*100)
exit

# 4、文档加载器：pdf
pdf_path = "01_RAG_document.pdf"
loader = PdfLoader(pdf_path)
docs = loader.load()
print("输出内容")
print(docs)
print('-'*100)
exit  

# 5、文档切分
# 5.1、RecursiveCharacterTextSplitter：基于字符的递归切分器，会根据字符长度和重叠长度进行切分，直到每个切分块的长度小于等于指定的字符长度
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100,
    separators = ["\n\n", "\n", " ", ""],
)
docs = text_splitter.split_documents(docs)
print("输出内容")
print(docs)
print('-'*100)
exit

# 5.2、文本按分隔符简单分割
from langchain_text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100,
    separators = ["\n\n", "\n", " ", ""],
)
docs = text_splitter.split_documents(docs)
print("输出内容")
print(docs)
print('-'*100)
exit

#5.3 MarkdownTextSplitter：基于Markdown的切分器，会根据Markdown的分隔符进行切分
from langchain_text_splitter import MarkdownHeaderTextSplitter
text_splitter = MarkdownHeaderTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100,
    separators = ["\n\n", "\n", " ", ""],
)
docs = text_splitter.split_documents(docs)
print("输出内容")
print(docs)
print('-'*100)
exit