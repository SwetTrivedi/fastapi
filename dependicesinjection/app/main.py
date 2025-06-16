from fastapi import FastAPI,Depends
from typing import Annotated
app=FastAPI()

#Create dependency function

async def common(q:str |None=None,skip:int=0,limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}

#  using dependency in endpoints
@app.get("/items")
async def read_items(commons:Annotated[dict,Depends(common)]):
    return common
