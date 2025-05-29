import redis
from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie,Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from ..schemas.user import UserCreate, UserOut, UserUpdate
from ..models.user import User
from ..utils.security import hash_password
from ..db.database import SessionLocal, redis_client
from ..auth.auth import authenticate_user,store_token,get_current_user
from redis import Redis
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uuid
from ..logging_config import setup_logger
from ..schemas.user import Role
from ..rbac.permission.permission import require_permission
from ..rbac.permission.utils import enforce_role_hierarchy
SECRET_KEY = "sdadasddqe212312edas" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# OAuth2 token handler
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
logger = setup_logger()
# API Router
router = APIRouter()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_redis():
    return redis_client

def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt





def get_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role not in ("admin", "super_admin"):
        raise HTTPException(status_code=403, detail="Insufficient privileges")
    return current_user

@router.post("/token")
def login_for_access_token(
    response: Response,
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = user.unique_id

    # Create tokens
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_token(
    data={"sub": user_id, "type": "access", "role": user.role},
    expires_delta=access_token_expires
)
    refresh_token = create_token(
    data={"sub": user_id, "type": "refresh","role":user.role},
    expires_delta=refresh_token_expires
)


 
    store_token(redis, access_token, user_id, "access", int(access_token_expires.total_seconds()))
    store_token(redis, refresh_token, user_id, "refresh", int(refresh_token_expires.total_seconds()))

    
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

@router.post("/refresh")
def refresh_token(
    response: Response,
    refresh_token: str = Cookie(None),
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis)
):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token missing"
        )

    try:
        # Verify refresh token
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type"
            )
        
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        stored_user_id = redis.get(f"refresh:{refresh_token}")
        if not stored_user_id or stored_user_id.decode() != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token revoked or invalid"
            )

        # Create new access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        new_access_token = create_token(
            data={"sub": user_id, "type": "access"},
            expires_delta=access_token_expires
        )

        # Store new access token
        store_token(
            redis,
            new_access_token,
            user_id,
            "access",
            int(access_token_expires.total_seconds())
        )

        # Set cookie
        response.set_cookie(
            key="access_token",
            value=new_access_token,
            httponly=True,
            secure=True,
            samesite="strict",
            max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )

        return {"access_token": new_access_token, "token_type": "bearer"}
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )
@router.post("/logout")
def logout(
    response: Response,
    access_token: str = Cookie(None),
    refresh_token: str = Cookie(None),
    redis: Redis = Depends(get_redis),
    current_user: User = Depends(get_current_user)
):
    # Remove access token
    if access_token:
        # Blacklist with remaining TTL
        token_data = redis.hgetall(f"token:{access_token}")
        if token_data:
            remaining_ttl = redis.ttl(f"token:{access_token}")
            if remaining_ttl > 0:
                redis.setex(f"blacklist:{access_token}", remaining_ttl, 1)
        
        # Remove from user's token set
        redis.srem(f"user:tokens:{current_user.unique_id}", access_token)
        redis.delete(f"token:{access_token}")
    
    # Remove refresh token
    if refresh_token:
        redis.delete(f"refresh:{refresh_token}")
        redis.srem(f"user:tokens:{current_user.unique_id}", refresh_token)
        redis.delete(f"token:{refresh_token}")
    
    # Clear cookies
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    
    return {"message": "Successfully logged out"}

@router.get("/users", response_model=List[UserOut])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(require_permission("can_view_all_users")),):
    """
	Get all users 
	"""
   
    return db.query(User).all()

@router.get("/user", response_model=UserOut)
def get_user_ById(id: str = Query(..., description="User Unique id  "),db: Session = Depends(get_db), current_user: User = Depends(require_permission("can_view_own_profile")),):
    """
	Get user data by Id.
	"""    
    
    db_user = db.query(User).filter(User.unique_id == id).first()
    return db_user


