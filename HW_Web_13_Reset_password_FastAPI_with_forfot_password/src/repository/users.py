# from typing import Optional
from libgravatar import Gravatar
from sqlalchemy.orm import Session
# from fastapi import Request
from fastapi import BackgroundTasks, Request

from src.database.models import User
from src.schemas import UserModel
from src.services.auth import auth_service


async def get_user_by_email(email: str, db: Session) -> User | None:
    return db.query(User).filter_by(email=email).first()


async def create_user(body: UserModel, db: Session):
    g = Gravatar(body.email)

    new_user = User(**body.dict(), avatar=g.get_image())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, refresh_token, db: Session):
    user.refresh_token = refresh_token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email, url: str, db: Session) -> User:
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user


async def forgot_password(email, db: Session, new_password: str):
    user = await get_user_by_email(email, db)
    user.password = auth_service.get_password_hash(new_password)
    print(f"WTF{user.password}")
    # user.password = new_password
    db.commit()
    return user
