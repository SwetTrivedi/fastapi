# auth.py (Modified)
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from models import mock_db
from schemas import TokenData, UserInDB

# --- JWT Configuration (Hardcoded - as per request) ---
SECRET_KEY = "your-super-secret-key"  # **CHANGE THIS IN PRODUCTION!**
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# ----------------------------------------------------

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer for dependency injection
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # This will be our login endpoint

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Use the hardcoded ACCESS_TOKEN_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # Use the hardcoded SECRET_KEY and ALGORITHM
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_user(username: str, role: str) -> Optional[UserInDB]:
    if role == "asset_user":
        for user_data in mock_db["users"]:
            if user_data["username"] == username:
                return UserInDB(**user_data)
    elif role == "admin":
        for user_data in mock_db["admin_users"]:
            if user_data["username"] == username:
                return UserInDB(**user_data)
    return None

async def authenticate_user(username: str, password: str, role: str) -> Optional[UserInDB]:
    user = await get_user(username, role)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Use the hardcoded SECRET_KEY and ALGORITHM for decoding
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
        token_data = TokenData(username=username, role=role)
    except JWTError:
        raise credentials_exception

    user = await get_user(token_data.username, token_data.role)
    if user is None:
        raise credentials_exception
    return user

async def get_current_admin_user(current_user: UserInDB = Depends(get_current_user)) -> UserInDB:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation forbidden for non-admin users",
        )
    return current_user

async def get_current_asset_user(current_user: UserInDB = Depends(get_current_user)) -> UserInDB:
    if current_user.role != "asset_user":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation forbidden for non-asset users",
        )
    return current_user