from app import app
from httpx import ASGITransport, AsyncClient
from db.base import Base
from db.engine import async_engine
from db.session import async_session_factory
import pytest_asyncio, pytest, warnings


@pytest_asyncio.fixture
async def setup_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await async_engine.dispose()


@pytest_asyncio.fixture
async def db_session():
    async with async_session_factory() as session:
        yield session


@pytest_asyncio.fixture
async def client(setup_db):
    client = AsyncClient(
        transport=ASGITransport(app),
        base_url="http://test"
    )
    
    try:
        yield client
    finally:
        await client.aclose()