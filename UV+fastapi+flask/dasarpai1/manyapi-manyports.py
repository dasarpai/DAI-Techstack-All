from fastapi import FastAPI
import uvicorn
from multiprocessing import Process

app1 = FastAPI()
app2 = FastAPI()
app3 = FastAPI()

@app1.get("/app1")
def main1():
    return {"message": "Hello from app1"}

@app2.get("/app2")
def main2():
    return {"message": "Hello from app2"}

@app3.get("/app3")
def main3():
    return {"message": "Hello from app3"}

def run_app1():
    uvicorn.run(app1, host="localhost", port=8001)

def run_app2():
    uvicorn.run(app2, host="localhost", port=8002)

def run_app3():
    uvicorn.run(app3, host="localhost", port=8003)

if __name__ == "__main__":
    p1 = Process(target=run_app1)
    p2 = Process(target=run_app2)
    p3 = Process(target=run_app3)
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()