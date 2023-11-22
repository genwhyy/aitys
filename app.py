
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from routers import user, auth, post, likes, subscribes
from fastapi.middleware.cors import CORSMiddleware

from fastapi.middleware.wsgi import WSGIMiddleware

origins = ["http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def check(db: Session = Depends(get_db)):
    return {"status": "success"}


app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(likes.router)
app.include_router(subscribes.router)



