from ..db.database import Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class S3Credentials(Base):
    __tablename__ = 's3_credentials'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    access_key = Column(String(60), nullable=False)
    secret_key = Column(String(60), nullable=False)
    region = Column(String(50), nullable=False)
    endpoint = Column(String(255), nullable=False)
    bucket = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)


