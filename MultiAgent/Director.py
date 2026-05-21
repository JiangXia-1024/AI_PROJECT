from typing import TypedDict, Annotated
from operator import add
from langchain_core.messages import AnyMessage,HumanMessage
from langchain_community.chat_models import ChatTongyi

from langgraph.graph import StateGraph, START, END
from langgraph.config import get_stream_writer
from langgraph.checkpoint.memory import InMemorySaver

import os

# 预设一些node的名字，方便后续使用
nodes = ["supervisor","travel","joke","couplet","other"]

llm = ChatTongyi(
    model = "qwen-plus",
    api_key = os.getenv("DASHSCOPE_API_KEY")
)

class State(TypedDict):
    messages: Annotated[list[AnyMessage],add]
    type: str

def supervisor_node(state:State):
    print(">>>>>>>>>>>>>Supervisor node")
    writer =get_stream_writer()
    writer({"node":">>>>>>>>>Supervisor node"})
    # 根据用户的问题，对问题进行分类，分类结果保存到type当中
    # 提示词
    prompt ="""你是一个专业的客服助手，负责对用户的问题进行分类，并将任务分给其他的Agent执行。
              如果用户的问题是和旅游路线规划相关的，那就返回travel。
              如果用户的问题是希望讲一个笑话，那就返回joke。
              如果用户的问题是希望对对联，那就返回couplet。
              如果是其他问题，就返回other。
              除了这几个选项外，不要返回任何的其他内容。

        """
    # 构建提示词
    prompts =[
        {"role":"system","content":prompt},# 系统提示词
        {"role":"user","content":state["messages"][0].content} # 用户的问题
    ]

    # 如果已经分类过了，就直接返回，不需要再次调用模型进行分类
    if "type" in state:
        writer({"supervisor_step":f"问题已经分类过了，分类结果：{state['type']}"})
        return {"type":END}
    else:
        # 调用模型进行分类
        response = llm.invoke(prompts)
        typeRes = response.content
        writer({"supervisor_step":f"问题分类结果：{typeRes}"})
        if typeRes in nodes:
            return {"type":typeRes}
        else:
            raise ValueError(f"type is not in nodes, type:{typeRes}")

    return {}

def other_node(state:State):
    print(">>>>>>>>>>>>>other_node")
    writer =get_stream_writer()
    writer({"node":">>>>>>>>>other_node"})
    return {"messages":[HumanMessage(content="我暂时无法回答这个问题")],"type":"other"}


def travel_node(state:State):
    print(">>>>>>>>>>>>>travel_node")
    writer =get_stream_writer()
    writer({"node":">>>>>>>>>travel_node"})
    return {"messages":[HumanMessage(content="travel_node")],"type":"travel"}

def joke_node(state:State):
    print(">>>>>>>>>>>>>joke_node")
    writer =get_stream_writer()
    writer({"node":">>>>>>>>>joke_node"})
    return {"messages":[HumanMessage(content="joke_node")],"type":"joke"}

def couplet_node(state:State):
    print(">>>>>>>>>>>>>couplet_node")
    writer =get_stream_writer()
    writer({"node":">>>>>>>>>couplet_node"})
    return {"messages":[HumanMessage(content="couplet_node")],"type":"couplet"}

def routing_func(state:State):
    if state["type"] == "travel":
        return "travel_node"
    elif state["type"] == "joke":
        return "joke_node"
    elif state["type"] == "couplet":
        return "couplet_node"
    elif state["type"] == END:
        return END
    else:
        return "other_node"


# 构建图
builder = StateGraph(State)
# 添加节点
builder.add_node("supervisor_node", supervisor_node)
builder.add_node("travel_node",travel_node)
builder.add_node("joke_node",joke_node)
builder.add_node("couplet_node",couplet_node)
builder.add_node("other_node", other_node)

# 添加边 Edge
builder.add_edge(START,"supervisor_node")
builder.add_conditional_edges("supervisor_node",routing_func,["travel_node","joke_node","couplet_node","other_node",END])
# 每个节点处理完都返回到supervisor_node
# start_key end_key
builder.add_edge("travel_node","supervisor_node")
builder.add_edge("joke_node","supervisor_node")
builder.add_edge("couplet_node","supervisor_node")
builder.add_edge("other_node","supervisor_node")

# 构建Graph
# 构建短期记忆
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 执行任务的测试代码
if __name__ == "__main__":
    config = {
        "configurable":{
            "thread_id":"1"
        }
    }
    
    for chunk in graph.stream({"messages": [HumanMessage(content="今天天气怎么样")]},
                config=config,
                stream_mode="custom"):
        print(">>>>>>>>>>>>>stream chunk:",chunk)
