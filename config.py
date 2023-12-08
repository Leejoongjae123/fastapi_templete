from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

user = "admin" #대표님
pwd = "dlwndwo2"
host = "database-2.crbwjwvrwwze.ap-northeast-2.rds.amazonaws.com"
port = 3306

DATABASE_URL = f'mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/information?charset=utf8mb4'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
