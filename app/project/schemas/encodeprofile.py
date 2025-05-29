from pydantic import BaseModel,constr,confloat,EmailStr
from datetime import datetime
from uuid import UUID
from enum import Enum
from typing import Optional

class UserSummary(BaseModel):
    unique_id: UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
class EncodeProfileCreate(BaseModel):
    name: str
    user_id: str
class EncodeProfileResponse(BaseModel):
    id: int
    name: str
    user:UserSummary

    class Config:
        orm_mode = True

class EncodeProfileDetailsCreate(BaseModel):
    
    profile_id: int
    width: int
    height: int
    video_bitrate: int
    audio_bitrate: int
    audio_channel: int
    audio_frequency: str
    sc_threshold: int
    profile: constr(regex=r"^(high|main|baseline)$")
    level: confloat(ge=3.0, le=4.1)
    max_bitrate: int
    bufsize: int
    movflags: str
    pix_fmt: constr(regex=r"^yuv420p$")
    acodec: constr(regex=r"^aac$")
    vcodec: constr(regex=r"^libx264$")
    force_format: constr(regex=r"^mp4$")  
   
     
    class Config:
        orm_mode = True


class EncodeProfileDetailsResponse(BaseModel):
    id: int
    profile_id: int
    width: int
    height: int
    video_bitrate: int
    audio_bitrate: int
    audio_channel: int
    audio_frequency: str
    sc_threshold: int
    profile: str
    level: float
    max_bitrate: int
    bufsize: int
    movflags: str
    pix_fmt: str
    acodec: str
    vcodec: str
    force_format: str
    created_at: Optional[datetime] = None  
    updated_at: Optional[datetime] = None  

    class Config:
        orm_mode = True

