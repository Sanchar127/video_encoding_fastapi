# import pytest
# import pytest_asyncio
# from httpx import AsyncClient
# from fastapi import status
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker
# from project.db.database import get_db
# from project.models.user import User
# from project.models.encodeprofile import EncodeProfiles
# from main import app
# from project.routes.user import get_admin_user
# import uuid
# import os
# DATABASE_URl= os.getenv("DATABASE_URL")
# # Database URL (must point to a test DB)


# # ----------------------
# # Fixture: Async DB Session
# # ----------------------
# @pytest_asyncio.fixture
# async def test_db_session():
#     engine = create_async_engine(DATABASE_URL, echo=True, future=True)
#     AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

#     async def override_get_db():
#         async with AsyncSessionLocal() as session:
#             yield session

#     app.dependency_overrides[get_db] = override_get_db
#     yield AsyncSessionLocal
#     await engine.dispose()

# # ----------------------
# # Fixture: Override admin user dependency
# # ----------------------
# @pytest.fixture(scope="function", autouse=True)
# def override_admin_user():
#     def mock_admin_user():
#         return User(
#             unique_id=str(uuid.uuid4()),
#             name="admin_user",
#             email="admin@example.com",
#             password="securepassword",
#             callback_key="key",
#             callback_url="http://callback.url",
#             callback_secret_key="secret",
#             is_activated=True,
#             status=True,
#             email_notification_status=True,
#             email_notification=True,
#             mobile="1234567890",
#             address="Admin Address",
#             role="admin"
#         )
#     app.dependency_overrides[get_admin_user] = mock_admin_user

# # ----------------------
# # Test: POST /encode-profile
# # ----------------------
# @pytest.mark.asyncio
# async def test_create_encode_profile(test_db_session):
#     test_user_id = str(uuid.uuid4())

#     # Create a user in the DB
#     async with test_db_session() as session:
#         async with session.begin():
#             user = User(
#                 unique_id=test_user_id,
#                 name="testuser",
#                 email="testuserdf5ff8@example.com",
#                 password="testpassword",
#                 callback_key="key",
#                 callback_url="http://callback.url",
#                 callback_secret_key="secret",
#                 is_activated=True,
#                 status=True,
#                 email_notification_status=True,
#                 email_notification=True,
#                 mobile="1234567890",
#                 address="Some Address",
#                 role="admin"
#             )
#             session.add(user)

#     # Send POST request to create encode profile
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         payload = {
#             "name": "1080p Profile",
#             "user_id": test_user_id
#         }
#         response = await ac.post("/encode-profile", json=payload)

#         assert response.status_code == status.HTTP_200_OK
#         assert response.json()["name"] == "1080p Profile"
#         assert response.json()["user_id"] == test_user_id

# # ----------------------
# # Test: GET /encodeprofileDetals
# # ----------------------
# @pytest.mark.asyncio
# async def test_get_all_encode_profiles(test_db_session):
#     test_user_id = str(uuid.uuid4())

#     # Create a user and a profile in the DB
#     async with test_db_session() as session:
#         async with session.begin():
#             user = User(
#                 unique_id=test_user_id,
#                 name="testuser2",
#                 email="testuser27fyf@example.com",
#                 password="testpassword",
#                 callback_key="key",
#                 callback_url="http://callback.url",
#                 callback_secret_key="secret",
#                 is_activated=True,
#                 status=True,
#                 email_notification_status=True,
#                 email_notification=True,
#                 mobile="0987654321",
#                 address="Another Address",
#                 role="admin"
#             )
#             profile = EncodeProfiles(
#                 name="720p Profile",
#                 user_id=test_user_id
#             )
#             session.add_all([user, profile])

#     # Send GET request to retrieve profiles
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/encodeprofile")

#         assert response.status_code == status.HTTP_200_OK
#         data = response.json()
#         print("RESPONSE JSON:", response.json())
#         assert isinstance(data, list)
#         assert any(p["name"] == "720p Profile" for p in data)
