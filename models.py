from sqlalchemy import  Column, Integer, String
from config import Base
from config import engine
class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(100))

