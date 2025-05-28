from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
app=FastAPI()

# items={
#     "apple":"A juciy fruit ",
#     "banana":"A yellow delight"
# }
#using HTTPException
# @app.get("/items/{item_id}")
# async def read_item(item_id:str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not Found "
#         )
#     return items[item_id]

# Adding Custom Header

# @app.get("/items/{item_id}")
# async def read_item(item_id:str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not Found ",
#             headers={"x-error-type":"itemmissing"}
#         )
#     return items[item_id]


##############  Custom Exception and Custom Handler  #########

# fruits={
#     "apple":"A juciy fruit ",
#     "banana":"A yellow delight"
# }

# #Create Exception
# class FruitException(Exception):
#     def __init__(self, fruit_name:str):
#         self.fruit_name=fruit_name

# # Custom Exception Handler 
# @app.exception_handler(FruitException)
# async def fruit_exception_handler(request:Request,exc:FruitException):
#     return JSONResponse(status_code=418,
#                         content={"message":f"{exc.fruit_name} is not valid "}
#                         )
# @app.get("/fruits/{fruit_name}")
# async def read_fruit(fruit_name:str):
#     if fruit_name not in fruits:
#         raise FruitException(
#             fruit_name=fruit_name
#         )
#     return fruits[fruit_name]

#Override To Builtin Exception 

# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse

# a=FastAPI()

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request,
#                                        exc:RequestValidationError):
#     return PlainTextResponse(str(exc),status_code=400)

# @app.get("items/{item_id}")
# async def read_item(item_id:int):
#     return item_id