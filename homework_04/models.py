"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio
import asyncpg
import os

from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

Base = None
Session = None

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)



class User(Base):
    __tablename__ = 'user'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )
    username = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )
    email = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )

    def __repr__(self):
        return "".format(self.code)


class Post(Base):
    __tablename__ = 'post'

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        unique=True,
    )

    title = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    def __repr__(self):
        return "".format(self.code)


async def create_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_main():
    await create_schemas()


if __name__ == "__main__":
    asyncio.run(async_main())
