# # app/main.py

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from project.db.database import Base, engine
# from project.routes.base import api_router, openapi_tags
# from fastapi.testclient import TestClient
# app = FastAPI(
#     title="My API",
#     openapi_tags=openapi_tags
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Register all routes
# app.include_router(api_router)

# # Create DB tables at startup
# Base.metadata.create_all(bind=engine)










from project import create_app
from fastapi.middleware.cors import CORSMiddleware  # Optional if needed
from asgi_csrf import asgi_csrf
from project.config import settings
app = create_app()



def skip_api_paths(scope) -> bool:
    return scope["path"].startswith("/api")

app = asgi_csrf(app, signing_secret=settings.CSRF_SECRET_KEY, always_set_cookie=True, skip_if_scope=skip_api_paths)

# celery = app.celery_app
