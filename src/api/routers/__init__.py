from fastapi import APIRouter

from .ping import router as ping_router
from .user import router as user_router


router = APIRouter()
router.include_router(ping_router)
router.include_router(user_router)