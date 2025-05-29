from fastapi import APIRouter, Depends, HTTPException, status, Request, Response

from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from authlib.integrations.starlette_client import OAuthError
from starlette.config import Config
from ..db.database import SessionLocal,redis_client
from ..models.user import User
from redis import Redis
from ..utils.security import hash_password
from datetime import timedelta
import uuid
import httpx
from .user import create_token,ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from ..auth.auth import store_token


def get_redis():
    return redis_client


router= APIRouter()
config = Config('.env')  

# OAuth setup
oauth = OAuth(config)

# Register OAuth providers
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_or_create_user(db: Session, email: str, name: str, provider: str):
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        # Create new user
        new_user = User(
            unique_id=str(uuid.uuid4()),
            name=name,
            email=email,
            password=hash_password(str(uuid.uuid4())),  # Random password for social login
            role="user",  # Default role
            is_activated=True,
            status="active",
            provider=provider
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    return user

@router.get("/login/google")
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/google")
async def auth_via_google(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis)
):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )
    
    userinfo = token.get('userinfo')
    if not userinfo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not get user info from Google"
        )
    
    email = userinfo.get('email')
    name = userinfo.get('name')
    
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not provided by Google"
        )
    
    user = await get_or_create_user(db, email, name, "google")
    
   
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_token(
        data={"sub": user.unique_id, "type": "access", "role": user.role},
        expires_delta=access_token_expires
    )
    refresh_token = create_token(
        data={"sub": user.unique_id, "type": "refresh", "role": user.role},
        expires_delta=refresh_token_expires
    )

    store_token(redis, access_token, user.unique_id, "access", int(access_token_expires.total_seconds()))
    store_token(redis, refresh_token, user.unique_id, "refresh", int(refresh_token_expires.total_seconds()))

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=int(access_token_expires.total_seconds())
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=int(refresh_token_expires.total_seconds())
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "role": user.role
    }

