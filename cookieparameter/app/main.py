# from fastapi import FastAPI,Cookie
# from typing import Annotated
from pydantic import BaseModel ,Field
# app=FastAPI()
# @app.get("/products/recommendations")
# async def get_recomendations(session_id:Annotated[str | None,Cookie()]=None):
#     if session_id:
#         return{"message":f"Recommendations for session {session_id}"}
#     return {"message":"No session "}
