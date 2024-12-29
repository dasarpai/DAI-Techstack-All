#pip install fastapi[all]
#uvicorn app4-error-handling:app

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint

app = FastAPI()

class User(BaseModel):
    name: str
    age: conint(ge=18, le=100)  # Age must be between 18 and 100

@app.post("/create_user/")
def create_user(user: User):
    return {"message": f"User {user.name} with age {user.age} created!"}

@app.post("/age_check/")
def age_check(age: int):
    if age < 18 or age > 100:
        raise HTTPException(status_code=400, detail="Age must be between 18 and 100.")
    return {"message": f"Age {age} is valid!"}
    