from pydantic import BaseModel, EmailStr

class NotificationRequest(BaseModel):
    email: EmailStr
    message: str

class NotificationResponse(BaseModel):
    status: str
    detail: str

class NotificationOut(BaseModel):
    id: int
    email: str
    message: str
    status: str

    class Config:
        from_attributes = True
