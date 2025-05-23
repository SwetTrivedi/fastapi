from fastapi import FastAPI
app=FastAPI()
@app.get("/product")
async def allproducts():
    return {"response":"This is Your All Product "}


@app.get("/product/{product_id}")
async def products(product_id:int):
    return {"response":"Your Product ","product_id":product_id}


@app.post("/product")
async def createproduct(new_product:dict):
    return {"response":"Product Added ","newproduct":new_product}


@app.put("/product/{product_id}")
async def allupdateproducts(new_update:dict,product_id:int):
    return {"response":"Product is updated  ","Hence ur new product":new_update}


@app.patch("/product/{product_id}")
async def someupdateproducts(new_update:dict,product_id:int):
    return {"response":"Product is updated  ","Hence ur new product":new_update}


@app.delete("/product/{product_id}")
def deleteproduct(product_id:int):
    return{"response":"Delete Product","product_id":product_id}