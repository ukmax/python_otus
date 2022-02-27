"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import User, Post, create_schemas, async_session


async def create_users(session: AsyncSession, users_list):
    for i in users_list:
        new_user = User(
            id=i['id'],
            name=i['name'],
            username=i['username'],
            email=i['email']
        )
        session.add(new_user)
    await session.commit()


async def create_posts(session: AsyncSession, posts_list):
    for i in posts_list:
        new_post = Post(
            id=i['id'],
            user_id=i['userId'],
            title=i['title'],
            body=i['body']
        )
        session.add(new_post)
    await session.commit()


async def async_main():
    await create_schemas()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    async with async_session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
