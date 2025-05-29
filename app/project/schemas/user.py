from pydantic import BaseModel, EmailStr, HttpUrl, Field
from uuid import UUID
from enum import Enum
from datetime import datetime
from typing import Optional


class Role(str, Enum):
    user = "user"
    admin = "admin"
    super_admin = "super_admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr  
    password: str
    mobile: str
    address: str
    role: Role = Role.user 
    is_activated: bool = True
    status: bool = True
    callback_key: str
    callback_url: HttpUrl 
    email_notification_status: bool = True
    email_notification: bool = True

class UserOut(BaseModel):
    id: int
    unique_id: UUID
    name: str
    email: EmailStr
    role: Role  
    is_activated: bool
    status: bool
    mobile: str
    address: str
    callback_key: str
    callback_url: str 
    callback_secret_key: str
    email_notification_status: bool = True
    email_notification: bool = True
    created_at: Optional[datetime] = None  
    updated_at: Optional[datetime] = None  

    class Config:
        orm_mode = True  

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    address: str
    role: Role
    is_activated: bool
    status: bool
    callback_key: str
    callback_url: HttpUrl
    callback_secret_key: str
    email_notification_status: bool
    email_notification: bool
