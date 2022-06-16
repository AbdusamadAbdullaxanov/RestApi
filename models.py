from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from intiate_sqlalchemy import server, Base
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(String, nullable=False, default=str(datetime.now()))


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, nullable=False, primary_key=True)
    comment = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(String, nullable=False, default=str(datetime.now()))


class BigMetadata(Base):
    __tablename__ = "texts"

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


def start():
    users = Users()
    users.metadata.create_all(server)
    posts = Posts()
    posts.metadata.create_all(server)
    big = BigMetadata()
    big.metadata.create_all()
