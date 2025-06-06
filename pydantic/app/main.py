from fastapi import FastAPI, Body

app = FastAPI()

# @app.post("/user/create")
# async def create_user(payload: dict = Body(...)):
#     name = payload.get("name")
#     age = payload.get("age")

#     if not name or not isinstance(name, str):
#         return {"error": "Name must be a string"}
#     if not age or not isinstance(age, int):
#         return {"error": "Age must be an integer"}

#     return {"message": f"User {name} of age {age} created."}




# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/user/create")
# async def create_user(user: User):
#     return {"message": f"User {user.name} of age {user.age} created."}

