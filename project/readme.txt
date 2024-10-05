# Item Management API

## Overview
This project is a RESTful API for managing items, developed using Django and Django REST Framework. The API allows authenticated users to create, read, update, and delete items. Redis is used for caching item data to improve performance, and JWT (JSON Web Token) authentication is implemented for secure access.

## Features
- CRUD Operations: Create, Read, Update, Delete items.
- Caching: Redis is used to cache item data for faster retrieval.
- Authentication: JWT authentication to secure API endpoints.
- Logging: Logs all API usage and errors for monitoring.
- Unit Tests: Comprehensive tests for all endpoints to ensure API reliability.

## Table of Contents
1. Requirements
2. Installation
3. Running the Application
4. API Endpoints
5. Running Tests
6. Logging
7. Project Structure

## Requirements
- Python 3.8+
- Django 3.2+
- Django REST Framework
- Redis (for caching)
- PostgreSQL 
- Simple JWT for authentication

## Installation

1. Clone the Repository

2.  Virtual Environment:myenv\Scripts\activate

3. Install Dependencies:pip install -r requirements.txt
4. Configure the Database:-Update the DATABASES setting in settings.py to point to your PostgreSQL database or any other preferred database.
Example:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Run Migrations:python manage.py migrate
6. Set Up Redis:Ensure that Redis is running on your machine.

7. Generate JWT Tokens
Use the following endpoint to obtain JWT tokens:POST /api/token/
Add user in database:-
	python manage.py shell 
	from django.contrib.auth.models import User
	User.objects.create_user(username='testuser', password='testpass')
	exit()
 hit url to get token in cmd :curl -X POST http://localhost:8000/api/token/ -d "username=testuser&password=testpass"

Running the Application
Start the Django development server:
python manage.py runserver
API Endpoints
Authenticated Endpoints (JWT Token Required)

Create Item
URL: /items/
Method: POST
Description: Creates a new item.
Request Body:
json

{
  "Name": "item1",
  "Description": "Test item",
  "Quantity": 10
}

Response:
json

{
  "id": 1,
  "Name": "item1",
  "Description": "Test item",
  "Quantity": 10
}
Read Item

URL: /items/<int:item_id>/
Method: GET
Description: Retrieves the details of a single item.
Response:
json

{
  "id": 1,
  "Name": "item1",
  "Description": "Test item",
  "Quantity": 10
}
Update Item

URL: /items/<int:item_id>/
Method: PUT
Description: Updates the details of an existing item.
Request Body:
json

{
  "Name": "item1",
  "Description": "Updated description",
  "Quantity": 20
}
Delete Item

URL: /items/<int:item_id>/
Method: DELETE
Description: Deletes an item.
Running Tests
To run the unit tests, use the following command:
python manage.py test
Logging
The application logs all API usage and errors. Logs are saved to a debug.log file.
INFO: Logs basic operations such as item creation or deletion.
ERROR: Logs any errors or exceptions that occur during API calls.
You can configure the logging in settings.py:

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    },
}



Project Structure

├── items/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project_name/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── readme.md
    debug.log
