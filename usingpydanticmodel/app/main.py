from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Annotated
app=FastAPI()

# class Product(BaseModel):
#     id:int
#     name:str
#     price:float
#     stock:int | None=None


# @app.post("/product")
# async def create_product(new_product:Product):
#     return new_product


# Multiple body parameters

# class Product(BaseModel):
#     name:str
#     price:float
#     stock:int | None=None

# class Seller(BaseModel):
#     username:str
#     full_name:str | None=None


# @app.post("/product")
# async def create_product(product:Product,seller:Seller):
#     return {"product":product,"seller":seller}



#pass a extra field 

# @app.post("/product")
# async def create_product(product:Product,seller:Seller,sec_key:Annotated[str,Body()]):
#     return {"product":product,"seller":seller,"sec_key":sec_key}


#pydantic field pass the validation of atrributes


# class Product(BaseModel):
#     name:str=Field(
#         title="ProductName",
#         description="The name of product",
#         max_length=100,
#         min_length=3
#         )
#     price:float=Field(
#         gt=0,
#         title="the price of the product in usd must be grater "
#         )
#     stock:int|None=Field(
#         default=None,
#         ge=0,
#         title="stock Quantity"
#         )
# @app.post("/product")
# async def create_product(product:Product):
#     return {"product":product}



# Nested Body model
# SubModel 

# class Category(BaseModel):
#     name:str=Field(
#         title="CategoryName",
#         max_length=50,
#         min_length=1
#     )
#     description:str | None=Field(
#         default=None,
#         title="Category Description",
#         max_length=200
#     )

# # Model which will use Submodel 
# class Product(BaseModel):
#     name:str=Field(
#         title="ProductName",
#         description="The name of product",
#         max_length=100,
#         min_length=1
#         )
#     price:float=Field(
#         gt=0,
#         title="the price of the product in usd must be grater "
#         )
#     stock:int|None=Field(
#         default=None,
#         ge=0,
#         title="stock Quantity"
#         )
#     category:Category |None=Field(
#         default=None,
#         title="Product",
#         description="the category to which the product "
#     )

# @app.post("/product")
# async def create_product(product:Product):
#     return {"product":product}


# Many cateogry fields 

# class Category(BaseModel):
#     name:str=Field(
#         title="CategoryName",
#         max_length=50,
#         min_length=1
#     )
#     description:str | None=Field(
#         default=None,
#         title="Category Description",
#         max_length=200
#     )
# class Product(BaseModel):
#     name:str=Field(
#         title="ProductName",
#         description="The name of product",
#         max_length=100,
#         min_length=1
#         )
#     price:float=Field(
#         gt=0,
#         title="the price of the product in usd must be grater "
#         )
#     stock:int|None=Field(
#         default=None,
#         ge=0,
#         title="stock Quantity"
#         )
#     category:list[Category]|None=Field(
#         default=None,
#         title="Product",
#         description="the category to which the product "
#     )
# @app.post("/product")
# async def create_product(product:Product):
#     return {"product":product}
