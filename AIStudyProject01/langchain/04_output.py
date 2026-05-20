# ✅ 新的导入方式
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import ChatPromptTemplate


# 1、构建提示词
prompt = CommaSeparatedListOutputParser([
    ("system","把用户输入的中文翻译成{language}"),
    ("user", "{input}"),
])

prompt = prompt.format(language="英文",input="你是谁？")

qwen = ChatOpenAI(
    model_name="qwen2.5-72b-instruct",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2、 访问大模型
result = qwen.invoke(prompt)
print(result)
print('-'*100)

# 使用输出解析器 str output parser
parser = StrOutputParser()
str_result = parser.invoke(result)
print(str_result)
