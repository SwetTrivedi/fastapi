from sqlmodel import Field,SQLModel,Relationship
#many to many
class userAddressLink(SQLModel,table=True):
    user_id:int=Field(foreign_key="user.id",primary_key=True)
    address_id:int=Field(foreign_key="address.id",primary_key=True)


class User(SQLModel,table=True):
    id:int=Field(primary_key=True)
    name:str
    email:str|None=None
# Relationship Attribute 
    profile:"Profile"|None=Relationship(back_populates="user")
    posts:list["Post"]=Relationship(back_populates="user")
    address:list["Address"]=Relationship(back_populates="user",link_model=userAddressLink)
# One to One Relationship 
class Profile(SQLModel,table=True):
    id:int =Field(primary_key=True)
    user_id:int=Field(foreign_key="user.id",unique=True)
    bio:str

    user:"User"=Relationship(back_populates="profile")
# One to Many Relationship

class Post(SQLModel,table=True):
    id:int=Field(primary_key=True)
    user_id:int=Field(foreign_key="user.id")
    title:str
    content: str
    user:"User"=Relationship(back_populates="posts")

# Many to Many Relationship 

class Address(SQLModel,table=True):
    id:int=Field(primary_key=True)
    street:str
    city:str
    user:list["User"]=Relationship(back_populates="address",link_model=userAddressLink)
