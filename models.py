from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class userModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(25), nullable=False)


class todoModel(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    content = Column(String(500), nullable=False)
    complete = Column(Boolean, nullable=False, default='False')
