import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://google.com") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
