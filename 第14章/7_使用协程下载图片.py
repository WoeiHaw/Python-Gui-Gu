import aiohttp
import asyncio
import ssl
import certifi

async def download_picture(session, url):
    print(f"开始下载{url}")
    response = await session.get(url)
    content  = await response.read()
    print("下载完毕")
    with open(f"{url[-10:]}.jpg","wb") as file:
        file.write(content)
    await response.release()


async def main():
    url_list = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhFcqE9Ht9Z_dTYV2MgzxSsOM7WNstAnsKpzQ23x5AFw&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPS2Q2yHjKfD9ynhy43r-OPHjmub4HE60ayqNWRZkjEg&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyTebqfsC5M4PTmTUPf8JcS7nP6ni2uzuB-zeooYrYPw&s=10"
    ]

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    session = aiohttp.ClientSession(connector=connector)

    coroutine_list = [download_picture(session,url)for url in url_list]
    await asyncio.gather(*coroutine_list)
    await session.close()

asyncio.run(main())
