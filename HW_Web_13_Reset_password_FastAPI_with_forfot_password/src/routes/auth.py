from fastapi import Depends, HTTPException, status, APIRouter, Security, BackgroundTasks, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import users as repository_users
from src.schemas import UserModel, UserResponse, TokenModel, RequestEmail
from src.services.auth import auth_service
from src.services.email import send_email

router = APIRouter(prefix="/api/auth", tags=['auth'])
security = HTTPBearer()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(body: UserModel, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)):
    exist_user = await repository_users.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = auth_service.get_password_hash(body.password)
    new_user = await repository_users.create_user(body, db)
    background_tasks.add_task(send_email, new_user.email, new_user.username, request.base_url,
                              payload={"subject": "Confirm your email", "template_name": "email_template.html"})

    return {"message": "Email confirmed"}, new_user


# async def signup(body: UserModel, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)):
#     exist_user = await repository_users.get_user_by_email(body.email, db)
#     if exist_user:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
#     body.password = auth_service.get_password_hash(body.password)
#     new_user = await repository_users.create_user(body, db)
#     background_tasks.add_task(send_email, new_user.email, new_user.username, request.base_url)
#     return {"user": new_user, "detail": "User successfully created. Check your email for confirmation."}


@router.post("/login", response_model=TokenModel)
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.username, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    # Generate JWT
    access_token = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": user.email})
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/refresh_token', response_model=TokenModel)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    email = await auth_service.decode_refresh_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if user.refresh_token != token:
        await repository_users.update_token(user, None, db)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    access_token = await auth_service.create_access_token(data={"sub": email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": email})
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/confirmed_email/{token}')
async def confirmed_email(token: str, db: Session = Depends(get_db)):
    email = auth_service.get_email_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    await repository_users.confirmed_email(email, db)
    return {"message": "Email confirmed"}


@router.post('/request_email')
async def request_email(body: RequestEmail, background_tasks: BackgroundTasks, request: Request,
                        db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.email, db)
    if user:
        if user.confirmed:
            return {"message": "Your email is already confirmed"}
        background_tasks.add_task(send_email, user.email, user.username, request.base_url,
                                  payload={"subject": "Confirm your email", "template_name": "email_template.html"})
    return {"message": "Check your email for confirmation."}

#
# @router.post('/reset_password')
# async def request_email(body: RequestEmail, background_tasks: BackgroundTasks, request: Request,
#                         db: Session = Depends(get_db)):
#     user = await repository_users.get_user_by_email(body.email, db)
#     if user:
#         background_tasks.add_task(send_email, user.email, user.username, request.base_url,
#                                   payload={"subject": "Confirmation", "template_name": "reset_password.html"})
#         return {"message": "Check your email for the next step."}
#     return {"message": "Your email is incorrect"}
#
#
# @router.patch('/update_password/{token},{password}')
# async def update_password(token: str, password: str, db: Session = Depends(get_db)):
#     print(f"WTF1{token}")
#     print(f"WTF2{password}")
#     email = auth_service.get_email_from_token(token)
#     user = await repository_users.get_user_by_email(email, db)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
#     new_password = password
#     await repository_users.forgot_password(email, db, new_password)
#     return {"message": "Password updated"}
