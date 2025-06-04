from db import engine
from tables import users
from sqlalchemy import insert,select,update,delete

#Insert or Create User 
async def create_user(name:str,email:str):
    async with engine.connect() as conn:
        stmt=insert(users).values(name=name,email=email)
        await conn.execute(stmt)
        await conn.commit()