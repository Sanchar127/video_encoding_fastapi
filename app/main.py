# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.db.database import Base, engine
from project.routes.base import api_router, openapi_tags
from fastapi.testclient import TestClient
app = FastAPI(
    title="My API",
    openapi_tags=openapi_tags
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
app.include_router(api_router)

# Create DB tables at startup
Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}