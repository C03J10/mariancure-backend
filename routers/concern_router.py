from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import Concern
from schemas import ConcernBase, ConcernCreate, ConcernGet

import crud

ConcernsRouter = APIRouter(tags=["Concerns"])

@ConcernsRouter.get("/concerns/", response_model=list[ConcernGet])
async def get_concerns(db: Session = Depends(get_db)):
    concerns = crud.get_all_concerns(db)
    return concerns

@ConcernsRouter.get("/concerns_with_feedback/", response_model=list[ConcernGet])
async def get_concerns_with_feedback(db: Session = Depends(get_db)):
    concerns = crud.get_all_concerns_with_feedback(db)
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

@ConcernsRouter.post("/add_concern", response_model=ConcernGet)
async def add_concern(concern: ConcernCreate, db:Session = Depends(get_db)):
    concern = crud.create_concern(db, concern)
    return concern