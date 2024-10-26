# HW_Web_12_JWT for RestAPI
In this homework, we continue to refine our REST API application from homework 11.

# Implemented required tasks:
- implemented an authentication mechanism in the application;
- Implemented an authorization mechanism using JWT tokens 
so that all operations with contacts are performed only by registered users;
- The user has access only to his transactions with contacts;

# Implemented additional tasks:
- for allowed operation  by privileges added next roles: user, moderator, admin;
- implemented  CORS Middleware for connecting to Client by API;


# general requirements
- When registering, if a user already exists with such an email, the server will return an HTTP 409 Conflict error;
- The server hashes the password and does not store it openly in the database;
- In case of successful user registration, the server should return the HTTP response status 201 Created and the new user's data;
- For all POST operations to create a new resource, the server returns a status of 201 Created;
- During the POST operation - user authentication, 
the server accepts a request with user data (email, password) in the body of the request;
- If the user does not exist or the password does not match, an HTTP 401 Unauthorized error is returned;
- the authorization mechanism using JWT tokens is implemented by 
a pair of tokens: the access token access_token and the update token refresh_token;



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