"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost:5432/blog_project"

engine = create_async_engine(PG_CONN_URI, echo=True)

Base = declarative_base(bind=engine)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}, username={self.username}, "
            f"email={self.email})"
        )

    def __repr__(self):
        return str(self)

    __mapper_args__ = {"eager_defaults": False}


class Post(Base):

    __tablename__ = "Post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    title = Column(String(256))
    body = Column(String(256))

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(user_id={self.user_id}, "
            f"name={self.title!r}, body={self.body}, "
            # f"user={self.user})"
        )

    def __repr__(self):
        return str(self)

    __mapper_args__ = {"eager_defaults": False}


