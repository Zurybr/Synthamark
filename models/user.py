from pydantic import BaseModel,EmailStr
from typing import Optional
from uuid import UUID

class User(BaseModel):
    id:Optional[int]
    name:str
    email:EmailStr
    password:str
