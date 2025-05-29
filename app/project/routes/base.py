# project/routes/base.py

from fastapi import APIRouter
from project.routes import user as user_routes
from project.routes.s3_video import router as s3_routes
from project.routes.encodeprofile import router as encode_profile_routes
from project.routes.init_admin import router as init_admin
from project.routes.social_auth import router as social_auth
api_router = APIRouter()

# Include sub-routers with tags
api_router.include_router(user_routes.router, tags=["Users"])
api_router.include_router(social_auth,tags=["social login"])
api_router.include_router(encode_profile_routes, tags=["Encode Profiles"])
api_router.include_router(s3_routes, tags=["S3 Videos"])
api_router.include_router(init_admin,tags=["first time run"])
# provide openapi_tags for use in FastAPI init
openapi_tags = [
    {"name": "Users", "description": "Operations with user accounts"},
    {"name": "S3 Videos", "description": "Upload and manage videos in S3"},
    {"name": "Encode Profiles", "description": "Manage encoding settings"},
    {"name":"First time run","description":"First time run "},
    {"name":"social login","description":"Social Login"}

]
