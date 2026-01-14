from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.notification import NotificationOut, NotificationRequest, NotificationResponse
from app.models.notification_db import Notification
from app.database import get_db

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=NotificationResponse)

def send_notification(
    request: NotificationRequest,
    db: Session = Depends(get_db)
):
    notification = Notification(
        email=request.email,
        message=request.message,
        status="SENT"
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {
        "status": "SUCCESS",
        "detail": f"Notification stored for {notification.email}"
    }

@router.get("/", response_model=list[NotificationOut])
def get_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notification).all()
    return notifications
