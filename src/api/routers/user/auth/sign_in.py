from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import UserSignInRequest
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from models.user import UsersORM
from db.get_db import get_db
from security.password import verify_password
from jose import jwt
from core.config import settings


router = APIRouter()

@router.post(
    "/sing-in",
    tags=["users"],
    summary="Аутентификация пользователя по логину/email и паролю",
    description="Аутентифицирует пользователя и возвращает токен доступа.",
    responses={
        200: {"description": "Success"},
        401: {"description": "InvalidCredentials"},
        422: {"description": "IncorrectUserData"},
    }
)
async def sign_in(user: UserSignInRequest, db: Session = Depends(get_db)):
    result = await db.execute(select(UsersORM).where((UsersORM.email == user.email) | (UsersORM.login == user.login)))
    userDB = result.scalar_one_or_none()
    
    if not userDB:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, userDB.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {"sub": str(userDB.id)},
        settings.RANDOM_SECRET,
        algorithm="HS256"
    )

    return JSONResponse(
        content={"token": token},
        status_code=200
    )