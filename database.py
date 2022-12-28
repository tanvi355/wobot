from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# database name here is 'todos'
DB_URL = "mysql+pymysql://root:password@127.0.0.1:3306/todos"

engine = create_engine(DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, bind=engine)
