import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from main import app  # FastAPI instance
from project.models.user import User
from project.schemas.user import UserCreate
from project.routes.user import get_db, get_admin_user
from project.utils.security import hash_password

# Fake DB and user overrides
@pytest.fixture
def override_get_db(test_db: Session):
    def _override():
        yield test_db
    app.dependency_overrides[get_db] = _override

@pytest.fixture
def admin_user():
    return User(id=1, name="Admin", email="admin@example.com", role="admin")

@pytest.fixture
def normal_user():
    return User(id=2, name="User", email="user@example.com", role="user")

@pytest.mark.asyncio
async def test_create_user_success(override_get_db, admin_user, test_db):
    app.dependency_overrides[get_admin_user] = lambda: admin_user

    user_data = {
        "name": "New User",
        "email": "new@example.com",
        "password": "securepass123",
        "mobile": "1234567890",
        "address": "Some Address",
        "role": "user",
        "callback_url": None,
        "callback_key": None,
        "callback_secret_key": None
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/create", json=user_data)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["role"] == "user"

@pytest.mark.asyncio
async def test_create_user_duplicate_email(override_get_db, admin_user, test_db):
    app.dependency_overrides[get_admin_user] = lambda: admin_user

    # Pre-insert user
    test_db.add(User(
        name="Existing User",
        email="existing@example.com",
        password=hash_password("password"),
        mobile="9999999999",
        address="Old Address",
        role="user"
    ))
    test_db.commit()

    user_data = {
        "name": "New User",
        "email": "existing@example.com",
        "password": "securepass123",
        "mobile": "1234567890",
        "address": "Some Address",
        "role": "user",
        "callback_url": None,
        "callback_key": None,
        "callback_secret_key": None
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/create", json=user_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

@pytest.mark.asyncio
async def test_create_user_super_admin_denied(override_get_db, admin_user):
    app.dependency_overrides[get_admin_user] = lambda: admin_user

    user_data = {
        "name": "Blocked User",
        "email": "block@example.com",
        "password": "securepass123",
        "mobile": "8888888888",
        "address": "Nowhere",
        "role": "super_admin",
        "callback_url": None,
        "callback_key": None,
        "callback_secret_key": None
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/create", json=user_data)

    assert response.status_code == 403
    assert response.json()["detail"] == "Cannot create super admin"

@pytest.mark.asyncio
async def test_create_admin_by_user_denied(override_get_db, normal_user):
    app.dependency_overrides[get_admin_user] = lambda: normal_user

    user_data = {
        "name": "Blocked Admin",
        "email": "admin2@example.com",
        "password": "securepass123",
        "mobile": "7777777777",
        "address": "Hidden",
        "role": "admin",
        "callback_url": None,
        "callback_key": None,
        "callback_secret_key": None
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/create", json=user_data)

    assert response.status_code == 403
    assert response.json()["detail"] == "Only admin and super admins can create admins"
