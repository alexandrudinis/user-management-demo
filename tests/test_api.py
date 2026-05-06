import pytest
from fastapi import HTTPException
from app.models import User
from app.schemas import UserCreate, UserUpdate


@pytest.mark.usefixtures("test_client")
class TestUserEndpoints:

    def test_create_user(self, test_client):
        new_user = UserCreate(username="testuser", email="test@example.com", full_name="Test User")
        response = test_client.post("/users/", json=new_user.dict())
        assert response.status_code == 200
        assert response.json()["username"] == "testuser"

    def test_read_users(self, test_client):
        response = test_client.get("/users/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_read_user(self, test_client):
        # Create a user first
        new_user = UserCreate(username="testuser2", email="test2@example.com", full_name="Test User 2")
        response = test_client.post("/users/", json=new_user.dict())
        user_id = response.json()["id"]

        response = test_client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["username"] == "testuser2"

    def test_update_user(self, test_client):
        # Create a user first
        new_user = UserCreate(username="testuser3", email="test3@example.com", full_name="Test User 3")
        response = test_client.post("/users/", json=new_user.dict())
        user_id = response.json()["id"]

        updated_user = UserUpdate(full_name="Updated Test User")
        response = test_client.put(f"/users/{user_id}", json=updated_user.dict())
        assert response.status_code == 200
        assert response.json()["full_name"] == "Updated Test User"

    def test_delete_user(self, test_client):
        # Create a user first
        new_user = UserCreate(username="testuser4", email="test4@example.com", full_name="Test User 4")
        response = test_client.post("/users/", json=new_user.dict())
        user_id = response.json()["id"]

        response = test_client.delete(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["detail"] == "User deleted"

        # Ensure the user is deleted
        response = test_client.get(f"/users/{user_id}")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"