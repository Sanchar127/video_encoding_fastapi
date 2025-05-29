from pydantic import BaseModel,EmailStr
from datetime import datetime
# from uuid import UUID
from enum import Enum
from typing import Optional

# class UserSummary(BaseModel):
#     unique_id: UUID
#     name: str
#     email: EmailStr

    # class Config:
    #     orm_mode = True
class SystemConfigCreate(BaseModel):
    config_key:str
    description: str
    updated_by:str
    created_at:str
    updated_at =datetime


class SystemConfigResponse(BaseModel):
    id: int
    config_key:str
    description: str
    updated_by:str
    created_at:str
    updated_at =datetime
    # user:UserSummary
    class Config:
        orm_mode = True



