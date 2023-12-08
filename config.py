from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "admin" #대표님
pwd = "dlwndwo2"
host = "exgen.cpmqglgzxg0p.ap-northeast-2.rds.amazonaws.com"
port = 3306

DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
