from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Define the FastAPI app
app = FastAPI()

# Mount static files if you have any static directory
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Define a sample route
@app.get("/")
async def read_root():
    #return {"message": "Hello, FastAPI!"}
    return {"Hello": "I am not the Local World!"}

from transformers import pipeline

pipe_flan = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/infer_t5")
def t5(input):
    output = pipe_flan(input)
    return {"output": output[0]["generated_text"]}
   