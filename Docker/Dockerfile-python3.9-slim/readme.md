# Full Workflow

## Demo Program
1. Create Environment

```python
#Create folder
mkdir docker_demo

#REM Create virtual environment with Python 3.9
##This create a local folder envhouse in this folder
python -m venv envhouse
 

#REM Activate the virtual environment
envhouse\Scripts\activate

#REM Install required packages
pip install pandas numpy streamlit flask

```


2. Create print_numbers.py Script:

```python
   def print_numbers():
       for i in range(1, 11):
           print(i)

   if __name__ == "__main__":
       print_numbers()
```

3. Create readme.md file

``` python
# This is Docker demo Main Heading
## This is Subheading.
```

## Create Docker Image

4. **Create `Dockerfile`:**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY print_numbers.py /
   copy readme.md /
   CMD ["python", "print_numbers.py"]
   ```

5. **Log in to Docker Hub (if not already logged in):**
   Ensure you are logged in to Docker Hub on your machine.

   ```sh
   docker login
   ```

   Enter your Docker Hub credentials when prompted.
   
6. **Build and Tag the Docker Image:**
   ```sh
   docker build -t harithapliyal/print_numbers:may2024 .
   ```

7. **Verify Local Image:**
   ```sh
   docker images
   ```

   Example output:
   ```
   REPOSITORY                     TAG        IMAGE ID       CREATED          SIZE
   harithapliyal/print_numbers    may2024    abcdef123456   2 minutes ago    123MB
   ```

8. **Push the Docker Image:**
   ```sh
   docker push harithapliyal/print_numbers:may2024
   ```

## Download the Image and run on local machine 

To download and use the Docker image you've pushed to Docker Hub on another machine, follow these steps:

1. **Log in to Docker Hub (if not already logged in):**
   Ensure you are logged in to Docker Hub on your machine.

   ```sh
   docker login
   ```

   Enter your Docker Hub credentials when prompted.

2. **Pull the Docker Image:**
   Download the Docker image from Docker Hub to your local machine.

   ```sh
   docker pull harithapliyal/print_numbers:may2024
   ```

3. **Run the Docker Image:**
   Once the image is downloaded, you can run it.

   ```sh
   docker run --rm harithapliyal/print_numbers:may2024

   ```If you need to interact with the container, such as running commands inside it, you can start it in an interactive mode:

   docker run -it harithapliyal/print_numbers:may2024 /bin/bash

   ```

   The `--rm` flag ensures that the container is removed after it stops. This helps in keeping your system clean.
   
   '### Verification

To verify that everything is working correctly, you should see the output of the print_numbers.py script:

```
1
2
3
4
5
6
7
8
9
10
```

## Docker Compose

1. Create docker.compose 
```python
#Create docker-compose.yml File:
version: '3.8'

services:
  house_price_app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DEBIAN_FRONTEND=noninteractive

```

2. Make sure your Dockerfile is in the same directory as your docker-compose.yml file and is using the correct format:

```python
# Use the official Python image with Python 3.9
FROM python:3.9-slim

# Set the environment variable to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Upgrade pip and install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

# Add the application code and other necessary files
COPY ./app.py /
COPY ./kc_house_data.csv /
COPY ./model_houseprice.pkl /
COPY ./config.json /

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python3", "-u", "./app.py"]

```

3. Build and Run with Docker Compose:

Use Docker Compose to build and run your application:

```
docker-compose up --builddocker-compose up --build
```

4. Running the Application:
After running docker-compose up --build, Docker Compose will build the image and start the container. You can access your Flask app at http://localhost:5000

If you want to run the containers in the background (detached mode), you can use:

docker-compose up --build -d 


## Docker Compose vs Docker Build 

Docker Compose and the `docker build` command serve different purposes and are used in different contexts when working with Docker.

### Docker Compose

**Docker Compose** is a tool for defining and running multi-container Docker applications. With Docker Compose, you can use a YAML file to configure your application’s services. Then, with a single command, you can create and start all the services from your configuration.

**Key Features and Uses:**

1. **Multi-Container Applications**: Docker Compose is designed to handle applications that require multiple containers working together. For example, a web app with a database, a web server, and a cache service.
2. **Configuration File**: Uses a `docker-compose.yml` file to define the services, networks, and volumes.
3. **Simplified Commands**: Use simple commands like `docker-compose up` and `docker-compose down` to manage the entire application stack.
4. **Networking**: Automatically sets up networking between containers defined in the `docker-compose.yml` file.
5. **Environment Variables**: Easily manage environment variables for different services.

**Example `docker-compose.yml`:**

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  db:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: example
```

### docker build

**`docker build`** is a command used to build an image from a Dockerfile. The Dockerfile contains a series of instructions on how to create the Docker image, including which base image to use, which dependencies to install, and how to configure the application inside the container.

**Key Features and Uses:**

1. **Build Images**: The primary purpose of `docker build` is to create Docker images from a Dockerfile.
2. **Dockerfile**: Requires a `Dockerfile` that contains all the steps needed to create the image.
3. **Custom Tags**: You can tag the image using the `-t` flag to specify a custom name and version.

**Example Command:**

```sh
docker build -t myapp:latest .
```

This command tells Docker to build an image from the Dockerfile in the current directory and tag it as `myapp:latest`.

### Differences

1. **Purpose**:
   - **Docker Compose**: Manages multi-container applications, setting up networks, volumes, and dependencies between services.
   - **`docker build`**: Builds a single Docker image from a Dockerfile.

2. **Configuration**:
   - **Docker Compose**: Uses a `docker-compose.yml` file to define services, networks, and volumes.
   - **`docker build`**: Uses a `Dockerfile` to define how to build a single image.

3. **Usage**:
   - **Docker Compose**: Suitable for orchestrating complex applications with multiple interconnected containers.
   - **`docker build`**: Suitable for building individual Docker images, which can then be run or managed separately.

4. **Commands**:
   - **Docker Compose**:
     - `docker-compose up`: Builds, (re)creates, starts, and attaches to containers for a service.
     - `docker-compose down`: Stops and removes containers, networks, volumes, and images created by `up`.
   - **`docker build`**:
     - `docker build`: Creates a Docker image from a Dockerfile.

In summary, Docker Compose is a higher-level tool that uses `docker build` under the hood to create images but extends the functionality to define and run multi-container Docker applications in a simple and effective way.







   
   
   
   
   