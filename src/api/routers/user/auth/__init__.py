from fastapi import APIRouter
from .sign_in import router as sign_in_router
from .sign_up import router as sign_up_router


router = APIRouter(prefix="/auth")
router.include_router(sign_in_router)
router.include_router(sign_up_router)