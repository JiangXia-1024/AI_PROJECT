from mcp.server import Server
from mcp.types import TextContent
import httpx
import json

# 创建MCP服务器实例
app = Server("weather-server")

# 模拟天气数据（实际应用中应调用真实天气API）
WEATHER_DATA = {
    "北京": {"temperature": "25°C", "condition": "晴天", "humidity": "45%"},
    "上海": {"temperature": "28°C", "condition": "多云", "humidity": "60%"},
    "广州": {"temperature": "32°C", "condition": "雷阵雨", "humidity": "75%"},
    "深圳": {"temperature": "31°C", "condition": "多云", "humidity": "70%"},
    "杭州": {"temperature": "26°C", "condition": "小雨", "humidity": "55%"},
}

@app.call_tool()
async def get_weather(city: str) -> list:
    """
    查询指定城市的天气信息
    
    参数:
        city: 城市名称（中文）
    
    返回:
        包含天气信息的文本内容列表
    """
    # 查找城市天气数据
    weather = WEATHER_DATA.get(city)
    
    if weather:
        result = f"【{city}天气】\n温度: {weather['temperature']}\n天气状况: {weather['condition']}\n湿度: {weather['humidity']}"
    else:
        # 如果城市不在预设数据中，返回模拟数据
        result = f"【{city}天气】\n未找到该城市的实时天气数据，请尝试查询以下城市：{', '.join(WEATHER_DATA.keys())}"
    
    return [TextContent(type="text", text=result)]

@app.list_tools()
async def list_tools() -> list:
    """
    列出服务器提供的所有工具
    """
    return [
        {
            "name": "get_weather",
            "description": "查询指定城市的天气信息，包括温度、天气状况和湿度",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称（中文），如：北京、上海、广州等"
                    }
                },
                "required": ["city"]
            }
        }
    ]

# 启动服务器的主函数
if __name__ == "__main__":
    import asyncio
    from mcp.server.stdio import stdio_server
    
    async def main():
        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                app.create_initialization_options()
            )
    
    asyncio.run(main())
