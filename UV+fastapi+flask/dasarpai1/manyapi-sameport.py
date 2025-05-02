from fastapi import FastAPI
import uvicorn

# Create the main app
app = FastAPI()

# Create the sub-apps
app1 = FastAPI()
app2 = FastAPI()
app3 = FastAPI()

# Define routes for each sub-app
@app1.get("/")
def main1():
    return {"message": "Hello from app1"}

@app2.get("/")
def main2():
    return {"message": "Hello from app2"}

@app3.get("/")
def main3():
    return {"message": "Hello from app3"}

# Mount the sub-apps
app.mount("/app1", app1)
app.mount("/app2", app2)
app.mount("/app3", app3)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)