import pytest
from unittest.mock import Mock,MagicMock,patch
from fastapi import HTTPException
from uuid import uuid4
from uuid import UUID
from datetime import datetime,timedelta
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional
from project.schemas.user import UserCreate,UserOut,UserUpdate
from project.routes.user import get_current_user,create_user,update_user,blacklist_user_token,get_blacklisted_token_details
from project.auth.auth import authenticate_user,store_token
# # Schemas from the user

class Role(str, Enum):
    user = "user"
    admin = "admin"
    super_admin = "super_admin"
    

# Simulated User class for testing
class User:
    def __init__(self, id: int, unique_id: UUID, name: str, email: str, password: str, mobile: str, role: Role = Role.user, is_activated: bool = True, **kwargs):
        self.id = id
        self.unique_id = unique_id
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.role = role
        self.is_activated = is_activated
        self.status = kwargs.get("status", True)
        self.address = kwargs.get("address")
        self.callback_key = kwargs.get("callback_key")
        self.callback_url = kwargs.get("callback_url")
        self.callback_secret_key = kwargs.get("callback_secret_key")
        self.email_notification_status = kwargs.get("email_notification_status", True)
        self.email_notification = kwargs.get("email_notification", True)
        self.created_at = kwargs.get("created_at")
        self.updated_at = kwargs.get("updated_at")

# Dummy data stores
dummy_users = {}
dummy_tokens = {}
dummy_blacklisted_tokens = {}
dummy_user_tokens = {}

# Mocked dependencies
mock_db = Mock()
mock_redis_client = Mock()

def reset_dummy_data():
    dummy_users.clear()
    dummy_tokens.clear()
    dummy_blacklisted_tokens.clear()
    dummy_user_tokens.clear()


def hash_password(password: str) -> str:
    return f"hashed_{password}"

# Pytest fixtures and tests
@pytest.fixture(autouse=True)
def setup_and_teardown():
    reset_dummy_data()
    yield
    reset_dummy_data()

    
@pytest.fixture
def redis_mock(mocker):
    return mocker.MagicMock()

@pytest.fixture
def db_mock():
    return MagicMock()





@pytest.fixture
def redis_mock():
    return MagicMock()


