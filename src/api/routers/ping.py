from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get(
    "/ping",
    tags=["default"],
    summary="Ping",
    description="Ping",
    responses={
        200: {"description": "Success"}
    }
)
async def ping():
    return JSONResponse(
        "PONG!",
        status_code=200
    )