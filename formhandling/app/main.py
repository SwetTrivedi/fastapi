from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from typing import Annotated
app=FastAPI()


# Simple HTML form for testing
# application/x-www-form-urlencoded 
@app.get("/",response_class=HTMLResponse)
async def get_form():
    return """ 
    <html>
        <body>
            <h2>Login Form</h2>
            <Form action="/login/" method="post">
                <label type="username">Username:<label><br>
                <input type="text" id="username" name="username"><br>
                <label type="password">Password:<label><br>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="submit">
            </form>
        </body>
    </html>
    """
@app.post("/login/")
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
    return{"username":username,"password_length":len(password)}


# form with validation 
# @app.post("/login/")
# async def login(
#     username:Annotated[str,Form(min_length=3)],
#     password:Annotated[str,Form(min_length=3,max_length=7)]
#     ):
#     return{"username":username,"password_length":len(password)}