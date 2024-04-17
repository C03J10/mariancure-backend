from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import Role
from schemas import RoleBase, RoleCreate , RoleGet

import crud

RolesRouter = APIRouter(tags=["Roles"])

@RolesRouter.get("/roles/", response_model=list[RoleGet])
async def get_roles(db: Session = Depends(get_db)):
    roles = crud.get_all_roles(db)
    return roles

@RolesRouter.get("/roles/{role}", response_model=RoleGet)
async def get_role(db:Session = Depends(get_db), role=int):
    role = crud.get_role(db, role)
    return role

@RolesRouter.post("/roles/", response_model=RoleGet)
async def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    add_role = crud.create_role(db, role)
    return add_role