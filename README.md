# Book Management System

## Overview

Book Management System is a FastAPI-based backend application for managing books and authors with PostgreSQL storage.

The project includes:

* JWT authentication
* CRUD operations for books and authors
* Filtering, pagination, and sorting
* Import/export functionality (JSON and CSV)
* Repository + service architecture
* SQLAlchemy ORM
* Raw SQL examples
* Pytest test suite
* Alembic migrations

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic v2
* JWT Authentication
* Pytest

---

# Project Structure

```text
book_app/
│
├── api/
├── core/
├── models/
├── repositories/
├── schemas/
├── services/
├── tests/
└── main.py
```

---

# Features

## Authentication

* User registration
* User login
* JWT token generation
* Password hashing with bcrypt
* Protected endpoints

---

## Books

* Create book
* Retrieve all books
* Retrieve book by ID
* Update book
* Delete book
* Filtering
* Pagination
* Sorting

---

## Authors

* Create author
* Retrieve authors
* Update author
* Delete author

---

## Import / Export

### Import

Supports:

* JSON
* CSV

### Export

Supports:

* JSON
* CSV

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/RToister/book_management.git
```

```bash
cd book_management
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/book_db

SECRET_KEY=supersecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Database Setup

## Create PostgreSQL database

```sql
CREATE DATABASE book_db;
```

---

# Alembic Migrations

## Run migrations

```bash
alembic upgrade head
```

---

# Run Application

```bash
uvicorn book_app.main:app --reload
```

Application will run on:

```text
http://127.0.0.1:8000
```

---

# API Documentation

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Authentication Flow

## Register

```http
POST /auth/register
```

Example body:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

## Login

```http
POST /auth/login
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

# Protected Endpoints

These endpoints require JWT token:

* POST /books
* PUT /books/{id}
* DELETE /books/{id}

---

# Testing

Run tests:

```bash
pytest -v
```

---

# Example Endpoints

## Create Author

```http
POST /authors/
```

---

## Create Book

```http
POST /books/
```

---

## Get Books

```http
GET /books/
```

---

## Export Books CSV

```http
GET /export/books/csv
```

---

## Import Books

```http
POST /import/books
```

---

# Implemented Requirements

## API Development

* CRUD endpoints
* Filtering
* Sorting
* Pagination
* Import/export

## Database Interaction

* PostgreSQL
* SQLAlchemy ORM
* Relationships
* Raw SQL query support

## Validation

* Pydantic validation
* Genre enum validation
* Year validation

## Authentication

* JWT authentication
* Password hashing
* Protected routes

## Testing

* Repository tests
* Pytest configuration

---

# Author

Ruslan Toister
