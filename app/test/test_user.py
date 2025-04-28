
# import pytest
# from fastapi import HTTPException
# from unittest.mock import MagicMock
# from fastapi import HTTPException
# from project.routes.user import get_admin_user,get_current_user
# from project.routes import user as user_module  # import module instead of function
# from project.routes.user import get_all_users, get_user_ById
# from project.routes.user import create_user,update_user
# from fastapi.security import OAuth2PasswordRequestForm
# from project.routes.user import get_all_stored_tokens


# # class DummyUser:
# #     def __init__(self, role):
# #         self.role = role

# # @pytest.mark.parametrize(
# #     "role,should_pass",
# #     [
# #         ("admin", True),
# #         ("super_admin", True),
# #         ("user", False),
# #     ]
# # )
# # def test_get_admin_user(role, should_pass):
# #     user = DummyUser(role=role)
    
# #     if should_pass:
# #         result = get_admin_user(current_user=user)
# #         assert result == user
# #     else:
# #         with pytest.raises(HTTPException) as exc_info:
# #             get_admin_user(current_user=user)
# #         assert exc_info.value.status_code == 403
# #         assert exc_info.value.detail == "Insufficient privileges"




# # class DummyUser:
# #     def __init__(self, unique_id, is_activated=True, role="user"):
# #         self.unique_id = unique_id
# #         self.is_activated = is_activated
# #         self.role = role

# # @pytest.mark.parametrize(
# #     "token_exists,user_found,is_activated,should_pass",
# #     [
# #         (True, True, True, True),     # Valid token and active user
# #         (False, True, True, False),   # Token not found in Redis
# #         (True, False, True, False),   # User not found in DB
# #         (True, True, False, False),   # User found but not activated
# #     ]
# # )
# # def test_get_current_user(monkeypatch, token_exists, user_found, is_activated, should_pass):
# #     dummy_token = "dummy_token"
# #     dummy_user_id = "dummy_user_id"
    
# #     # Mock redis_client.get
# #     def mock_redis_get(key):
# #         if token_exists and key == f"token:{dummy_token}":
# #             return dummy_user_id
# #         return None
    
# #     # Mock db.query().filter().first()
# #     class DummyQuery:
# #         def filter(self, *args, **kwargs):
# #             return self
# #         def first(self):
# #             if user_found:
# #                 return DummyUser(unique_id=dummy_user_id, is_activated=is_activated)
# #             return None

# #     class DummyDB:
# #         def query(self, model):
# #             return DummyQuery()

# #     # Monkeypatch redis_client and db
# #     monkeypatch.setattr(user_module, "redis_client", MagicMock(get=mock_redis_get))
# #     db = DummyDB()

# #     if should_pass:
# #         result = get_current_user(token=dummy_token, db=db)
# #         assert isinstance(result, DummyUser)
# #         assert result.unique_id == dummy_user_id
# #     else:
# #         with pytest.raises(HTTPException) as exc_info:
# #             get_current_user(token=dummy_token, db=db)
# #         assert exc_info.value.status_code in (401, 403)





# # class DummyUser:
# #     def __init__(self, unique_id, role="admin", is_activated=True):
# #         self.unique_id = unique_id
# #         self.role = role
# #         self.is_activated = is_activated

# # # Dummy DB Session
# # class DummyDBSession:
# #     def __init__(self, users):
# #         self.users = users

# #     def query(self, model):
# #         return self

# #     def all(self):
# #         return self.users

# #     def filter(self, condition):
# #         # Just return self for chaining
# #         return self

# #     def first(self):
# #         # Simulate getting the first user (if users exist)
# #         return self.users[0] if self.users else None

# # @pytest.fixture
# # def dummy_admin_user():
# #     return DummyUser(unique_id="admin-123", role="admin")

# # @pytest.fixture
# # def dummy_users():
# #     return [
# #         DummyUser(unique_id="user-1"),
# #         DummyUser(unique_id="user-2"),
# #     ]

# # def test_get_all_users(dummy_admin_user, dummy_users):
# #     db = DummyDBSession(users=dummy_users)
# #     result = get_all_users(db=db, current_user=dummy_admin_user)

# #     assert result == dummy_users
# #     assert len(result) == 2
# #     assert result[0].unique_id == "user-1"

# # @pytest.mark.parametrize(
# #     "user_exists",
# #     [
# #         True,
# #         False
# #     ]
# # )
# # def test_get_user_ById(dummy_admin_user, dummy_users, user_exists):
# #     users = dummy_users if user_exists else []
# #     db = DummyDBSession(users=users)