@router.post("/users/create", response_model=UserOut)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_permission("can_create_users")),
):
    """
    Create user.
    """
    enforce_role_hierarchy(user_data.role, current_user)

    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = hash_password(user_data.password)
    new_user = User(
        unique_id=str(uuid.uuid4()),
        name=user_data.name,
        email=user_data.email,
        password=hashed_password,
        role=user_data.role,
        is_activated=True,
        status="active"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.put("/users/update", response_model=UserOut)
def update_user(
    user_data: UserUpdate,
    user_id: str = Query(..., description="User Unique id"),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_permission("can_update_users")),
    
   
):

    """
	Update user by userId.
	"""
    
    db_user = db.query(User).filter(User.unique_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    enforce_role_hierarchy(user_data.role, current_user, db_user.role)

    # Email duplication check
    if db.query(User).filter(User.email == user_data.email, User.unique_id != user_id).first():
        raise HTTPException(status_code=400, detail="Email already in use")

    # Update user details
    db_user.name = user_data.name
    db_user.email = user_data.email
    db_user.mobile = user_data.mobile
    db_user.address = user_data.address
    db_user.role = user_data.role 
    db_user.callback_url = user_data.callback_url
    db_user.callback_key = user_data.callback_key
    db_user.callback_secret_key = user_data.callback_secret_key
    db_user.is_activated = user_data.is_activated 
    db_user.status = user_data.status
    db_user.email_notification_status = user_data.email_notification_status
    db_user.email_notification = user_data.email_notification
    
    db.commit()
    db.refresh(db_user)
    return db_user





@router.post("/users/blacklist-token")
def blacklist_user_token(
    user_id: str = Query(..., description="User Unique ID"),
    duration_minutes: int = Query(None, description="Duration in minutes to blacklist the token"),
    redis: Redis = Depends(get_redis),
    current_user: User = Depends(require_permission("can_blacklist_other_tokens")),
):
    enforce_role_hierarchy(user_data.role, current_user)
    try:
  
        if current_user.role == "admin" and user_id != current_user.unique_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Admins can only revoke their own tokens"
            )

        key = f"user:tokens:{user_id}"
        try:
            tokens = redis.smembers(key)
        except RedisError as re:
            logger.error(f"Redis error while fetching tokens: {re}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Redis is unavailable. Please try again later."
            )

        if not tokens:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No tokens found for this user"
            )

        try:
            with redis.pipeline() as pipe:
                for token in tokens:
                    token_str = token.decode() if isinstance(token, bytes) else str(token)
                    if duration_minutes and duration_minutes > 0:
                        pipe.setex(f"blacklist:{token_str}", duration_minutes * 60, "1")
                    else:
                        pipe.set(f"blacklist:{token_str}", "1")
                    pipe.sadd("blacklisted_tokens", token_str)
                pipe.execute()
        except RedisError as re:
            logger.error(f"Redis error during blacklisting: {re}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Redis failed to blacklist tokens."
            )

        return {
            "message": f"Tokens for user {user_id} have been blacklisted",
            "duration_minutes": duration_minutes if duration_minutes else "permanently"
        }

    except HTTPException:
        raise  # re-raise known HTTP errors
    except Exception as e:
        logger.error(f"Unexpected error blacklisting tokens for user {user_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected server error occurred while blacklisting tokens."
        )




@router.get("/blacklisted-tokens/details")
def get_blacklisted_token_details(current_user: User = Depends(require_permission("can_view_blacklisted_tokens")),):
    tokens = redis_client.smembers("blacklisted_tokens")
    details = []
    """
	Use to  BlackList the user
	"""
    
    for token in tokens:
        token_str = token.decode() if isinstance(token, bytes) else token

      
        user_id = redis_client.hget(f"token:{token_str}", "user_id")

        if user_id:
            user_id = user_id.decode() if isinstance(user_id, bytes) else user_id

        
        ttl_seconds = redis_client.ttl(f"blacklisted:{token_str}")

      
        if ttl_seconds == -1:
            duration = "permanent"
        elif ttl_seconds == -2:
            duration = "expired"
        else:
            duration = f"{ttl_seconds // 60} minutes"

        details.append({
            "token": token_str,
            "user_id": user_id,
            "remaining_duration": duration
        })

    return {"blacklisted_tokens": details}

@router.get("/tokens/stored")
def get_all_stored_tokens(redis: Redis = Depends(get_redis), current_user: User = Depends(require_permission("can_view_all_tokens"))):
    """
    Retrieve all stored tokens with their associated user IDs.
    """
   
    keys = redis.keys("token:*")
    tokens = []
    for key in keys:
        token = key.decode().replace("token:", "") if isinstance(key, bytes) else key.replace("token:", "")
        # Retrieve user_id from the hash
        user_id = redis.hget(f"token:{token}", "user_id")
        if user_id:
            user_id = user_id.decode() if isinstance(user_id, bytes) else user_id
            tokens.append({"token": token, "user_id": user_id})
    return {"stored_tokens": tokens}


