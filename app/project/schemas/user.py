from pydantic import BaseModel, EmailStr, HttpUrl, Field
from uuid import UUID
from enum import Enum
from datetime import datetime
from typing import Optional

# Define an Enum for the role
class Role(str, Enum):
    user = "user"
    admin = "admin"
    super_admin = "super_admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr  # Email is automatically validated by Pydantic
    password: str
    mobile: str
    address: str
    role: Role = Role.user  # Using Enum for role validation
    is_activated: bool = True
    status: bool = True
    callback_key: str
    callback_url: str  # Will validate that it's an HTTP/HTTPS URL
    callback_secret_key: str
    email_notification_status: bool = True
    email_notification: bool = True

class UserOut(BaseModel):
    id: int
    unique_id: UUID
    name: str
    email: EmailStr
    role: Role  # Now using Enum for role
    is_activated: bool
    status: bool
    mobile: str
    address: str
    callback_key: str
    callback_url: str  # This will validate that it's an HTTP/HTTPS URL
    callback_secret_key: str
    email_notification_status: bool = True
    email_notification: bool = True
    created_at: Optional[datetime] = None  # Optional for created_at
    updated_at: Optional[datetime] = None  # Optional for updated_at

class UserUpdate(BaseModel):
    name: str
    email: str
    password: str
    mobile: str
    address: str
    role: str
    is_activated: bool
    status: bool
    email_notification_status: bool
    email_notification: bool
    stream_url: str = None
    callback_url: str = None
    callback_key: str = None
    callback_secret_key: str = None
