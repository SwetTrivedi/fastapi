from sqlalchemy import MetaData,Table,Column,Integer,String

from db import engine

metadata=MetaData()
users=Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50),nullable=False),
    Column("email",String,nullable=False,unique=True)
)
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
