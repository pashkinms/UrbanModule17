from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
    
class CreateTask(BaseModel):
    title: str
    content: str
    ptiority: int
    
class UpdateTask(BaseModel):
    title: str
    content: str
    ptiority: int