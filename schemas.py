from pydantic import BaseModel

# Request Schema
class Blog(BaseModel):
    title : str
    body : str

# Response Schema
class ShowBlog(Blog):
    class Config():
        orm_mode = True