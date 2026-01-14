from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.api.notifications import router as notification_router
from app.database import engine
from app.models.notification_db import Notification

app = FastAPI()

# ✅ CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for local/dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Notification.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(notification_router)
