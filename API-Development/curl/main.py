from fastapi import FastAPI, Query, Body, Header, File, UploadFile, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Example data storage
fake_db = {"item1": "value1", "item2": "value2"}


# 1. GET Request with Query Parameters
@app.get("/get-example")
def get_example(param1: str = Query(...), param2: str = Query(None)):
    return {"param1": param1, "param2": param2}


# 2. POST Request with JSON
class PostData(BaseModel):
    key1: str
    key2: str


@app.post("/post-example")
def post_example(data: PostData):
    return {"received": data.dict()}


# 3. PUT Request
@app.put("/put-example/{item_id}")
def put_example(item_id: str, data: PostData):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = data.dict()
    return {"updated_item": item_id, "data": data.dict()}


# 4. DELETE Request
@app.delete("/delete-example/{item_id}")
def delete_example(item_id: str):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"deleted_item": item_id}


# 5. File Upload
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}


# 6. Authentication
@app.get("/auth-example")
def auth_example(authorization: str = Header(None)):
    if authorization != "Bearer YOUR_API_KEY":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Authorized"}


# 7. Pagination Example
@app.get("/pagination-example")
def pagination_example(page: int = Query(1), limit: int = Query(10)):
    items = list(fake_db.keys())
    start = (page - 1) * limit
    end = start + limit
    return {"page": page, "limit": limit, "items": items[start:end]}


# 8. Debugging Example (headers and request data)
@app.get("/debug-example")
def debug_example(headers: dict = Header(None)):
    return {"headers": headers}


# 9. Redirect Example
@app.get("/redirect-example")
def redirect_example():
    return {"message": "Use curl -L to follow redirects"}


# 10. Proxy Example
@app.get("/proxy-example")
def proxy_example():
    return {"message": "This endpoint is just for testing proxies"}


# 11. HTTPS Example (SSL)
@app.get("/https-example")
def https_example():
    return {"message": "Test curl with -k to ignore SSL errors (not implemented here)"}


# 12. Parallel Requests Example
@app.get("/parallel-example/{item_id}")
def parallel_example(item_id: str):
    return {"item_id": item_id, "message": "Fetched in parallel"}