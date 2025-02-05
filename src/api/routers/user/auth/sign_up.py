from fastapi import APIRouter
from schemas.user import UserSignUpRequest


router = APIRouter()

@router.post("/sing-up")
async def sign_in(user: UserSignUpRequest):
    return f"Hello, {user.first_name}"