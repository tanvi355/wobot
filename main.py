from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from database import Base, SessionLocal, engine
from models import todoModel, userModel
from sqlalchemy.orm import Session
from typing import List
from schemas import todoDisplaySchema, todoAddSchema, userAddSchema, userSchema

Base.metadata.create_all(bind=engine)

app = FastAPI(title='To-Do List')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# home page
@app.get('/')
async def home():
    return "To-Do List API (FastAPI + MySQL)"


#-------------------------user operations-----------------------------------

# user signup using username, email and password
@app.post('/signup', response_class=JSONResponse)
async def signup(user_details:userAddSchema, db:Session=Depends(get_db)):
    # check if user already exists
    email_exists = db.query(userModel).filter(userModel.email == user_details.email).first()
    username_exists = db.query(userModel).filter(userModel.username == user_details.username).first()
    if email_exists or username_exists:
        raise HTTPException(status_code=409, detail="User already exists")

    # provide required user details and add new user
    user_details = userModel(username=user_details.username, email=user_details.email, password=user_details.password)
    db.add(user_details)
    db.commit()
    return f"User created successfully"

# user login using email and password
@app.post('/login', response_class=JSONResponse)
async def login(user_info:userSchema, db:Session=Depends(get_db)):
    # if user exists and details provided are correct
    try:
        email_exists = db.query(userModel).filter(userModel.email == user_info.email).first()
        password_exists = db.query(userModel).filter(userModel.password == user_info.password).first()
        if email_exists and password_exists:
            return {f"User logged in":True}
    except:
        raise HTTPException(status_code=404, detail="wrong email or password, please try again or signup")


#-------------------------to-do list operations---------------------------------

# Create
# add a task to the list-- will display the task details after adding it
@app.post('/add_task', response_model=todoDisplaySchema)
async def add_tasks(todo_task:todoAddSchema, db:Session=Depends(get_db)):
    # provide required parameters of a task
    todo_task = todoModel(title=todo_task.title, content=todo_task.content, complete=todo_task.complete)
    db.add(todo_task)
    db.commit()
    return todo_task

# Read
# display all the items in the to-do list
@app.get('/list_tasks', response_model=List[todoDisplaySchema])
async def get_tasks(db: Session=Depends(get_db)):
    return db.query(todoModel).all()

# Update
# update a task in the list -- will display the task details after updating
@app.put('/update_task/{task_id}', response_model=todoDisplaySchema)
async def update_task(task_id:int, task:todoDisplaySchema, db:Session=Depends(get_db)):
    # check if task exists in the table
    try:
        task_to_update = db.query(todoModel).filter(todoModel.id == task_id).first()
        # update the task with the new details
        task_to_update.title=task.title
        task_to_update.content=task.content
        task_to_update.complete=task.complete
        db.add(task_to_update)
        db.commit()
        return task_to_update
    # if task does not exist in the table
    except:
        raise HTTPException(status_code=404, detail="task does not exist")


# Delete
# delete a task of given id from the list
@app.delete('/delete_task/{task_id}', response_class=JSONResponse)
async def delete_task(task_id:int, db:Session=Depends(get_db)):
    # check if task exists in the table
    try:
        task_to_delete = db.query(todoModel).filter(todoModel.id == task_id).first()
        db.delete(task_to_delete)
        db.commit()
        return {f"task of id {task_id} has been deleted successfully":True}
    # if task does not exist in the table
    except:
        return HTTPException(status_code=404, detail="task does not exist")
