import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from pydantic_settings import BaseSettings

app = FastAPI()

class Register(BaseSettings):
    username: str
    password: str
    email: str

@app.post("/register", status_code=status.HTTP_201_CREATED)
def signUp(register: Register):
    return {
        "username": register.username,
            "email": register.email
    }

@pytest.fixture()
def client():
    return TestClient(app)

def test_signUp(client: TestClient) -> None:
    # Simulate a user registration and login process
    registration_data = {
                "username": "testuser",
                "password": "password123",
                "email": "testuser@example.com"
            }
    response = client.post("/register", json=registration_data)
    assert response.status_code == 201
    assert response.json() ==  {
                "username": registration_data['username'],
                "email": registration_data['email']
            }
            