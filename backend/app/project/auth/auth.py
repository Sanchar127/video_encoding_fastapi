<<<<<<< HEAD:app/project/auth/auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..db.database import redis_client
from ..models.user import User
from ..utils.security import verify_password
from uuid import uuid4
from ..db.database import SessionLocal
from datetime import timedelta
from sqlalchemy.exc import SQLAlchemyError
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def store_token(token: str, user_id: str, redis_client, is_refresh=False):
    if is_refresh:
        expiration_time = timedelta(days=7)
        redis_key = f"refresh_token:{token}"
    else:
        expiration_time = timedelta(minutes=15)
        redis_key = f"token:{token}"
    
    redis_client.set(redis_key, user_id, ex=expiration_time)
    redis_client.sadd(f"user_tokens:{user_id}", token)




def authenticate_user(db: Session, email: str, password: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return None
        return user
    except SQLAlchemyError as e:
=======
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..db.database import redis_client
from ..models.user import User
from ..utils.security import verify_password
from uuid import uuid4
from ..db.database import SessionLocal
from datetime import timedelta
from sqlalchemy.exc import SQLAlchemyError
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def store_token(token: str, user_id: str, redis_client, is_refresh=False):
    if is_refresh:
        expiration_time = timedelta(days=7)
        redis_key = f"refresh_token:{token}"
    else:
        expiration_time = timedelta(minutes=15)
        redis_key = f"token:{token}"
    
    redis_client.set(redis_key, user_id, ex=expiration_time)
    redis_client.sadd(f"user_tokens:{user_id}", token)




def authenticate_user(db: Session, email: str, password: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            return None
        return user
    except SQLAlchemyError as e:
>>>>>>> 4653c3c (Restructured project: moved app to backend/, added frontend/):backend/app/project/auth/auth.py
        raise Exception(f"Database error: {e}")