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
from models import User, Post, engine, Session, Base
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from typing import List, Dict


async def async_main():

    users_data: List[Dict]
    posts_data: List[Dict]

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )

    async with Session() as session:
        async with session.begin():
            session.add_all(
                [
                    User(name=user['name'], username=user['username'], email=user['email'])
                    for user in users_data
                ]
            )
            session.add_all(
                [
                    Post(user_id=post['userId'], title=post['title'], body=post['body'])
                    for post in posts_data
                ]
            )
        await session.commit()

    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
