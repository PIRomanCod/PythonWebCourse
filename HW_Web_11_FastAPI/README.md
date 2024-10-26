# HW_Web_11_RestAPI
The REST API for storing and managing contacts. 
The API build using the FastAPI infrastructure and use SQLAlchemy for database management.

# Contacts stored in the database and contain the following information:
-First Name
-Last Name
-E-mail address
-Phone number
-Birthday
-Favorite flag
-Additional data (optional)


# The API able to do the following:
-Create a new contact
-Get a list of all contacts
-Get one contact per ID
-Update an existing contact
-Patch favorite flag
-Delete contact

# In addition to the basic CRUD functionality, the API also have the following features:
-Contacts can be searchable by name, surname, phone or email address.
-The API able to retrieve a list of contacts with birthdays for the next {shift} days.
-The API has middlewares for: performance measuring, errors_handling
-The API has events for change favorite flag before insert or change contact, related with first name
-The APi has a template for visualisation of API (only model without implementation)


# general requirements:
-Used the FastAPI framework to create API
-Used ORM SQLAlchemy to work with the database
-PostgreSQL used as a database.
-Provide API documentation
-Used the Pydantic data validation module

# Start
- upload docker -> postgres
- uvicorn main:app --host localhost --port 8000 --reload  -> start application 
- http://127.0.0.1:8000/docs -> Swagger documentation
- http://127.0.0.1:8000/redoc -> Redoc documentation
- http://127.0.0.1:8000/ -> template