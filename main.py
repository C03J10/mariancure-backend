from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.role_router import RolesRouter
from routers.user_router import UsersRouter
from routers.concern_router import ConcernsRouter
from routers.feedback_router import FeedbacksRouter

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://172.16.0.189:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RolesRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")
app.include_router(ConcernsRouter, prefix="/api")
app.include_router(FeedbacksRouter, prefix="/api")