from fastapi import APIRouter, Depends, HTTPException, status
from schemas import LoginUser
from sqlalchemy.orm import Session
from db import get_db
from hashing import verify_password
import models


router = APIRouter()


@router.post("/login")
def login(request : LoginUser, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    return user