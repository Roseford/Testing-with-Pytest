import httpx
import pytest
import pytest_asyncio
from typing import AsyncIterator
from fastapi import FastAPI, status
from pydantic_settings import BaseSettings

app = FastAPI()

class Register(BaseSettings):
    username: str
    password: str
    email: str

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def signUp(register: Register):
    return {
        "username": register.username,
            "email": register.email
            }

@pytest_asyncio.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
        
@pytest.mark.asyncio
async def test_signUp(client: httpx.AsyncClient):
    # Simulate a user registration and login process
    registration_data = {
                "username": "testuser",
                "password": "password123",
                "email": "testuser@example.com"
            }
    response = await client.post("/register", json=registration_data)
    assert response.status_code == 201
    assert response.json() ==  {
                "username": registration_data['username'],
                "email": registration_data['email']
            }
            