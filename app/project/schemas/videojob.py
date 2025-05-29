from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID
class UserSummary(BaseModel):
    unique_id: UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
class ProfileSummary(BaseModel):
    id:int
    name:str
    class Config:
        orm_mode = True
    
class VideoJobRead(BaseModel):
    id: int
    video_filename: str
    job_by: str
    encoding_profile: int
    encoding_profileDetails: int 
    retry: Optional[int]=None
    video_url: Optional[str]=None
    status: str
    user:UserSummary
    encode_profile: ProfileSummary  
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

