"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from typing import List

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str):
    async with session.get(url, ssl=False) as response:
        response_json = await response.json()
        return response_json


async def fetch_users_data() -> List[dict]:
    async with ClientSession() as session:
        data = await fetch_json(session, USERS_DATA_URL)
        return data


async def fetch_posts_data() -> List[dict]:
    async with ClientSession() as session:
        data = await fetch_json(session, POSTS_DATA_URL)
        return data


async def main():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    print("users= ", users_data)
    print("post= ", posts_data)


if __name__ == '__main__':
    asyncio.run(main())
