from sqlalchemy import Column, String, Boolean, Integer, DateTime
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from ..db.database import Base  # Ensure the correct import path for Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String(36), default=lambda: str(uuid4()), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    callback_key = Column(String(200), nullable=False)
    callback_url = Column(String(200), nullable=False)
    callback_secret_key = Column(String(200), nullable=False)
    is_activated = Column(Boolean, default=True)
    status = Column(Boolean, default=False)
    email_notification_status = Column(Boolean, default=True)
    email_notification = Column(Boolean, default=True)
    mobile = Column(String(20), nullable=False)
    address = Column(String(255))
    role = Column(String(20), nullable=False, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)  # Default value to current time
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Updated value on change

    video_jobs = relationship("VideoJob", back_populates="user")
    encode_profiles = relationship("EncodeProfiles", back_populates="user")

