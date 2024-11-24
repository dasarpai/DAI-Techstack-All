

# Important Commands 

## Create a Dockerfile. 

## Run following commain in the same folder. It will build the image and run the container.
docker build -t my-jupyter-notebook .

## To run docker on port 8888. Load volume in /home

### from wsl shell 

#### If want to fire all gpu 
docker run -it --rm --gpus all -p 8888:8888 -v "$(pwd):/workspace" my-jupyter-notebook

#### Want to add a volue to the container 
docker run -p 8888:8888 -v ${PWD}:/home/jovyan/work -d my-jupyter-notebook
docker run -p 8081:8081 -d sorokine/docker-colab-local:latest
docker run -p 8081:8081 sorokine/docker-colab-local

#### If image does not exists
docker build -t diffusers-pytorch-cuda .

### from windows 11 shell.
docker run -it --rm --gpus all -p 8888:8888 -v "%cd%:/workspace" my-jupyter-notebook
docker run -it --rm --gpus all -p 8888:8888 -v "D:\github\Dataset:/workspace" my-jupyter-notebook

docker exec -it c09ca90b6a97 /bin/bash
python -c "import tensorflow as tf; print(tf.__version__)"

It will launch jupyter in docker and make the link available on the host machine at
http://127.0.0.1:8888/tree

## To use docker in Visual code.
ctrl+shift+p      
select kernel    
existing jypter server    
type the above generated url, along with token.

## How to access docker shell?

docker exec -it container-id-or-name /bin/bash

# Full Workflow

## Important Commands 
docker run -it ubuntu bash   


## Create Demo App
1. Create Environment

```python
#Create folder
mkdir docker_demo
cd docker_demo

#REM Create virtual environment with Python 3.9
##This create a local folder envhouse in this folder
python -m venv envdemo
 

#REM Activate the virtual environment
envdemo\Scripts\activate

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





## I have gpu enabled docker setup on my machine. I want to access this machine from colab, as a local machine.

To use your GPU-enabled Docker setup on your local machine and access it from Google Colab, you can create an SSH tunnel. This involves running an SSH server on your local machine and connecting to it from Colab. Here are the steps to achieve this:

### Step 1: Set Up an SSH Server on Your Local Machine

1. **Install an SSH Server:**

   For Windows, you can use OpenSSH:
   - Open the `Settings` app.
   - Go to `Apps` > `Optional Features`.
   - Click `Add a feature` and install `OpenSSH Server`.

   For Linux, you can install OpenSSH:
   ```sh
   sudo apt-get update
   sudo apt-get install openssh-server
   ```

2. **Start the SSH Service:**

   For Windows:
   - Open `PowerShell` as an administrator and run:
     ```sh
     Start-Service sshd
	 
	 Get-Service sshd
     ```

   - For Linux:
   ```sh
   sudo service ssh start
   
   sudo service ssh status
   ```

3. **Allow SSH Traffic Through the Firewall:**

   For Windows:
   - Open `PowerShell` as an administrator and run:
     ```sh
     New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
     ```

   For Linux:
   ```sh
   sudo ufw allow ssh
   ```
3. **Step 3: Verify SSH Server Configuration**
- Check SSH Configuration:

	Open the SSH configuration file:
	```sh
	sudo nano /etc/ssh/sshd_config

	```
	Ensure the following lines are present and not commented out:
	```bash
	Port 22
	PermitRootLogin yes
	```
4. **Start SSH Service**
	```sh
	sudo service ssh restart
	```

5: Test the SSH Connection Locally
	Before trying to connect from Colab, test the SSH connection locally to ensure it's working:

	Open a terminal or PowerShell on your local machine and run:

	```sh
	ssh your_username@localhost
	Replace your_username with your actual username.
	```

6: Create the SSH Tunnel in Google Colab
	Generate SSH Keys in Colab (if not already done):

	```python
	!ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/id_rsa -N ""
	```
	Display Your Public Key:

	```python
	!cat ~/.ssh/id_rsa.pub
	```
	Add the Public Key to Your Local Machine:   
	Copy the public key displayed by the previous command and add it to the ~/.ssh/authorized_keys file on your local machine.

	Create the SSH Tunnel in Colab:

	```python
	!ssh -o StrictHostKeyChecking=no -L 8888:localhost:8888 your_username@your_local_machine_ip
	```
	Replace your_username and your_local_machine_ip with your actual username and IP 



### Step 2: Run Your Docker Container

Start your Docker container with the necessary ports exposed. For example:

```sh
docker run -it --rm --gpus all -p 8888:8888 -v "C:\path\to\your\folder:/workspace" my-jupyter-notebook
```

### Step 3: Create an SSH Tunnel in Google Colab


***Note:***   
windows:      
command to get local_machine_ip: ipconfig    
command to get username: echo %USERNAME%

linux/wsl:    
command to get machine_name: hostname 
command to get username: whoami


1. **Generate SSH Keys:**

   In Google Colab, generate an SSH key pair if you don't have one:

   ```python
   !ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/id_rsa -N ""
   ```

2. **Copy Your Public Key to Your Local Machine:**

   Display your public key in Colab:

   ```python
   !cat ~/.ssh/id_rsa.pub
   ```

   Add the displayed public key to your local machine's `~/.ssh/authorized_keys` file.

3. **Create the SSH Tunnel:**

   In Colab, use `ssh` to create a tunnel to your local machine:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')

   !ssh -o StrictHostKeyChecking=no -L 8888:localhost:8888 your_username@your_local_machine_ip
   
   !ssh -o StrictHostKeyChecking=no -L 8888:localhost:8888 _hari@192.168.1.100

   ```

   Replace `your_username` with your local machine's username and `your_local_machine_ip` with its IP address.


