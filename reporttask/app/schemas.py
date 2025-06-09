from pydantic import BaseModel, EmailStr
from typing import Optional
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str
