from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
import models, schemas, utils, oath
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/all", response_model=List[schemas.UserOut])
def users(db: Session = Depends(get_db), skip=0, limit=100):
    users = db.query(models.User, func.count(models.Subscribe.user_id).label("subscribe")).join(
        models.Subscribe, models.Subscribe.user_id == models.User.id, isouter=True).group_by(models.User.id).limit(limit).offset(skip).all()
    return users


@router.get('/{login}', response_model=schemas.UserOut)
def get_user(login: str, db: Session = Depends(get_db), ):
    user = db.query(models.User, func.count(models.Subscribe.user_id).label("subscribe")).join(
        models.Subscribe, models.Subscribe.user_id == models.User.id, isouter=True).filter(models.User.login == login).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {login} does not exist")

    return user