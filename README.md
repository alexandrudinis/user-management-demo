# User Management Demo

## Project Description
This project is a user management application built using FastAPI, featuring JWT authentication, CRUD functionality, and SQLite storage. It allows for the management of users, including creating, reading, updating, and deleting user records.

## Features
- User Registration and Authentication
- CRUD operations for user management
- JWT Token Authentication
- Data validation using Pydantic
- Lightweight and easy to deploy using Docker

## Project Structure
```
user-management-demo/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers/
│   │   └── users.py
│   └── utils/
│       └── auth.py
├── docs/
│   └── ARCHITECTURE.md
├── requirements.txt
├── Dockerfile
└── README.md
```

## Installation
To get started with this project, clone the repository and install the dependencies:
```bash
git clone https://github.com/alexandrudinis/user-management-demo.git
cd user-management-demo
pip install -r requirements.txt
```

## Running the Application
To run the application locally, use the command:
```bash
uvicorn app.main:app --reload
```

## API Endpoints
| Method | Path               | Description                   | Auth Required |
|--------|--------------------|-------------------------------|---------------|
| POST   | /users             | Create a new user            | Yes           |
| GET    | /users/{user_id}   | Get user details by ID       | Yes           |
| PUT    | /users/{user_id}   | Update user details by ID    | Yes           |
| DELETE | /users/{user_id}   | Delete a user                | Yes           |
| POST   | /auth/login        | User login                   | No            |
| POST   | /auth/register     | User registration             | No            |

## Docker Usage
To build and run the application using Docker, execute:
```bash
# Build the Docker image
docker build -t user-management-demo .

# Run the Docker container
docker run -d -p 8000:8000 user-management-demo
```

## Environment Variables
You may configure the following environment variables:
- `DATABASE_URL`: The connection string for the SQLite database.
- `SECRET_KEY`: A secret key for JWT token generation. Make sure to set this to a secure value.

This README provides a comprehensive overview of the User Management application and its features. For further assistance, consult the documentation or reach out to the maintainers.