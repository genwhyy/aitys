
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from routers import user, auth, post

from fastapi.middleware.wsgi import WSGIMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def check(db: Session = Depends(get_db)):
    return {"status": "success"}

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)



