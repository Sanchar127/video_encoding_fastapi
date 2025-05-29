# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from project.db.database import Base  # Your declarative base
# # from project.models.user import user  # Ensure models are loaded

# # ✅ Replace these with your MySQL test DB details
# TEST_DATABASE_URL = "mysql+pymysql://test_user:test_password@mysql_test_host:3306/test_db"

# engine = create_engine(TEST_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create all tables before tests run
# Base.metadata.create_all(bind=engine)

# @pytest.fixture
# def test_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
