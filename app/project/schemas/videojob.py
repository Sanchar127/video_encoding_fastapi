from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VideoJobRead(BaseModel):
    id: int
    video_filename: str
    job_by: str
    encoding_profile: int
    encoding_profileDetails: int 
    retry: Optional[int]=None
    video_url: Optional[str]=None
    status: str
    started_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

