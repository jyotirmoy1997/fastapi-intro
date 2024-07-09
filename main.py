from fastapi import FastAPI
from pydantic import BaseModel
from routers import blog
from routers import details
import uvicorn
import models
from db import engine


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(details.router, prefix="/details", tags=["details"])


@app.get("/")
def index():
    return "Root"



if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000
    uvicorn.run(app, host = HOST, port = PORT)