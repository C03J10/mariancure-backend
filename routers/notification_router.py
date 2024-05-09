from fastapi import Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
from models import Notification
from schemas import NotificationBase

import crud

NotificationsRouter = APIRouter(tags=["Notifications"])

@NotificationsRouter.get("/notifications/", response_model=list[NotificationBase])
async def get_notifications(db: Session = Depends(get_db), user_id= int):
    notifications = crud.get_notifications_of_user(db, user_id)
    return notifications

@NotificationsRouter.put("/update_notification/", response_model=NotificationBase)
async def get_notifications(db: Session = Depends(get_db), notification_id= int):
    notification = crud.update_notification(db, notification_id)
    return notification