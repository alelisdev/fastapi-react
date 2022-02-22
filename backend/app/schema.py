from typing import List
from pydantic import BaseModel

class UserInfoBase(BaseModel):
    fullname: str
    email: str
class UserCreate(UserInfoBase):
    password: str

class UserInfo(UserInfoBase):
    id: int
    class Config:
        orm_mode = True