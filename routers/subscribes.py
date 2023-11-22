from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import schemas, database, models, oath


router = APIRouter(
    prefix="/subs",
    tags=['Subscribe']
)



@router.post("/", status_code=status.HTTP_201_CREATED)
def Subscribe(subscribe: schemas.Subscribe, db: Session = Depends(database.get_db), current_user: int = Depends(oath.get_current_user)):

    user = db.query(models.User).filter(models.User.id == subscribe.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {subscribe.user_id} does not exist")

    sub_query = db.query(models.Subscribe).filter(
        models.Subscribe.user_id == subscribe.user_id, models.Subscribe.id == current_user.id)

    found_sub = sub_query.first()
    if (subscribe.dir == 1):
        if found_sub:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has alredy subscribed {subscribe.user_id}")
        new_sub = models.Subscribe(user_id=subscribe.user_id, id=current_user.id)
        db.add(new_sub)
        db.commit()
        return {"message": "successfully subscribed"}
    else:
        if not found_sub:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Subscription does not exist")

        sub_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully unsubscribed"}