
## Setup & Test
pip install fastapi uvicorn   
pip install python-multipart   

test in browser: http://127.0.0.1:8000/docs   

## GET Request
curl "http://127.0.0.1:8000/get-example?param1=value1&param2=value2"

> Ouput: {"param1":"value1","param2":"value2"}

## POST Request
curl -X POST "http://127.0.0.1:8000/post-example" -H "Content-Type: application/json" -d "{\"key1\": \"value1\", \"key2\": \"value2\"}"

> Ouput: "received":{"key1":"value1","key2":"value2"}}

## curl -X POST "http://127.0.0.1:8000/upload" ^
-F "file=@./readme.md"       

> Ouput: {"filename":"readme.md","content_type":"application/octet-stream"}

