from db.engine import async_engine
from db.base import Base
from db.session import async_session_factory


async def get_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    db = async_session_factory()
    try:
        yield db
    finally:
        await db.close()