### Step 4: Access Your Jupyter Notebook

Once the SSH tunnel is set up, you can access the Jupyter Notebook running on your local machine through the Colab environment. Open the Jupyter Notebook in your browser:

```sh
http://localhost:8888
```

This URL will now be forwarded to your local machine through the SSH tunnel.

### Summary

By setting up an SSH server on your local machine and creating an SSH tunnel from Colab, you can access and utilize your GPU-enabled Docker setup as if it were a local machine.
   
   
## sudo not available on your machine 
sudo apt-get update   
/bin/sh: 1: sudo: not found

The error message `/bin/sh: 1: sudo: not found` suggests that the `sudo` command is not available in your environment. This can happen in certain restricted or minimal Linux environments.

### Installing and Running SSH Without `sudo`

If you are running a minimal Linux environment where `sudo` is not installed, you may need to install `sudo` first. However, if you do not have root access to install `sudo`, you will need to perform the necessary commands as the root user directly. Here are the steps to proceed in such an environment:

### Step 1: Log in as Root
If you have root access, you can switch to the root user:

```sh
su -
```

### Step 2: Install OpenSSH Server (as root)
If you are logged in as the root user, you do not need `sudo`:

```sh
apt-get update
apt-get install openssh-server
```

### Step 3: Start the SSH Service
Again, if you are the root user, you can start the service directly:

```sh
service ssh start
```

### Step 4: Configure the SSH Server (if necessary)
Edit the SSH configuration file to ensure it's set up correctly:

```sh
nano /etc/ssh/sshd_config
```

Make sure the following lines are present and not commented out:

```
Port 22
PermitRootLogin yes
```

Restart the SSH service to apply any configuration changes:

```sh
service ssh restart
```

### Step 5: Allow SSH Traffic Through the Firewall
If your environment uses a firewall, ensure SSH traffic is allowed. For example, using UFW (Uncomplicated Firewall):

```sh
ufw allow ssh
```

### Step 6: Test the SSH Connection Locally
Before attempting to connect from Google Colab, test the SSH connection locally:

```sh
ssh your_username@localhost
```

Replace `your_username` with your actual username.

### Step 7: Connect from Google Colab
Once your SSH server is set up and running, you can create an SSH tunnel from Google Colab:

1. **Generate SSH Keys in Colab (if not already done):**
   ```python
   !ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/id_rsa -N ""
   ```

2. **Display Your Public Key:**
   ```python
   !cat ~/.ssh/id_rsa.pub
   ```

3. **Add the Public Key to Your Local Machine:**
   Copy the public key displayed by the previous command and add it to the `~/.ssh/authorized_keys` file on your local machine.

4. **Create the SSH Tunnel in Colab:**
   ```python
   !ssh -o StrictHostKeyChecking=no -L 8888:localhost:8888 your_username@your_local_machine_ip
   ```

   Replace `your_username` and `your_local_machine_ip` with your actual username and IP address.

### Summary
By following these steps, you can set up and run an SSH server in an environment without `sudo`, ensuring that you can establish an SSH connection from Google Colab to your local machine. This setup will enable you to create an SSH tunnel and access your GPU-enabled Docker setup.


