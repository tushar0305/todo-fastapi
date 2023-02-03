from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import uvicorn

app = FastAPI()

# Define the Todo model
class Todo(BaseModel):
    title: str
    description: str
    is_completed: bool

# Connect to the MySQL database
cnn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wobot"
)
cursor = cnn.cursor()

# Create the todo table
table = "CREATE TABLE IF NOT EXISTS todos (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), description TEXT, is_completed BOOLEAN)"
cursor.execute(table)

# POST endpoint to create a new todo
@app.post("/todos")
def create_todo(todo: Todo):
    query = "INSERT INTO todos (title, description, is_completed) VALUES (%s, %s, %s)"
    values = (todo.title, todo.description, todo.is_completed)
    cursor.execute(query, values)
    cnn.commit()
    return {"message": "Todo created successfully."}

# GET endpoint to retrieve a list of todos
@app.get("/todos")
def get_todos():
    query = "SELECT * FROM todos"
    cursor.execute(query)
    todos = cursor.fetchall()
    return {"todos": todos}

# PUT endpoint to update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    query = "UPDATE todos SET title = %s, description = %s, is_completed = %s WHERE id = %s"
    values = (todo.title, todo.description, todo.is_completed, todo_id)
    cursor.execute(query, values)
    cnn.commit()
    return {"message": "Todo updated successfully."}

# DELETE endpoint to delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    query = "DELETE FROM todos WHERE id = %s"
    cursor.execute(query, (todo_id,))
    cnn.commit()
    return {"message": "Todo deleted successfully."}
