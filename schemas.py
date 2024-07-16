from pydantic import BaseModel

# Request Schema
class Blog(BaseModel):
    title : str
    body : str

# Response Schema
class ShowBlog(Blog):
    class Config():
        orm_mode = True

    

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    class Config():
        orm_mode = True


class LoginUser(BaseModel):
    username : str
    password : str