from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/greet/{name}")
def greet_user(name: str, greeting: str = "Hello"):
    return {"message": f"{greeting}, {name}!"}
