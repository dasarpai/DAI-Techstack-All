from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/create_user/")
def create_user(user: User):
    return {"message": f"User {user.name} with age {user.age} created!"}
