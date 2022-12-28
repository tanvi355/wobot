# wobot
Wobot Task 


## To-Do List API

- Built using FastAPI framework + MySQL database
- REST API
- CRUD functionalities
- `main.py`: contains all the operations to be performed (GET, POST, PUT, DELETE requests)
- `database.py`: connecting to the database
- `models.py`: contains the database models defined for the tasks and users
- `schemas.py`: contains the schemas for creating and displaying the entities

## Learnings

- Learnt how to work with FastAPI as this was my first time using it.

## How to use the API?

- Download the code or fork and clone this repository.
- Run the app using the command `uvicorn main:app --reload`
- You can test the API using Postman or inbuilt Swagger UI by providing the appropriate input based on the schema of the operation to be performed.