# #     if user_exists:
# #         result = get_user_ById(id="user-1", db=db, current_user=dummy_admin_user)
# #         assert result.unique_id == "user-1"
# #     else:
# #         result = get_user_ById(id="user-1", db=db, current_user=dummy_admin_user)
# #         assert result is None









# # Dummy User model to replace SQLAlchemy User and Test for create
# class DummyDBUser:
#     email = "dummy@example.com"
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)

# # Dummy current user
# class DummyUser:
#     def __init__(self, unique_id=None, email=None, role="user", password=None, **kwargs):
#         self.unique_id = unique_id
#         self.email = email
#         self.password = password
#         self.role = role
#         self.__dict__.update(kwargs)

# # Dummy DB session
# class DummyDBSession:
#     def __init__(self, existing_users=None):
#         self.existing_users = existing_users or []
#         self.added_user = None
#         self.committed = False
#         self.refreshed_user = None

#     def query(self, model):
#         return self

#     def filter(self, condition):
#         return self

#     def first(self):
#         # Simulate finding user by email
#         return self.existing_users[0] if self.existing_users else None

#     def add(self, user):
#         self.added_user = user

#     def commit(self):
#         self.committed = True

#     def refresh(self, user):
#         self.refreshed_user = user

# # Dummy password hasher
# def dummy_hash_password(password):
#     return f"hashed-{password}"

# # Fixtures for dummy users
# @pytest.fixture
# def dummy_admin_user():
#     return DummyUser(unique_id="admin-123", role="admin")

# @pytest.fixture
# def dummy_regular_user():
#     return DummyUser(unique_id="user-123", role="user")

# # Monkeypatch User and hash_password automatically for all tests
# @pytest.fixture(autouse=True)
# def mock_user_dependencies(monkeypatch):
#     from project.routes import user as user_module

#     monkeypatch.setattr(user_module, "User", DummyDBUser)
#     monkeypatch.setattr(user_module, "hash_password", dummy_hash_password)

# # Parametrize different test cases
# @pytest.mark.parametrize(
#     "existing_user, role_to_create, creator_role, should_pass, expected_status",
#     [
#         (True, "user", "admin", False, 400),         # Duplicate email
#         (False, "super_admin", "admin", False, 403), # Trying to create super_admin
#         (False, "admin", "user", False, 403),        # Non-admin creating admin
#         (False, "admin", "admin", True, None),       # Admin creating admin (OK)
#         (False, "user", "admin", True, None),        # Admin creating user (OK)
#     ]
# )
# def test_create_user(monkeypatch, existing_user, role_to_create, creator_role, should_pass, expected_status):
#     from project.routes.user import create_user

#     # Prepare dummy user data
#     dummy_user_data = DummyUser(
#         name="Test User",
#         email="test@example.com",
#         password="password123",
#         mobile="1234567890",
#         address="123 Test Street",
#         role=role_to_create,
#         callback_url="SASDADZSDADASDA",
#         callback_key="sdasdasdasdas",
#         callback_secret_key=True,
#         is_activated=True,
#         status=True,
#         email_notification_status=True,
#         email_notification=True,
#     )

#     # Prepare dummy DB session
#     db = DummyDBSession(existing_users=[dummy_user_data] if existing_user else [])

#     # Prepare current user (creator)
#     current_user = DummyUser(unique_id="creator-1", role=creator_role)

#     if should_pass:
#         created_user = create_user(user_data=dummy_user_data, db=db, current_user=current_user)

#         # Assertions for successful creation
#         assert db.added_user is not None
#         assert db.committed
#         assert db.refreshed_user == created_user

#         assert created_user.email == dummy_user_data.email
#         assert created_user.password == "hashed-password123"
#         assert created_user.role == role_to_create
#     else:
#         # Should raise HTTPException
#         with pytest.raises(HTTPException) as exc_info:
#             create_user(user_data=dummy_user_data, db=db, current_user=current_user)

#         assert exc_info.value.status_code == expected_status








# # # Dummy User model for testing



# # class User:
# #     def __init__(self, email, password, is_activated, name, mobile, address, email_notification_status, status):
# #         self.email = email
# #         self.password = password
# #         self.is_activated = is_activated
# #         self.name = name
# #         self.mobile = mobile
# #         self.address = address
# #         self.email_notification_status = email_notification_status
# #         self.status = status

