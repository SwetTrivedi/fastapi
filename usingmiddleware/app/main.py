from fastapi import FastAPI
from middleware import my_user_middleware,my_firstmiddleware
#  Built in middleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app=FastAPI()

# creating  middleware 
# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("Middleware: Before middleware ")
#     print(f"request processing the request")
#     response=await call_next(request)
#     print("Middleware:  After processing the request,before returning response")
#     print(f"Response status code {response.status_code}")
#     return response


# app.middleware("http")(my_user_middleware)
# app.middleware("http")(my_firstmiddleware)

#  Built in Middleware

# app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/users")
async def gat_users():
    print("Endpoint : Inside get_users endpoint ")
    return{"data":"all users data"}

@app.get("/products")
async def gat_users():
    print("Endpoint : Inside product endpoint ")
    return{"data":"all product data"}