# Full-Stack Notification Service 🚀

A full-stack software engineering project demonstrating backend APIs, database integration, and frontend UI communication.

## 🔧 Tech Stack
**Backend**
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

**Frontend**
- HTML
- JavaScript (Fetch API)

**Database**
- SQLite (can be extended to PostgreSQL / MySQL)

**DevOps / Tools**
- Git
- GitHub
- REST APIs
- Swagger / OpenAPI

---

## 🏗 Architecture Overview
## 🏗 Architecture Overview

This project follows a clean, layered full-stack architecture:

### 1️⃣ Frontend (Client Layer)
- Built using **HTML + Vanilla JavaScript**
- Provides a simple UI to:
  - Send notifications (email + message)
  - Fetch all notifications from backend
- Communicates with backend using **REST APIs (Fetch API)**

### 2️⃣ Backend (API Layer)
- Built using **FastAPI**
- Exposes REST endpoints for:
  - Health check
  - Create notifications
  - Retrieve notifications
- Uses **Pydantic models** for request/response validation
- Swagger UI automatically documents APIs

### 3️⃣ Database (Persistence Layer)
- Uses **SQLite** via **SQLAlchemy ORM**
- Stores notification records (email, message, status)
- Easily extensible to PostgreSQL / MySQL

### 4️⃣ DevOps & Tooling
- Version controlled using **Git**
- Hosted on **GitHub**
- API tested via **Swagger UI**
- Backend served using **Uvicorn**
