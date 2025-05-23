from fastapi import FastAPI
from enum import Enum
# define enum class with allowed product categories 
app=FastAPI()


##### Path Predefined #######


# class Productcategory(str,Enum):
#     books="Books"
#     clothing="clothing"
#     electronic="electroic"

# @app.get("/product{category}")
# async def allproducts(category:Productcategory):
#     return {"response":"This is Your All Product ","category":category}




# class Productcategory(str,Enum):
#     books="books"
#     clothing="clothing"
#     electronic="electroic"

# @app.get("/product/{category}")
# async def allproducts(category:Productcategory):
#     if category==Productcategory.books:
#         return {"response":"Books are awesome","category":category}
#     elif category.value=="clothing":
#         return "Niceclothing"
#     else:
#         return "unkowncategory"



###########  Path Convertar ###########



# @app.get("/file/{file_path:path}")
# async def readfiles(file_path:str):
#     return {"You are requested file path ":file_path}
