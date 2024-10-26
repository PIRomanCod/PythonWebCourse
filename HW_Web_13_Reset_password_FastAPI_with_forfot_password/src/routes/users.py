from fastapi import APIRouter, Depends, status, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader

from src.database.db import get_db
from src.database.models import User
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.conf.config import settings
from src.schemas import UserResponse, RequestEmail
from src.services.email import send_email

router = APIRouter(prefix="/api/users", tags=["users"])

templates = Jinja2Templates(directory='templates')
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/me/", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


@router.patch('/avatar', response_model=UserResponse)
async def update_avatar_user(file: UploadFile = File(), current_user: User = Depends(auth_service.get_current_user),
                             db: Session = Depends(get_db)):
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    r = cloudinary.uploader.upload(file.file, public_id=f'RestContacts/{current_user.username}', overwrite=True)
    src_url = cloudinary.CloudinaryImage(f'RestContacts/{current_user.username}') \
        .build_url(width=250, height=250, crop='fill', version=r.get('version'))
    user = await repository_users.update_avatar(current_user.email, src_url, db)
    return user


@router.post('/reset_password')
async def request_email(body: RequestEmail, background_tasks: BackgroundTasks, request: Request,
                        db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.email, db)
    if user:
        background_tasks.add_task(send_email, user.email, user.username, request.base_url,
                                  payload={"subject": "Confirmation", "template_name": "reset_password.html"})
        return {"message": "Check your email for the next step."}
    return {"message": "Your email is incorrect"}


@router.get('/password_reset_confirm/{token}')
async def password_reset_confirm(token: str):
    pass
    return {"message": "Page password_reset_confirm", "token": token}


@router.get("/password_reset_confirm/", response_class=HTMLResponse, description="Enter new password")
async def root(request: Request):
    return templates.TemplateResponse('password_reset_confirm.html', {"request": request, "title": "Contact Manager"})


@router.post('/update_password/{token}{password}')
async def update_password(token: str, password: str, db: Session = Depends(get_db)):
    print(f"WTF1{token}")
    print(f"WTF2{password}")
    email = auth_service.get_email_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    new_password = password
    await repository_users.forgot_password(email, db, new_password)
    return {"message": "Password updated"}

