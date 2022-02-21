
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(20))
    email = Column(String(100), unique=True)
    password = Column(String(500))