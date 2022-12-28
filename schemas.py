from pydantic import BaseModel, EmailStr
from typing import Optional

# schema for adding a new user
class userAddSchema(BaseModel):
    username: str
    email: str
    password: str

# schema for user login
class userSchema(BaseModel):
    email: str
    password: str

# schema for displaying the task list
class todoDisplaySchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    complete: Optional[bool]

    class Config:
        orm_mode = True

# schema for adding a new task
class todoAddSchema(BaseModel):
    title: str
    content: str
    complete: bool
