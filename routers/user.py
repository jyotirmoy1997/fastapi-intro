from fastapi import APIRouter, Depends
from schemas import User, ShowUser
from sqlalchemy.orm import Session
from db import get_db
import models
from hashing import get_password_hash


router = APIRouter()


@router.get("/")
def getUsers():
    return "Users"


@router.post("/", response_model=ShowUser)
def addUser(request : User, db : Session = Depends(get_db)):
    new_user = models.User(name = request.name, 
                           email = request.email,
                           password = get_password_hash(request.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
