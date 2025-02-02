from fastapi import APIRouter
from .routers import router as api_router

router = APIRouter(prefix="/api")
router.include_router(api_router)