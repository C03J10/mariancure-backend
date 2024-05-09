from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.user_router import UsersRouter
from routers.concern_router import ConcernsRouter
from routers.feedback_router import FeedbacksRouter
from routers.notification_router import NotificationsRouter

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://mariancure.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UsersRouter, prefix="/api")
app.include_router(ConcernsRouter, prefix="/api")
app.include_router(FeedbacksRouter, prefix="/api")
app.include_router(NotificationsRouter, prefix="/api")