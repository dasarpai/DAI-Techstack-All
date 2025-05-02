from flask import Flask

app = Flask(__name__)

@app.get("/")
def main():
    print("Hello from app. This msg will be printed on the server console")
    return {
        "message": "Hello from app",
        "consoleMessage": "I am app1"
    }


if __name__ == "__main__":
    app.run(host="localhost", port=8000)