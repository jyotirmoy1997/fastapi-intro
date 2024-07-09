from fastapi import APIRouter, Depends
from request_schemas import Blog
from sqlalchemy.orm import Session
from db import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def index():
    return "Index Blog Route"


@router.get("/{id}")
def get_id(id):
    return {
        "data" : id
    }


@router.post("/")
def post_blog(request : Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog