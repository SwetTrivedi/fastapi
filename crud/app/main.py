from fastapi import FastAPI

app=FastAPI()

PRODUCTS=[
    {
        "id":1,
        "title":"Thinkpad",
        "desc":"Ram-8 gb SSD"
    },
    {
        "id":2,
        "title":"HP",
        "desc":"Ram-4 gb SSD"
    },
    {
        "id":3,
        "title":"Lenevo",
        "desc":"Ram-2 gb SSD"
    }
]


@app.get("/product")
async def allproduct():
    return PRODUCTS


@app.get("/product/{product_id}")
async def singleproduct(product_id:int):
    for product in PRODUCTS:
        if product["id"]==product_id:
            return product
        

@app.post("/product")
async def createproduct(new_product:dict):
    PRODUCTS.append(new_product)
    return {"status":"created","new_product":new_product}


@app.put("/product/{product_id}")
def update_product_put(product_id: int, new_update_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index] = new_update_product
            return {
                "status": "upadted",
                "product_id": product_id,
                "new update product": new_update_product,
            }

@app.patch("/product/{product_id}")
def update_product_patch(product_id: int, new_update_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index].update(new_update_product)
            return {
                "status": "upadted",
                "product_id": product_id,
                "new update product": PRODUCTS[index],
            }
        


@app.delete("/product/{product_id}")
def update_product(product_id:int):
    for index,product in enumerate(PRODUCTS):
        if product["id"]==product_id:
            PRODUCTS.pop(index)
            return "datadeleted"
