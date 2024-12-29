# Readme by hari Thapliyal

## Links
- http://127.0.0.1:8000
- http://localhost:8000/docs

## For Validation with Pydantic 
#file: pp3-validation-with-pydantic.py   
#pip install fastapi[all]   
#uvicorn app4-error-handling:app   

## For Error Handling   
#file: app4_error_handling.py     
#uvicorn app4-error-handling:app   
#pip install gunicorn uvicorn[gunicorn]   

## For Production Deployment 
#uvicorn app4_error_handling:app --host 0.0.0.0 --port 8000 --workers 4   


## For Dockerization/Containerization of App 
Great choice! Docker is an excellent way to package your FastAPI app and deploy it anywhere.

### **Step 1: Create a `Dockerfile`**

The `Dockerfile` is a script that contains the instructions to build your Docker image. Let's create one for your FastAPI app.

1. In the root of your project directory (where `app4_error_handling.py` is located), create a file named `Dockerfile` (without any file extension) and add the following content:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "app4_error_handling:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **Step 2: Create a `requirements.txt` file**

Next, you need to create a `requirements.txt` file that lists all the dependencies for your project. You can generate it by running:

```bash
pip freeze > requirements.txt
```

This will generate a list of installed packages and versions, including FastAPI and Uvicorn.

### **Step 3: Build the Docker image**

Now that we have the `Dockerfile` and `requirements.txt`, we can build the Docker image. Run the following command in the terminal (from the directory where the `Dockerfile` is located):

```bash
docker build -t fastapi-example .
```

This will build the Docker image and tag it as `fastapi-example`.

### **Step 4: Run the Docker container**

Once the image is built, you can run it as a container:

```bash
docker run -d -p 8000:8000 fastapi-example
```

- `-d` runs the container in detached mode (in the background).
- `-p 8000:8000` binds port 8000 on your machine to port 8000 in the container.

You can check if your container is running by visiting:

```
http://127.0.0.1:8000
```

### **Step 5: Test the Dockerized app**

If everything worked, you should now be able to access your FastAPI app just like before, but it's now running inside a Docker container!

### **Step 6: (Optional) Push to Docker Hub**

If you want to share your image or deploy it on a server, you can push it to Docker Hub. Here are the steps:

1. Log in to Docker Hub (if you don't have an account, you can create one on [Docker Hub](https://hub.docker.com/)):

```bash
docker login
```

2. Tag your image:

```bash
docker tag fastapi-example <your-dockerhub-username>/fastapi-example:latest
```

3. Push the image:

```bash
docker push <your-dockerhub-username>/fastapi-example:latest
```

This will upload the image to Docker Hub, and you can pull it from anywhere and run it.

### Pull and Run in future or on some other machine
```
docker pull harithapliyal/fastapi-example

docker run -d -p 8000:8000 fastapi-example
```