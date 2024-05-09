from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import Concern
from schemas import ConcernBase, ConcernGet

import crud

ConcernsRouter = APIRouter(tags=["Concerns"])

@ConcernsRouter.get("/concerns/", response_model=list[ConcernGet])
async def get_concerns(db: Session = Depends(get_db)):
    concerns = crud.get_all_concerns(db)
    return concerns

@ConcernsRouter.get("/concerns_of_patient/", response_model=list[ConcernGet])
async def get_concerns_of_patient(db: Session = Depends(get_db), user_id=int):
    concerns = crud.get_all_concerns_of_user(db, user_id)
    return concerns

@ConcernsRouter.get("/concerns_by_pharmacist/", response_model=list[ConcernGet])
async def get_concerns_by_pharmacist(db: Session = Depends(get_db), user_id=int):
    concerns = crud.get_concerns_by_pharmacist(db, user_id)
    return concerns

@ConcernsRouter.get("/concerns/{concern_id}", response_model=ConcernGet)
async def get_concern(db:Session = Depends(get_db), concern_id=int):
    concern = crud.get_concern(db, concern_id)
    if concern:
        return concern
    raise HTTPException(status_code=404, detail="Concern not found")

@ConcernsRouter.get("/concern", response_model=ConcernGet)
async def get_concern(db:Session = Depends(get_db), user_id=int):
    concern = crud.get_concern_by_user(db, user_id)
    if concern:
        return concern
    raise HTTPException(status_code=404, detail="Concern not found")

@ConcernsRouter.get("/search_concern/", response_model=list[ConcernGet])
async def search_concern(db: Session = Depends(get_db), name=str):
    concerns = crud.search_concerns(db, name)
    return concerns

@ConcernsRouter.post("/add_concern", response_model=ConcernGet)
async def add_concern(concern: ConcernBase, db:Session = Depends(get_db)):
    concern = crud.create_concern(db, concern)
    return concern