## Reset the password of docker container 

To set or reset the password for a user, you need to access the Docker container directly.

The `sorokine/docker-colab-local` image might not have a password set for the default user. To set or reset the password for a user, you need to access the Docker container directly.

Here are the steps to set a password for the user `_hari`:

### Step 1: Start the Docker Container with a Shell

Run the Docker container and get a shell into it:

```sh
docker run -it --rm --name colab-container sorokine/docker-colab-local /bin/bash
```

This command starts the container and opens a Bash shell.

### Step 2: Set a Password for the User

Inside the container, set a password for the `_hari` user (or the appropriate user if it's different):

```sh
passwd _hari
```

You will be prompted to enter a new password. Enter the password twice to confirm it.

### Step 3: Exit the Container

After setting the password, you can exit the container by typing `exit`.

### Step 4: Restart the Container

Restart the container with the appropriate settings for SSH and Jupyter:

```sh
docker run -it --rm --gpus all -p 8888:8888 -p 22:22 -v "C:\path\to\your\folder:/workspace" sorokine/docker-colab-local
```

### Step 5: Connect from Google Colab

Use the newly set password when you SSH from Google Colab:

1. **Generate SSH Keys in Colab (if not already done):**
   ```python
   !ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/id_rsa -N ""
   ```

2. **Display Your Public Key:**
   ```python
   !cat ~/.ssh/id_rsa.pub
   ```

3. **Add the Public Key to Your Docker Container:**
   - Copy the public key displayed by the previous command.
   - Add it to the `~/.ssh/authorized_keys` file for the `_hari` user inside the Docker container. You can do this by accessing the container again:

     ```sh
     docker exec -it colab-container /bin/bash
     mkdir -p /home/_hari/.ssh
     echo "your_public_key" >> /home/_hari/.ssh/authorized_keys
     chown -R _hari:_hari /home/_hari/.ssh
     chmod 600 /home/_hari/.ssh/authorized_keys
     ```

4. **Create the SSH Tunnel in Colab:**
   ```python
   !ssh -o StrictHostKeyChecking=no -L 8888:localhost:8888 _hari@your_local_machine_ip
   ```

   Replace `_hari` and `your_local_machine_ip` with your actual username and IP address.

### Summary

By setting a password for the `_hari` user inside the Docker container, you can successfully connect via SSH from Google Colab. This setup will enable you to create an SSH tunnel and access your GPU-enabled Docker setup.


## tensorflow gpu 
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda-repo-wsl-ubuntu-12-6-local_12.6.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-12-6-local_12.6.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6


nvcc cuda version : 11.5
nvidia smi cuda: 12.5
tensorflow 


For stability and broad compatibility with various packages, you should consider the following versions for TensorFlow and PyTorch:

### **TensorFlow:**
- **TensorFlow 2.13.0**: This version is a stable release that balances new features with compatibility. It works well with CUDA 11.2, CUDA 11.8, and cuDNN 8.1, ensuring compatibility with many TensorFlow Hub models and libraries.
- **TensorFlow 2.12.0**: Another stable release that supports CUDA 11.2 and cuDNN 8.1, making it a reliable choice if you need strong compatibility with older models or codebases.

### **PyTorch:**
- **PyTorch 2.0**: The latest major release that offers improved performance and new features while supporting CUDA 11.x and CUDA 12.x. It's a good choice if you want the latest improvements and compatibility with recent libraries.
- **PyTorch 1.13.1**: A stable version with good compatibility for a wide range of projects. It supports CUDA 11.6 and cuDNN 8.1.

### **General Recommendations:**
- **TensorFlow 2.13.0** and **PyTorch 2.0**: These versions are likely to be the most compatible with recent experiments and packages from TF Hub, Hugging Face, and GitHub.
- **Check Package Documentation**: Ensure that the specific packages or models you're using are compatible with these versions by checking their documentation or repository requirements.

**Verify Compatibility:**
- **TensorFlow Compatibility:** [TensorFlow GPU Support](https://www.tensorflow.org/install/source#gpu)
- **PyTorch Compatibility:** [PyTorch CUDA Compatibility](https://pytorch.org/get-started/previous-versions/)

By choosing these versions, you should be able to ensure stability while maintaining compatibility with most experiments and packages.

# Now tell me to steps to install tensorflow 2.13.0 and ensure cuda, cuDNN and Nvidia cuda are compabable.

https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```


