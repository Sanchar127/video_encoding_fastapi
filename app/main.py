from fastapi import FastAPI
from project.db.database import Base,engine
from project.routes import user as user_routes

from project.routes.s3_video import router as s3_routes
from project.routes.encodeprofile import router as encode_profile_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_routes.router)
app.include_router(encode_profile_routes)  
app.include_router(s3_routes)  


# Create DB tables at startup
Base.metadata.create_all(bind=engine)
