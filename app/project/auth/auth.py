from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta  
from uuid import uuid4
from redis import Redis
from ..db.database import redis_client,SessionLocal
from ..models.user import User
from ..utils.security import verify_password
from jose import JWTError, jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "sdadasddqe212312edas" 
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_redis():
    return redis_client

def store_token(redis: Redis, token: str, user_id: str, token_type: str, expires_in: int):
    """Store token data consistently in Redis"""
    try:
    
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
        expires_ts = int(expires_at.timestamp())
        

        token_data = {
            "user_id": user_id,
            "type": token_type,
            "expires": str(expires_ts)
        }
        
        # Use pipeline for atomic operations
        with redis.pipeline() as pipe:
            pipe.hset(f"token:{token}", mapping=token_data)
            pipe.expire(f"token:{token}", expires_in)
            pipe.sadd(f"user:tokens:{user_id}", token)
            if token_type == "refresh":
                pipe.set(f"refresh:{token}", user_id, ex=expires_in)
            pipe.execute()
            
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to store token: {str(e)}"
        )
def authenticate_user(db: Session, email: str, password: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return None
        return user
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {e}")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
    redis=Depends(get_redis),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if redis.get(f"blacklist:{token}"):
            raise HTTPException(status_code=401, detail="Token has been blacklisted")
            
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        role: str = payload.get("role")
        if user_id is None:  
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.unique_id == user_id).first()
    if user is None:
        raise credentials_exception
    return user
