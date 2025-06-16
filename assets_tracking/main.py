# main.py (Modified)

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_current_admin_user,
    get_current_asset_user,
    get_password_hash # This is still needed for user registration
)
# Removed: from config import settings
from models import mock_db, UserInDB as DBUser
from schemas import Token, CurrentUser, UserCreate, AdminUserCreate, AssetUserCreate

app = FastAPI(
    title="Real-Time Asset Tracking API",
    description="Backend for tracking movable assets with real-time updates.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Real-Time Asset Tracking API!"}

# --- Registration Endpoints ---
@app.post("/register/asset-user", response_model=CurrentUser, status_code=status.HTTP_201_CREATED)
async def register_asset_user(user: AssetUserCreate):
    existing_user = await authenticate_user(user.username, "", "asset_user")
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered as asset user"
        )
    hashed_password = get_password_hash(user.password)
    new_user = DBUser(username=user.username, hashed_password=hashed_password, role="asset_user")
    mock_db["users"].append(new_user.to_dict())
    return CurrentUser(username=new_user.username, role=new_user.role)

@app.post("/register/admin", response_model=CurrentUser, status_code=status.HTTP_201_CREATED)
async def register_admin_user(user: AdminUserCreate):
    existing_admin = await authenticate_user(user.username, "", "admin")
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered as admin"
        )
    hashed_password = get_password_hash(user.password)
    new_admin = DBUser(username=user.username, hashed_password=hashed_password, role="admin")
    mock_db["admin_users"].append(new_admin.to_dict())
    return CurrentUser(username=new_admin.username, role=new_admin.role)

# --- Login Endpoint ---
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password, "asset_user")
    if not user:
        user = await authenticate_user(form_data.username, form_data.password, "admin")

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- Protected Endpoints ---
@app.get("/users/me", response_model=CurrentUser)
async def read_users_me(current_user: Annotated[CurrentUser, Depends(get_current_user)]):
    return current_user

@app.get("/admin/dashboard")
async def admin_dashboard(current_admin: Annotated[CurrentUser, Depends(get_current_admin_user)]):
    return {"message": f"Welcome, Admin {current_admin.username}! This is your secure dashboard."}

@app.get("/asset-user/profile")
async def asset_user_profile(current_asset_user: Annotated[CurrentUser, Depends(get_current_asset_user)]):
    return {"message": f"Welcome, Asset User {current_asset_user.username}! This is your secure profile."}