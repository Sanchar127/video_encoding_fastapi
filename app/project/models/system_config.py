from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base
from datetime import datetime,timezone

class SystemConfig(Base):
    __tablename__ = "system_config"

    id = Column(Integer, primary_key=True, index=True)
    config_key = Column(String, unique=True, nullable=False)
    config_value = Column(String, nullable=False)
    description = Column(String, nullable=False)
    updated_by = Column(Integer, ForeignKey("users.unique_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.timezone.utcnow)
    updated_at = Column(DateTime, default=datetime.timezone.utcnow, onupdate=datetime.timezone.utcnow)
    user = relationship("User", back_populates="system_config")
