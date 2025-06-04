from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column ,relationship
from db import engine
from sqlalchemy import String , ForeignKey , Table,Column ,Integer

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    phone:Mapped[int]=mapped_column(Integer,unique=True)

    def __repr__(self) ->str:
        return f"<user(id={self.id} ,name={self.name},email={self.email})"
    

# def create_tables():
#     Base.metadata.create_all(engine)