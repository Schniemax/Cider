import asyncio

from cider_ws import CiderWsClient


async def run() -> None:
    async with CiderWsClient(client_name="example-script", client_author="local") as client:
        status = await client.status()
        print("status:", status.raw)

        await client.playpause()
        queue = await client.queue()
        print("queue type:", queue.type)


if __name__ == "__main__":
    asyncio.run(run())
