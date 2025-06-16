# schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None # Added role to token data

class UserBase(BaseModel):
    username: str = Field(..., example="john_doe")

class UserCreate(UserBase):
    password: str = Field(..., example="securepassword123")

class UserInDB(UserBase):
    hashed_password: str
    role: str # "asset_user" or "admin"

class AdminUserCreate(UserCreate):
    # Admin specific fields if any, otherwise just inherits from UserCreate
    pass

class AssetUserCreate(UserCreate):
    # Asset user specific fields if any
    pass

class AssetUser(UserBase):
    role: str = "asset_user"

class AdminUser(UserBase):
    role: str = "admin"

class CurrentUser(BaseModel):
    username: str
    role: str