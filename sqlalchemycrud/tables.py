from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String,ForeignKey

metadata=MetaData()


# Define the Relationship  = One to many 

users=Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50),nullable=False),
    Column("email",String,nullable=False,unique=True),

)
posts=Table(
    "posts",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("user_id",Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
    Column("title",String(length=50),nullable=False),
    Column("content",String(length=50),nullable=False),

)



# create table in database 
def create_tables():
    metadata.create_all(engine)