from .user_data import ExampleUserData, generate_correct_user_data
from .confest import *


@pytest.mark.asyncio
async def test_valid_creating_user(client, db_session):
    """Correct creating user."""
    correct_data = ExampleUserData().correct_user_data

    for data in correct_data:
        response = await client.post(
            "/user/auth/sign-up",
            json=data
        )
        assert response.status_code == 200, f"Error: {response.status_code}"


async def create_user(data, client):
    response = await client.post(
        "/user/auth/sign-up",
        json=data
    )

    assert response.status_code == 200, f"Error: {response.status_code}"


@pytest.mark.asyncio
@pytest.mark.benchmark
async def test_valid_creating_user_random(client, db_session, benchmark):
    """Correct creating user from random user data."""
    user_data = generate_correct_user_data()
    benchmark(lambda: create_user(user_data, client))


@pytest.mark.asyncio
async def test_invalid_creating_user_no_fields(client, db_session):
    """Incorrect creating user with no fields."""

    incorrect_data = ExampleUserData().no_field_user_data
    
    for data in incorrect_data: 
        response = await client.post(
            "/user/auth/sign-up",
            json=data
        )
        assert response.status_code != 200, f"Error: {response.status_code}"


@pytest.mark.asyncio
async def test_invalid_creating_user_incorrect_user_data(client, db_session):
    """Incorrect creating user with incorrect user data."""

    incorrect_data = ExampleUserData().no_field_user_data
    
    for data in incorrect_data: 
        response = await client.post(
            "/user/auth/sign-up",
            json=data
        )
        assert response.status_code != 200, f"Error: {response.status_code}"