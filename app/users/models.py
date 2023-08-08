from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Follow(Base):
    __tablename__ = 'follows'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    follower: Mapped[int] = mapped_column(ForeignKey('users.id'))
    idol: Mapped[int] = mapped_column(ForeignKey('users.id'))


