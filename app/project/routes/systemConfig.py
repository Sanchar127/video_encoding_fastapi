from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..logging_config import setup_logger
from ..schemas.systemConfig import SystemConfigCreate, SystemConfigResponse
from ..models.system_config import SystemConfig

logger = setup_logger()
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/system-config", response_model=SystemConfigResponse)
def create_encode_profile(systemconfig: SystemConfigCreate, db: Session = Depends(get_db)):
    """
    Use to set setting encode profile 
    """
    db_config = SystemConfig(**systemconfig.dict())  # populate model from input schema

    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    
    logger.info(f"Created system config with id {db_config.id}")

    return db_config