@pytest.fixture
def admin_user():
    user = User(
        id=1,
        unique_id=str(uuid4()),
        name="Admin User",
        email="admin@example.com",
        password=hash_password("admin123"),
        mobile="1234567890",
        role=Role.admin,
        is_activated=True,
        status=True,
        address="123 Admin St",
        callback_key="admin_key",
        callback_url="https://admin.example.com/callback",
        callback_secret_key="admin_secret",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    dummy_users[user.unique_id] = user
    return user

@pytest.fixture
def super_admin_user():
    user = User(
        id=2,
        unique_id=str(uuid4()),
        name="Super Admin",
        email="superadmin@example.com",
        password=hash_password("super123"),
        mobile="0987654321",
        role=Role.super_admin,
        is_activated=True,
        status=True,
        address="456 Super St",
        callback_key="super_key",
        callback_url="https://superadmin.example.com/callback",
        callback_secret_key="super_secret",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    dummy_users[user.unique_id] = user
    return user

@pytest.fixture
def regular_user():
    user = User(
        id=3,
        unique_id=str(uuid4()),
        name="Regular User",
        email="user@example.com",
        password=hash_password("user123"),
        mobile="5555555555",
        role=Role.user,
        is_activated=True,
        status=True,
        address="789 User St",
        callback_key="user_key",
        callback_url="https://user.example.com/callback",
        callback_secret_key="user_secret",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    dummy_users[user.unique_id] = user
    return user

def test_authenticate_user_success(regular_user, mocker):
    mocker.patch("project.auth.auth.verify_password", return_value=True)
    mock_db = mocker.MagicMock()
    mock_db.query().filter().first.return_value = regular_user
    user = authenticate_user(mock_db, "user@example.com", "user123")
    assert user.email == "user@example.com"

def test_authenticate_user_invalid_credentials(regular_user, mocker):
    mocker.patch("project.auth.auth.verify_password", return_value=False)
    
    mock_db = mocker.MagicMock()
    mock_db.query().filter().first.return_value = regular_user  

    user = authenticate_user(mock_db, "user@example.com", "wrongpassword")
    assert user is None

def test_store_token():
    redis_mock = MagicMock()

    user_id = str(uuid4())
    token = str(uuid4())

    # Call the store_token function with the mock
    store_token(token, user_id, redis_client=redis_mock)

    # Check correct key and expiration for access token
    redis_mock.set.assert_called_once_with(
        f"token:{token}", user_id, ex=timedelta(minutes=15)
    )
    redis_mock.sadd.assert_called_once_with(
        f"user_tokens:{user_id}", token
    )


def test_get_current_user_valid_token(regular_user, redis_mock, db_mock):
    token = str(uuid4())
    
    #
    redis_mock.get.side_effect = lambda key: {
        f"token:{token}": regular_user.unique_id,
        f"blacklist:{token}": None  
    }.get(key, None) 
    
    
    db_mock.query().filter().first.return_value = regular_user

 
    user = get_current_user(token=token, db=db_mock, redis=redis_mock)

   
    assert user.unique_id == regular_user.unique_id

def test_get_current_user_blacklisted_token(regular_user, redis_mock, db_mock):
    token = str(uuid4())
    
   
    redis_mock.get.side_effect = lambda key: {
        f"token:{token}": regular_user.unique_id,   
        f"blacklist:{token}": "1"                   
    }.get(key, None)  
    
    
    db_mock.query().filter().first.return_value = regular_user

    # Call the get_current_user function and check for the expected exception
    with pytest.raises(HTTPException) as exc:
        get_current_user(token=token, db=db_mock, redis=redis_mock)

    assert exc.value.status_code == 401
    assert exc.value.detail == "Token has been blacklisted"


def test_get_current_user_invalid_token(redis_mock, db_mock):
    invalid_token = str(uuid4())  # Generate an invalid token
    
    # Mock Redis to return None for the invalid token (simulating an invalid or expired token)
    redis_mock.get.side_effect = lambda key: None  
    # Ensure the DB mock isn't used because the token is invalid (it shouldn't reach here)
    db_mock.query().filter().first.return_value = None
    
    # Call the get_current_user function and check for the expected exception
    with pytest.raises(HTTPException) as exc:
        get_current_user(token=invalid_token, db=db_mock, redis=redis_mock)
    
    # Assert that the exception is raised with the expected status code and detail
    assert exc.value.status_code == 401
    assert exc.value.detail == "Invalid or expired token"


@patch("project.routes.user.redis_client")  # patch in the module where it's used
def test_blacklist_user_token_success(mock_redis):
    # Setup
    user_id = str(uuid4())
    token = str(uuid4())
    admin_user = MagicMock()
    admin_user.unique_id = user_id
    admin_user.role = "admin"

    mock_redis.smembers.return_value = [token.encode()]
    mock_redis.set.return_value = None
    mock_redis.sadd.return_value = None

    result = blacklist_user_token(user_id, 60, admin_user)

    assert result["message"] == f"Tokens for user {user_id} have been blacklisted"
    assert result["duration_minutes"] == 60




@patch("project.routes.user.redis_client")
def test_get_blacklisted_token_details(mock_redis, admin_user):
    token = str(uuid4())
    user_id = admin_user.unique_id

    # Simulate Redis content
    mock_redis.smembers.return_value = [token.encode()]
    mock_redis.get.side_effect = lambda key: user_id if key == f"token:{token}" else "1"  # handle token:<token> and blacklist:<token>

    result = get_blacklisted_token_details()

    assert len(result["blacklisted_tokens"]) == 1
    assert result["blacklisted_tokens"][0]["token"] == token
    assert result["blacklisted_tokens"][0]["user_id"] == user_id


# @pytest.mark.asyncio
# async def test_blacklist_user_token_admin_restriction(mock_redis):
#     user_id = str(uuid4())
#     token = str(uuid4())
#     admin_user = MagicMock()
#     admin_user.unique_id = user_id
#     admin_user.role = "admin"

#     mock_redis.smembers.return_value = [token.encode()]
#     mock_redis.set.return_value = None
#     mock_redis.sadd.return_value = None
#     with pytest.raises(HTTPException) as exc:
#         await blacklist_user_token(user_id, 60, admin_user)

#     assert exc.value.status_code == 403
#     assert exc.value.detail == "Admins can only revoke their own token"




def test_create_user_success(redis_mock, db_mock, admin_user):
    user_data = UserCreate(
        name="New User",
        email="newuser@example.com",
        password="new123",
        mobile="1112223333",
        address="101 New St",
        role=Role.user,
        callback_key="new_key",
        callback_url="https://newuser.example.com/callback",
        callback_secret_key="new_secret"
    )

    # Simulate no existing user with the same email
    db_mock.query.return_value.filter.return_value.first.return_value = None

    db_mock.add.side_effect = lambda x: None
    db_mock.commit.side_effect = lambda: None
    db_mock.refresh.side_effect = lambda x: setattr(x, "id", "fake-id")

    new_user = create_user(user_data=user_data, db=db_mock, current_user=admin_user)

    assert new_user.email == user_data.email
    assert new_user.name == user_data.name


def test_create_user_duplicate_email(admin_user):
    user_data = UserCreate(
        name="New User",
        email="user@example.com",  # This email is assumed to already exist
        password="new123",
        mobile="1112223333",
        address="101 New St",
        role=Role.user,
        callback_key="new_key",
        callback_url="https://newuser.example.com/callback",
        callback_secret_key="new_secret"
    )

    # Setup mock DB to simulate duplicate email
    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.first.return_value = True  # Simulate existing user

    with pytest.raises(HTTPException) as exc:
        create_user(user_data=user_data, db=db_mock, current_user=admin_user)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Email already registered"




def test_create_user_super_admin_forbidden(admin_user):
    user_data = UserCreate(
        name="New User",
        email="newuser@example.com",
        password="new123",
        mobile="1112223333",
        address="101 New St",
        role=Role.super_admin,  # Trying to create a super admin
        callback_key="new_key",
        callback_url="https://newuser.example.com/callback",
        callback_secret_key="new_secret"
    )

    db_mock = MagicMock()
    db_mock.query.return_value.filter.return_value.first.return_value = None  # No duplicate

    with pytest.raises(HTTPException) as exc:
        create_user(user_data=user_data, db=db_mock, current_user=admin_user)

    assert exc.value.status_code == 403
    assert exc.value.detail == "Cannot create super admin"


# def test_update_user_success(super_admin_user, regular_user):
#     user_data = UserUpdate(
#         name="Updated User",
#         email="updated@example.com",
#         password="new123",
#         mobile="9998887777",
#         address="202 Updated St",
#         role=Role.user,
#         is_activated=True,
#         status=True,
#         email_notification_status=True,
#         email_notification=True,
#         stream_url="https://stream.example.com",
#         callback_url="https://updated.example.com/callback",
#         callback_key="updated_key",
#         callback_secret_key="updated_secret"
#     )

#     db_mock = MagicMock()
#     db_mock.query.return_value.filter.return_value.first.return_value = regular_user
#     db_mock.commit.side_effect = lambda: None
#     db_mock.refresh.side_effect = lambda x: setattr(x, "updated_at", "2025-04-29T12:00:00Z")

#     updated_user = update_user(
#         user_id=regular_user.unique_id,
#         user=user_data,  
#         db=db_mock,
#         current_user=super_admin_user
#     )

#     assert updated_user.name == "Updated User"
#     assert updated_user.email == "updated@example.com"
#     assert updated_user.mobile == "9998887777"
#     assert updated_user.updated_at is not None


# def test_update_user_duplicate_email(super_admin_user, regular_user, admin_user):
#     user_data = UserUpdate(
#         name="Updated User",
#         email="admin@example.com",
#         password="new123",
#         mobile="9998887777",
#         address="202 Updated St",
#         role=Role.user,
#         is_activated=True,
#         status=True,
#         email_notification_status=True,
#         email_notification=True
#     )
#     with pytest.raises(HTTPException) as exc:
#         update_user(regular_user.unique_id, user_data, super_admin_user)
#     assert exc.value.status_code == 400
#     assert exc.value.detail == "Email already in use"

# def test_update_user_admin_cannot_update_other_admin(admin_user, regular_user):
#     user_data = UserUpdate(
#         name="Updated User",
#         email="updated@example.com",
#         password="new123",
#         mobile="9998887777",
#         address="202 Updated St",
#         role=Role.admin,
#         is_activated=True,
#         status=True,
#         email_notification_status=True,
#         email_notification=True
#     )
#     with pytest.raises(HTTPException) as exc:
#         update_user(regular_user.unique_id, user_data, admin_user)
#     assert exc.value.status_code == 403
#     assert exc.value.detail == "Admins can only update themselves"