# # # Mocking the session or database query with dummy users
# # @pytest.fixture
# # def dummy_db_session_with_users():
# #     # Dummy data for users
# #     dummy_users = [
# #         User(
# #             email="test@example.com",
# #             password="hashed_password",
# #             is_activated=True,
# #             name="Test User",
# #             mobile="1234567890",
# #             address="123 Test Street",
# #             email_notification_status=True,
# #             status="active"
# #         ),
# #         User(
# #             email="inactive@example.com",
# #             password="hashed_password",
# #             is_activated=False,
# #             name="Inactive User",
# #             mobile="0987654321",
# #             address="456 Inactive Road",
# #             email_notification_status=False,
# #             status="inactive"
# #         ),
# #         User(
# #             email="nonexistent@example.com",
# #             password="hashed_password",
# #             is_activated=False,
# #             name="Nonexistent User",
# #             mobile="1122334455",
# #             address="789 Nonexistent Lane",
# #             email_notification_status=False,
# #             status="inactive"
# #         )
# #     ]
    
# #     # Return a mocked session object that simulates fetching the users
# #     mock_session = MagicMock()
    
# #     # Mock the query method to return the dummy users list
# #     mock_session.query.filter_by.return_value = dummy_users
# #     yield mock_session


# # # Create a mock user object
# # mock_user = MagicMock()
# # mock_user.email = "test@example.com"
# # mock_user.password = "$2b$12$eW5FdHkVjsnF0L6hbqfNXuMTyYcvT4I7nZlXddkIga2DUeGnSV8ZW"  # Example bcrypt hashed password
# # mock_user.is_activated = True

# # # Setup the dummy_db_session_with_users mock

# # dummy_db_session_with_users.query.return_value.filter.return_value.first.return_value = mock_user

# # @pytest.mark.parametrize(
# #     "existing_user_email, password, user_activated, should_pass, expected_status, expected_token",
# #     [
# #         ("test@example.com", "password123", True, True, None, True),  # Valid user, should pass
# #         ("inactive@example.com", "password123", False, False, 403, False),  # Inactive user, should fail
# #         ("nonexistent@example.com", "password123", None, False, 400, False),  # Nonexistent user, should fail
# #         ("test@example.com", "wrongpassword", True, False, 400, False),  # Incorrect password, should fail
# #     ]
# # )
# # def test_login(dummy_db_session_with_users, existing_user_email, password, user_activated, should_pass, expected_status, expected_token):
# #     from project.routes.user import login

# #     # Simulate the form data with the provided email, password, and an empty scope
# #     form_data = OAuth2PasswordRequestForm(username=existing_user_email, password=password, scope="")

# #     # Prepare the mock current user and DB session
# #     db = dummy_db_session_with_users
# #     if existing_user_email == "test@example.com":
# #         db.existing_users[0].is_activated = user_activated  # Set activation status dynamically

# #     if should_pass:
# #         # Call the login function
# #         response = login(form_data=form_data, db=db)

# #         # Assertions for successful login
# #         assert response.status_code == 200
# #         assert "access_token" in response.json()
# #         assert "user_uniqueId" in response.json()

# #         # Check if the token is returned correctly
# #         if expected_token:
# #             assert isinstance(response.json()["access_token"], str)
# #     else:
# #         # Should raise HTTPException
# #         with pytest.raises(HTTPException) as exc_info:
# #             login(form_data=form_data, db=db)

# #         assert exc_info.value.status_code == expected_status



# # # test for get all stored token 

# # # @pytest.fixture
# # # def mock_redis():
# # #     redis_client = MagicMock()

# # #     # Simulating some stored tokens in Redis
# # #     redis_client.keys.return_value = [b"token:abc123", b"token:def456"]

# # #     # Simulating the user IDs associated with these tokens
# # #     redis_client.get.side_effect = lambda key: b"user_1" if key == b"token:abc123" else b"user_2"

# # #     return redis_client

# # # def test_get_all_stored_tokens(mock_redis):
# # #     # Call the function with the mock Redis client
# # #     result = get_all_stored_tokens(mock_redis)

# # #     # Assertions
# # #     assert result["stored_tokens"] == [
# # #         {"token": "abc123", "user_id": "user_1"},
# # #         {"token": "def456", "user_id": "user_2"},
# # #     ]

# # #     # Check if the Redis `keys` and `get` methods were called correctly
# # #     mock_redis.keys.assert_called_once_with("token:*")
# # #     mock_redis.get.assert_any_call(b"token:abc123")
# # #     mock_redis.get.assert_any_call(b"token:def456")


    