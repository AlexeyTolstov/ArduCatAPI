from app import app
from core.config import settings
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )