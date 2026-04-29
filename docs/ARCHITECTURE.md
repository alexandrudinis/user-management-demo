# User Management Application Architecture

## Project Layout

```
user-management-demo/
│
├── app/
│   ├── main.py               # Main application entry point
│   ├── models.py             # Database models
│   ├── schemas.py            # Pydantic schemas for validation
│   ├── routers/              # Directory for API route definitions
│   │   ├── auth.py           # Authentication routes
│   │   └── users.py          # User management routes
│   └── database.py           # Database connection and setup
│
├── docs/
│   └── ARCHITECTURE.md       # Architecture documentation
│
└── requirements.txt          # Project dependencies
```

## Data Models

We will use SQLAlchemy to define our database models:

### User
- `id`: Integer (Primary Key)
- `email`: String (Unique)
- `hashed_password`: String
- `created_at`: DateTime
- `updated_at`: DateTime

#### `models.py`
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

## Pydantic Schemas

We will use Pydantic for data validation and serialization:

#### `schemas.py`
```python
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models
```

## API Endpoints

Here’s a proposed list of API endpoints:

### Authentication Endpoints (in `auth.py`)
- **POST /auth/login**: Login user and return JWT token.
- **POST /auth/register**: Register a new user.

### User Management Endpoints (in `users.py`)
- **GET /users**: Retrieve all users.
- **GET /users/{user_id}**: Retrieve a specific user by ID.
- **PUT /users/{user_id}**: Update user information.
- **DELETE /users/{user_id}**: Delete a user.

## JWT Authentication

- Use `pyjwt` for token creation and validation.
- Token will be required for routes that modify user data and will be included in the headers as `Authorization: Bearer <token>`.

## Database Setup

#### `database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
```