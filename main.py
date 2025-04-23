import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio


# define the MCP server
mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m", "mcp_server_fetch"]
)

# configure groq api key
os.environ["GROQ_API_KEY"] = "your_groq_api_key"

# create the AI Agent
agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    mcp_servers=[mcp_fetch_server]
)

# main async function
async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("extract the content and summarize it: https://blogs.nvidia.com/blog/what-is-a-transformer-model/")
        output = result.output
        return output

# run the main function
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)
