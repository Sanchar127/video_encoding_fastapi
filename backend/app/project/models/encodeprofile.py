from sqlalchemy import Column, Integer, String, ForeignKey, Float,DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base

class EncodeProfiles(Base):
    __tablename__ = 'encode_profiles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    user_id = Column(String(36), ForeignKey("users.unique_id"), nullable=False)  # Corrected to String(36)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user = relationship("User", back_populates="encode_profiles")
    video_jobs = relationship("VideoJob", back_populates="encode_profile")
    profile_details = relationship("EncodeProfileDetails", back_populates="parent_profile", cascade="all, delete-orphan")

class EncodeProfileDetails(Base):
    __tablename__ = "encode_profile_details"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("encode_profiles.id"), nullable=False)
    width = Column(Integer)
    height = Column(Integer)
    video_bitrate = Column(Integer)
    audio_bitrate = Column(Integer)
    audio_channel = Column(Integer, default=2)
    audio_frequency = Column(String(50), default="44100")
    sc_threshold = Column(Integer, default=0)
    profile = Column(String(50), default="high")
    level = Column(Float)
    max_bitrate = Column(Integer)
    bufsize = Column(Integer)
    movflags = Column(String(50), default="faststart")
    pix_fmt = Column(String(50), default="yuv420p")
    acodec = Column(String(50))
    vcodec = Column(String(50))
    force_format = Column(String(50), default="mp4")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    parent_profile = relationship("EncodeProfiles", back_populates="profile_details")
