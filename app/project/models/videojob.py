from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base
from datetime import datetime

class VideoJob(Base):
    __tablename__ = 'video_jobs'

    id = Column(Integer, primary_key=True, index=True)
    video_filename = Column(String(220), nullable=False)
    job_by = Column(String(36), ForeignKey("users.unique_id"), nullable=False)
    encoding_profile = Column(Integer, ForeignKey("encode_profiles.id", ondelete="CASCADE"), nullable=False)
    encoding_profileDetails = Column(Integer, nullable=False)
    status = Column(String(200), nullable=False)
    retry_count = Column(Integer, default=0, nullable=True)

    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="video_jobs")  # use string, no import needed
    encode_profile = relationship("EncodeProfiles", back_populates="video_jobs")
