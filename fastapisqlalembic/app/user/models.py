from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False,unique=True)

    def __repr__(self) -> str:
        return f"<user(id={self.id},name={self.name},email={self.email})"