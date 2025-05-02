from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def main():
    print("Hello from app. This msg will be printed on the server console")
    return {
        "message": "Hello from app",
        "consoleMessage": "I am app1"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)