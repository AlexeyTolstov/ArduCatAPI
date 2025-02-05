from fastapi import APIRouter
from schemas.user import UserSignInRequest


router = APIRouter()

@router.post("/sing-in")
async def sign_in(user: UserSignInRequest):
    return "Hello"