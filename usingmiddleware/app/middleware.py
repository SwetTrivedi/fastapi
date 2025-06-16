from fastapi import Request


# async def my_middleware(request:Request,call_next):
#     print("Middleware: Before middleware ")
#     print(f"request processing the request")
#     response=await call_next(request)
#     print("Middleware:  After processing the request,before returning response")
#     print(f"Response status code {response.status_code}")
#     return response


# if  we run the middleware any specific url then 

async def my_user_middleware(request:Request,call_next):
    if request.url.path.startswith("/users"):
        print("Middleware: Before middleware ")
        print(f"request processing the request")
        response=await call_next(request)
        print("Middleware:  After processing the request,before returning response")
        print(f"Response status code {response.status_code}")
        return response
    else:
        print(f"Middleware:Skipping {request.url.path}")
        response=await call_next(request)
        return response




async def my_firstmiddleware(request:Request,call_next):
    print("Middleware: Before middleware ")
    print(f"request processing the request")
    response=await call_next(request)
    print("Middleware:  After processing the request,before returning response")
    print(f"Response status code {response.status_code}")
    return response