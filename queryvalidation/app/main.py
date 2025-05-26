from fastapi import FastAPI,Query
from typing import Annotated
app=FastAPI()

PRODUCTS=[
    {"id":1,"title":"Bittu ka Backpack"},
    {"id":2,"title":"Biscuit yaani jisme bish koot koot ke bhra hai "},
    {"id":3,"title":"Gooday khao subah subah "},
]

# # @app.get("/products")
# # async def get_products(search:str | None=None):
# #     if search:
# #         search_lower=search.lower()
# #         filterd_products=[]
# #         for product in PRODUCTS:
# #             if search_lower in product["title"].lower():
# #                 filterd_products.append(product)
# #         return filterd_products
# #     return PRODUCTS
    


# # validation without anoted
    
# # @app.get("/products")
# # async def get_products(search:str | None=Query(deafult=None,max_length=5)):
# #     if search:
# #         search_lower=search.lower()
# #         filterd_products=[]
# #         for product in PRODUCTS:
# #             if search_lower in product["title"].lower():
# #                 filterd_products.append(product)
# #         return filterd_products
# #     return PRODUCTS    

# # validation with anotated
# # @app.get("/products")
# # async def get_products(search:Annotated[str | None,Query(max_length=5)]=None):
# #     if search:
# #         search_lower=search.lower()
# #         filterd_products=[]
# #         for product in PRODUCTS:
# #             if search_lower in product["title"].lower():
# #                 filterd_products.append(product)
# #         return filterd_products
# #     return PRODUCTS    


# # Multiple Search Terms 
@app.get("/products")
async def get_products(search : Annotated[list[str] | None,Query()]=None):
    if search:
        filtered_products=[]
        for product in PRODUCTS:
            for s in search:
                if s.lower() in product["title"].lower():
                    filtered_products.append(product)
        return filtered_products
    return PRODUCTS