from fastapi import APIRouter, Depends, status, HTTPException
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

# Getting All Blogs
@router.get("/")
def index(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Getting a single blog by id
@router.get("/{id}")
def get_blog(id : int, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # If blog not matches, then we have to throw a 404 not found error
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Blog not found")

    return blog
    

# Endpoint for creating a new blog
@router.post("/", status_code = status.HTTP_201_CREATED)
def post_blog(request : Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id: int, request: Blog, db: Session = Depends(get_db)):
    # Check if the blog post exists
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    # Perform the update
    blog.update(request.dict())
    db.commit()
    
    return {"msg": "updated"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {
        "msg": "Content Deleted"
    }