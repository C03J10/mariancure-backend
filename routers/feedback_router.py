from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import Assessment
from schemas import FeedbackCreate, ConcernGet

import crud

FeedbacksRouter = APIRouter(tags=["Feedbacks"])

@FeedbacksRouter.post("/add_feedback", response_model=ConcernGet)
async def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    feedback = crud.create_feedback(db, feedback)
    return feedback
