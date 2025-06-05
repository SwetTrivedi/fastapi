from  models import User
from db import async_session
from sqlalchemy import select

# Insert Or Create user
async def create_user(name:str,email:str):
    async with async_session()as session:
        user=User(name=name,email=email)
        session.add(user)
        await session.commit()

# Read the Data
async def get_user(user_id:int):
    async with async_session()as session:
        user=await session.get(User,user_id)
        return user

# fetch all data 
async def get_all_user():
    async with async_session()as session:
        stmt=select(User)
        users=await session.scalars(stmt)
        return users.all()
# Update user email

async def update_user_email(user_id:int,new_email:str):
    async with async_session() as session:
        user=await session.get(User,user_id)
        if user:
            user.email=new_email
            await session.commit()
        return user
    
#Delete Data
async def delete_user(user_id:int):
    async with async_session() as session:
        user=await session.get(User,user_id)
        if user:
            await session.delete(user)
            await session.commit()
