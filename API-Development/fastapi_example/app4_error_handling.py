# uvicorn app4-error-handling:app
# pip install gunicorn uvicorn[gunicorn]
# uvicorn app4_error_handling:app --host 0.0.0.0 --port 8000 --workers 4

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet_user(name: str):
    logger.info(f"Greet endpoint accessed with name: {name}")
    return {"message": f"Hello, {name}!"}
