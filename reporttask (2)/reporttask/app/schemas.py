
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class ReportCreate(BaseModel):
    pass

class ReportOut(BaseModel):
    id: int
    status: str
    file_path: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
