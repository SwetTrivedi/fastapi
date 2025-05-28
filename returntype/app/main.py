from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()

# class Product(BaseModel):
#     id:int
#     name:str
#     price:float
#     stock: int | None=None

# class Productout(BaseModel):
#     name:str
#     price:float

# @app.get("/products")
# async def get_product() -> Product:
#     return {"id":1,"name":"Vivo","price":33.44,"stock":5}

# @app.get("/products")
# async def get_products() -> List[Product]:
#     return[
#         {"id":1,"name":"Moto","price":20000,"stock":5},
#         {"id":2,"name":"vivo","price":40000,"stock":4},
#         {"id":3,"name":"Redmi","price":30000,"stock":3}
#     ]


# @app.post("/products")
# async def create_product(product:Product)->Product:
#     return product


# @app.post("/products")
# async def create_product(product:Product)->Productout:
#     return product




####################   Includeing and Excluding Concept   ##########################


# products_db={
#     "1":{"id":"1","name":"Laptop","price":"19999.0","stock":10,"is_active":True},
#     "2":{"id":"2","name":"Laptop","price":"20999.0","stock":10,"is_active":False}
# }
# class Product(BaseModel):
#     id:int
#     name:str
#     price:float    

#Including Specific Fields 

# @app.get("/products/{product_id}",response_model=Product,
#         response_model_include={"name","price"})
# async def get_product(product_id:str):
#     return products_db.get(product_id,{})



#Excluding Specific Fields 

# @app.get("/products/{product_id}",response_model=Product,
#         response_model_exclude={"name","price"})
# async def get_product(product_id:str):
#     return products_db.get(product_id,{})








