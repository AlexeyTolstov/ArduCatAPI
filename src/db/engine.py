from sqlalchemy.ext.asyncio import create_async_engine
from core.config import settings


async_engine = create_async_engine(
    url=settings.ASYNC_DATABASE_URL,
    echo=False
)