import asyncio
import anyio
from mcp import ClientSession
from mcp_server.djangomcp import DjangoMCP


def test_mcp2_protocol_tools_and_instructions():
    async def exercise():
        server = DjangoMCP(name="successor-test", instructions="original")
        server.append_instructions("extra")
        assert server._lowlevel_server.instructions == "original\n\nextra"
        assert server.session_manager is not None
        client_write, server_read = anyio.create_memory_object_stream(0)
        server_write, client_read = anyio.create_memory_object_stream(0)
        async with anyio.create_task_group() as group:
            async def serve():
                async with server_read, server_write:
                    await server._lowlevel_server.run(
                        server_read, server_write,
                        server._lowlevel_server.create_initialization_options(),
                    )
            group.start_soon(serve)
            async with ClientSession(client_read, client_write) as client:
                await client.initialize()
                tools = await client.list_tools()
                assert "get_server_instructions" in {tool.name for tool in tools.tools}
                result = await client.call_tool("get_server_instructions", {})
                assert not result.is_error
                assert "extra" in result.content[0].text
                await client.list_resources()
                await client.list_prompts()
            group.cancel_scope.cancel()
    asyncio.run(asyncio.wait_for(exercise(), timeout=15))
