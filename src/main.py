from core.config import settings
from app import app


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        app, 
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )