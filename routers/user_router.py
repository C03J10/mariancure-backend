from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import User
from schemas import UserBase, UserCreate , UserGet

import crud

UsersRouter = APIRouter(tags=["Users"])

@UsersRouter.get("/users/", response_model=list[UserGet])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users

@UsersRouter.get("/get_email_address", response_model=UserGet)
async def get_user_by_email_address(db:Session = Depends(get_db), email_address=str):
    user = crud.get_user_by_email_address(db, email_address)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@UsersRouter.post("/add_user", response_model=UserGet)
async def add_user(user: UserCreate, db:Session = Depends(get_db)):
    user = crud.create_user(db, user)
    if user:
        return user
    return None

@UsersRouter.put("/update_password", response_model=UserGet)
async def update_user_password(db:Session = Depends(get_db), email_address=str, password=str):
    user = crud.update_password(db, email_address, password)
    if user:
        return user
    return None

@UsersRouter.get("/login", response_model=UserGet)
async def get_user(db:Session = Depends(get_db), username=str, password=str):
    user = crud.get_user_by_login(db, username, password)
    print(user)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Invalid Login")


