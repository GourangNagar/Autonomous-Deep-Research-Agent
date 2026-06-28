import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from langchain_community.tools import DuckDuckGoSearchRun

app = Server("duckduckgo-mcp-server")
search_tool = DuckDuckGoSearchRun()

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="duckduckgo_search",
            description="Searches the web using DuckDuckGo",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "duckduckgo_search":
        query = arguments.get("query")
        try:
            result = await asyncio.to_thread(search_tool.invoke, query)
            return [TextContent(type="text", text=str(result))]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e}")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
