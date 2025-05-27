from fastapi import FastAPI

app=FastAPI()

# Single queryparameter

# @app.get("/product")
# async def product(category:str):
#     return{"status":"OK","category":category}


# Multiple Queryparameter 

# @app.get("/product")
# async def product(category:str,limit:int):
#     return{"status":"OK","category":category,"limit":limit}


# Optional Query Parameter 

# @app.get("/product")
# async def product(limit:int,category:str | None=None):
#     return{"status":"OK","category":category,"limit":limit}

# Path parameter and querparameter

@app.get("/product/{year}")
async def product(year:str,category:str):
    return{"status":"OK","year":year,"category":category}