from .confest import *


@pytest.mark.asyncio
async def test_ping(client, db_session):
    """Checks server availability at /ping endpoint."""

    response = await client.get("/ping")
    assert response.status_code == 200, f"Error: {response.status_code}"