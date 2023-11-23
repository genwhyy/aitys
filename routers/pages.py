
from routers.user import create_user
from database import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.templating import Jinja2Templates
from schemas import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas import UserCreate
from routers import form



templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/users/register/")
def register(request: Request):
    return templates.TemplateResponse("reg.html", {"request": request})


@router.post("/users/register/")
async def register(request: Request, db: Session = Depends(get_db)):
    form = UserCreate(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            login=form.login, user_fname=form.user_fname, user_sname=form.user_sname, password=form.password
        )
        try:
            user = create_user(user=user, db=db)
            return responses.RedirectResponse(
                "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
            )  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse("reg.html", form.__dict__)
    return templates.TemplateResponse("reg.html", form.__dict__)

# @router.post("/post/create")
# def create(request: Request, content = )