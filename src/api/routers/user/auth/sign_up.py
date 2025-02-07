from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from schemas.user import UserSignUpRequest
from models.user import UsersORM
from db.get_db import get_db
from jose import jwt

from security.password import hash_password
from core.config import settings


router = APIRouter()

@router.post(
    "/sign-up",
    tags=["users"],
    summary="Регистрация новых пользователей",
    description="Регистрирует новых пользователей и возвращает токен доступа.",
    responses={
        200: {"description": "Success"},
        409: {"description": "EmailOrLoginAlreadyRegistred"},
        422: {"description": "IncorrectUserData"},
    }
)
async def sign_in(user: UserSignUpRequest, db: Session = Depends(get_db)):
    new_user = UsersORM(
        email=user.email,
        login=user.login,
        password=hash_password(user.password),
        first_name=user.first_name,
        last_name=user.last_name
    )
    
    result = await db.execute(select(UsersORM).where(UsersORM.email == user.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="EmailAlreadyRegistered")

    result = await db.execute(select(UsersORM).where(UsersORM.login == user.login))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="LoginAlreadyRegistered")
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    token = jwt.encode(
        {"sub": str(new_user.id)},
        settings.RANDOM_SECRET,
        algorithm="HS256"
    )

    return JSONResponse(
        content={"token": token},
        status_code=200
    )
