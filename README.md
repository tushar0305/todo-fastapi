# Todo App using FastAPI and MySQL

This is a simple implementation of a CRUD (Create, Read, Update, Delete) Todo app using FastAPI and MySQL.

## Prerequisites
* MySQL database set up and running on localhost
* Python 3.6 or higher installed
* Pipenv or virtualenv setup

## Setup
1. Clone this repository to your local machine:
```
https://github.com/tushar0305/wobot-assignment.git
```

2. Change into the repository directory:
```
cd todo-app
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Create the database and table:
```
CREATE DATABASE todo_app;

USE todo_app;

CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
```

## Running the app

1. Run the FastAPI app:
```
uvicorn main:app --reload
```

2. Access the API endpoint in your browser or via a tool such as Postman:
```
http://localhost:8000/todos
```

## Endpoints
The following endpoints are currently implemented in this Todo app:

* `POST /todos` : creates a new Todo task
* `GET /todos` : Get the list of tasks
* `PUT /todos/{task_id}` : Update the task
* `DELETE /todos{task_id}` : Delete the task
