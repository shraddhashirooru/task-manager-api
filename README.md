# <p align="center">Task Manager API</p>

A Task Management REST API built with FastAPI and PostgreSQL. Users can create, read, update, and delete tasks, with authentication using JWT tokens.

## Features

- User registration and authentication

- Create, read, update, delete (CRUD) tasks

- JWT-based authentication

- Each user can manage their own tasks

- Task status tracking

- Automatic timestamps for task creation and updates

## Authentication & Security

- Users sign up with a username, email, and password.
  
- Passwords are hashed using bcrypt before being stored in the database to ensure security.
  
- Click the Authorize button in Swagger UI using username and password, FastAPI automatically calls the /login endpoint, gets the JWT token, and stores it in Swagger UI.
  
- Then, any request to protected endpoints automatically includes that token in the Authorization header.
  
- Users remain authorized and can manage tasks until the token expires.
  
- This ensures that only the task owner can manage their tasks, keeping data secure and private.

## Tech Stack

- Backend: Python, FastAPI

- Database: PostgreSQL, SQLAlchemy ORM

- Authentication: JWT (python-jose)

- Environment Management: python-dotenv

- Password Hashing: passlib

 ## Installation

### Clone the repository: 
```
git clone https://github.com/shraddhashirooru/task-manager-api.git
cd task-manager-api
```
### Create a virtual environment and activate it:
```
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```
### Install dependencies:
```
pip install -r requirements.txt
```
### Create a .env file with your database and secret key configuration:
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=YourPassword
SECRET_KEY=YourSecretKey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### Run the FastAPI server:
```
uvicorn app.main:app --reload
```
---
## API Endpoints
<img width="1167" height="768" alt="TaskAppImage" src="https://github.com/user-attachments/assets/b33547d0-15b5-40b7-b414-aa1fd655e08b" />

### Authentication 

- ``` POST /login ``` - Login to get JWT token
### Users

- ```POST /users/signup``` - Register new user

- ```GET /users/``` - Get all users

- ```GET /users/{id}``` - Get a single user

- ```PUT /users/{id}``` - Update a user

- ```DELETE /users/{id}``` - Delete a user

### Tasks

- ```POST /tasks/``` - Create task

- ```GET /tasks/``` - Get all tasks for logged-in user

- ```GET /tasks/{id}``` - Get a single task

- ```PUT /tasks/{id}``` - Update a task

- ```DELETE /tasks/{id}``` - Delete a task

### Usage

Use Swagger UI: http://localhost:8000/docs

Use JWT token received from login for authenticated routes.
