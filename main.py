from fastapi import FastAPI
from pydantic import BaseModel
from routers import blog, details, user, auth
import uvicorn
import models
from db import engine


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(details.router, prefix="/details", tags=["details"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
def index():
    return "Root"



if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000
    uvicorn.run(app, host = HOST, port = PORT)