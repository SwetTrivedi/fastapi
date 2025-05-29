from fastapi import FastAPI,Form,File,UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel,Field
import os
import uuid
import shutil
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


# using pydantic 

# class Formdata(BaseModel):
#     username:str
#     password:str

# class Formdata(BaseModel):
#     username:str=Field(min_length=3)
#     password:str=Field(min_length=3,max_length=20)
# @app.post("/login/")
# async def login(data:Annotated[Formdata,Form()]):
#     return data


# @app.get("/",response_class=HTMLResponse)
# async def main():
#     return """
#         <html>
#             <body>
#                 <h2>Single File Upload (Bytes)</h2>
#                 <form action="/files/" enctype="multipart/form-data" method="post">
#                     <input name ="file" type="file">
#                     <input type="submit" value="Upload">
#                 </form>
#                 <h2>Single File Upload (Uploadfile)</h2>
#                 <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
#                     <input name ="file" type="file">
#                     <input type="submit" value="Upload">
#                 </form>
#             </body>
#     </html>
#      """
# @app.post("/files/")
# async def create_file(file:Annotated[bytes | None,File()]=None):
#     if not file:
#         return "Not File"
#     filename=f"{uuid.uuid4()}.bin"
#     save_path=f"uploads/{filename}"
#     os.makedirs("uploads",exist_ok=True)
#     with open(save_path,"wb")as buffer:
#         buffer.write(file)
#     return {"file size ":len(file)}

# Single files 

# @app.post("/uploadfiles/")
# async def create_upload_file(file:Annotated[UploadFile | None,File()]=None):
#     if not file:
#         return "No sch File"
#     save_path=f"uploads/{file.filename}"
#     os.makedirs("uploads",exist_ok=True)
#     with open(save_path,"wb")as buffer:
#         shutil.copyfileobj(file.file,buffer)
#     return{"filename":file.filename,"content_type":file.content_type}


# ##  ###  #### Mutliple data submited 

# @app.get("/",response_class=HTMLResponse)
# async def main():
#     return """
#         <html>
#             <body>
#                 <h2>Multiple File Upload (Uploadfile)</h2>
#                 <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
#                     <input name ="files" type="file" multiple>
#                     <input type="submit" value="Upload">
#                 </form>
#             </body>
#     </html>
#      """
# @app.post("/uploadfiles/")
# async def create_upload_file(files:Annotated[list[UploadFile],File()]):
#     save_files=[]
#     os.makedirs("uploads",exist_ok=True)
#     for file in files:
#         save_path=f"uploads/{file.filename}"
#         with open(save_path,"wb")as buffer:
#             shutil.copyfileobj(file.file,buffer)
#         save_files.append({"filename":file.filename})
#     return save_files