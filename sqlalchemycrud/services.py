from db import engine
from tables import users,posts
from sqlalchemy import insert , select , update , delete,asc,desc,func

# insert or create user 

def create_user(name:str,email:str):
    with engine.connect()as conn:
        stmt=insert(users).values(name=name,email=email)
        conn.execute(stmt)
        conn.commit()

def create_post(user_id:int,title:str,content:str):
    with engine.connect()as conn:
        stmt=insert(posts).values(user_id=user_id,title=title,content=content)
        conn.execute(stmt)
        conn.commit()





# get the single data
def get_user_by_id(user_id:int):
    with engine.connect()as conn :
        stmt=select(users).where(users.c.id == user_id)
        result=conn.execute(stmt).first()
        return result 
    
# get all_users 
def get_all_users():
    with engine.connect()as conn :
        stmt=select(users)
        result=conn.execute(stmt).fetchall()
        return result 
    
# get post by user 

def get_posts_by_user(user_id:int):
    with engine.connect()as conn: 
        stmt=select(posts).where(posts.c.user_id==user_id)
        result=conn.execute(stmt).fetchall()
        return result 


#update User Email

def update_user_email(user_id:int,new_email:str):
    with engine.connect()as conn:
        stmt=update(users).where(users.c.id==user_id).values(email=new_email)
        conn.execute(stmt)
        conn.commit


#Delete Post

def delete_post(post_id:int):
    with engine.connect()as conn :
        stmt=delete(posts).where(posts.c.id==post_id)
        conn.execute(stmt)
        conn.commit()

# get all users ordered by name (A-z)
def get_user_ordered_by_name():
    with engine.connect()as conn:
        stmt=select(users).order_by(asc(users.c.name))
        result=conn.execute(stmt).fetchall()
        return result


#  Get the latest post 
def get_post_latest_first():
    with engine.connect()as conn:
        stmt=select(posts).order_by(desc(posts.c.title))
        result=conn.execute(stmt).fetchall()
        return result
    
# Group Post by user (count how many post each user has )
def get_post_count_per_user():
    with engine.connect()as conn:
        stmt=select(posts.c.user_id,func.count(posts.c.id).label("total_post")).group_by(posts.c.user_id)
        result=conn.execute(stmt).fetchall()
        return result
    
# Join user and post (list all posts wih author name )
def get_posts_with_author():
    with engine.connect()as conn:
        stmt=select(
            posts.c.id,
            posts.c.title,
            users.c.name.label("author_name")
        ).join(users,posts.c.user_id==users.c.id)
        result=conn.execute(stmt).fetchall()
        return result


#######################   Using Raw SQl  ##################
from  sqlalchemy import text

def raw_sql_insert():
    with engine.connect()as conn:
        stmt=text("""
            INSERT INTO users(name,email)
                  VALUES(:name,:email)
         """)
        conn.execute(stmt,{"name":"Khushi","email":"khushi420@gmail.com"})
        conn.commit()

def raw_sql_example():
    with engine.connect()as conn:
        stmt=text("SELECT * FROM users WHERE email=:email")
        result=conn.execute(stmt,{"email":"khushi420@gmail.com"}).first()
        return result