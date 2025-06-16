from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.auth_handler import get_password_hash, verify_password, create_access_token, create_refresh_token
from database import get_db
from models import User
from schemas import UserCreate, UserLogin, Token
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(400, detail="Email already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        role=user.role if user.role == "admin" else "user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username, "role": db_user.role},
        expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(data={"sub": db_user.username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
