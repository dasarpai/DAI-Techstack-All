# 18-Mar-22

- Docker - Container - Kubernetics
- Scalable Application
- Download installer
- Run Installer
- Error - Resolve Error / Successful
- Configuration.
- redis.io/download.
- www.docker.com - signup.
	- Get started.
	- Docker Desktop. - Download
	- Installer Docker.
	- Start Docker. - Blue color 
	- docker version.
- client/ server detail.
- docker run redis
- docker rmi redis => remove image.
- docker rmi hello-world 
- docker run redis (very easy installation.
- docker ecosystem
	- docker client, docker server, docker hob, docker images, docker machine, docker compose.
- docker run hello-world.
- command->docker client->docker server-> docker local image cash-> docker hub.
- mongoDB / WebBrowser / Hello-World => Kernel => Memory/CPU/Newtork/HDD
- Namespace (create seprate space using memory/cpu/hw etc for each app) and CGroup (control group gives persmission). File in one namesapce even on the same machine cannot be seen by other namespace.
- when docker is download 
- it download linux virutal machine.
- docker runs inside a VM
- what is image = snapshot of filesystem (Redis other libs) with startup commands commands (run redis)
- what is container? => if you run the image it creates a container. During this time image is put into cache or memory of your machine.
- docker run busybox ping google.com
- docker ps (shows running conainters)
- you can run one image in multiple containers.
- docker ps -a
- docker start b2f888b2f3bbb (just few character of docker id)
- docker kill b2f888b2f3bbb
- docker system prune
- to go inside the container.
- docker exec -it containerid sh
	- commands like ls will work
- Our Docker Subscription Service Agreement include a change to the terms of use for Docker Desktop.
- It remains free for small businesses (fewer than 250 employees AND less than $10 million in annual revenue), personal use, education, and non-commercial open source projects.
- It requires a paid subscription for professional use in larger enterprise
- docker.com/get-started 
- downloaded docker image from docker hub 
- create container.
- To create image we docker file.
- create docker file-> docker client -> docker server -> 
- docker file contains: base image, dependency conf, and startup command.
- vi Dockerfile
	- FROM alpine
	- RUN apk add --update redis 
	- CMd ["redis-server"]
- To build a docker Image. from the directory where above file is kept.
- docker build .
```
	[+] Building 6.9s (6/6) FINISHED
	 => [internal] load build definition from Dockerfile                        0.1s
	 => => transferring dockerfile: 98B                                         0.0s
	 => [internal] load .dockerignore                                           0.0s
	 => => transferring context: 2B                                             0.0s
	 => [internal] load metadata for docker.io/library/alpine:latest            4.2s
	 => [1/2] FROM docker.io/library/alpine@sha256:21a3deaa0d32a8057914f36584b  0.0s
	 => => resolve docker.io/library/alpine@sha256:21a3deaa0d32a8057914f36584b  0.0s
	 => => sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380 1.64kB / 1.64kB  0.0s
	 => => sha256:e7d88de73db3d3fd9b2d63aa7f447a10fd0220b7cbf39803 528B / 528B  0.0s
	 => => sha256:c059bfaa849c4d8e4aecaeb3a10c2d9b3d85f5165c66 1.47kB / 1.47kB  0.0s
	 => CACHED [2/2] RUN apk add --update redis                                 0.0s
	 => exporting to image                                                      0.0s
	 => => exporting layers                                                     0.0s
	 => => writing image sha256:f0ed2fd4b8d78765c77da57b18dd9a1000ab0d13f1c91d  0.0s
```
- docker build . (alpine image download, creating a temp container, open the new container from newly create, download redis, install redis, removing interim container, create one more container, build image.) 
- docker run f0ed2fd4b8d78
- docker run -t mytag-isHari/myredis:latest .
	- id = mytag-isHari
	- myredis = image namesapce
	- latest = version number


# 29-Jul-22
heroku is a salesforce company 

https://www.youtube.com/c/DockerIo
1. http://localhost/tutorial/our-application/
2. download http://localhost/assets/app.zip
3. open in visual studio 
4. create Docerfile
5. copy this content into a file Dockerfile (filename without extension)
```
	FROM node:12-alpine
	# Adding build tools to make yarn install work on Apple silicon / arm64 machines
	RUN apk add --no-cache python2 g++ make
	WORKDIR /app
	COPY . .
	RUN yarn install --production
	CMD ["node", "src/index.js"]
```
6. docker build -t getting-started .  ##Build a docker. This command used the Dockerfile to build a new container image. 
7. docker run -dp 3000:3000 getting-started ## Run a docker image.


# Usage:  docker [OPTIONS] COMMAND
```
A self-sufficient runtime for containers
Options:
      --config string      Location of client config files (default
                           "C:\\Users\\admin\\.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "C:\\Users\\admin\\.docker\\ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "C:\\Users\\admin\\.docker\\cert.pem")
      --tlskey string      Path to TLS key file (default
                           "C:\\Users\\admin\\.docker\\key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.7.1)
  compose*    Docker Compose (Docker Inc., v2.2.3)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  scan*       Docker Scan (Docker Inc., v0.17.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/
```

- docker build --tag hello-world . (Build Image)
```
	[+] Building 3.6s (11/11) FINISHED
	 => [internal] load build definition from Dockerfile                                                                                                               0.0s
	 => => transferring dockerfile: 266B                                                                                                                               0.0s
	 => [internal] load .dockerignore                                                                                                                                  0.0s
	 => => transferring context: 2B                                                                                                                                    0.0s
	 => [internal] load metadata for docker.io/library/node:12-alpine                                                                                                  3.3s
	 => [auth] library/node:pull token for registry-1.docker.io                                                                                                        0.0s
	 => [1/5] FROM docker.io/library/node:12-alpine@sha256:d4b15b3d48f42059a15bd659be60afe21762aae9d6cbea6f124440895c27db68                                            0.0s
	 => [internal] load build context                                                                                                                                  0.1s
	 => => transferring context: 2.49kB                                                                                                                                0.0s
	 => CACHED [2/5] RUN apk add --no-cache python2 g++ make                                                                                                           0.0s
	 => CACHED [3/5] WORKDIR /app                                                                                                                                      0.0s
	 => CACHED [4/5] COPY . .                                                                                                                                          0.0s
	 => CACHED [5/5] RUN yarn install --production                                                                                                                     0.0s
	 => exporting to image                                                                                                                                             0.0s
	 => => exporting layers                                                                                                                                            0.0s
	 => => writing image sha256:49e83b13987a83f2cdf4e253fe5fd8685c0bea1faa9b81f62415a50edbb4c7f1                                                                       0.0s
	 => => naming to docker.io/library/hello-world                                                                                                                     0.0s
```
- docker ps 
```
	docker ps -a
	container id 
	Image 
	Command 
	Created 
	Status 
	Ports 
	Names 
```

remove image 
docker rmi imageid

docker run imageid 

# OpenStack
https://www.openstack.org/

- OpenStack: The Most Widely Deployed Open Source Cloud Software in the World
- Deployed by thousands. Proven production at scale. OpenStack is a set of software components that provide common services for cloud infrastructure.
- Cloud Infrastructure for Virtual Machines, Bare Metal, and Containers
- Openstack controls large pools of compute, storage, and networking resources, all managed through APIs or a dashboard.
- Beyond standard infrastructure-as-a-service functionality, additional components provide orchestration, fault management and service management amongst other services to ensure high availability of user applications.
- OpenStack is an open source platform that uses pooled virtual resources to build and manage private and public clouds.
- The tools that comprise the OpenStack platform, called "projects," handle the core cloud-computing services of compute, networking, storage, identity, and image services. 
- More than a dozen optional projects can also be bundled together to create unique, deployable clouds.
- In virtualization, resources such as storage, CPU, and RAM are abstracted from a variety of vendor-specific programs and split by a hypervisor before being distributed as needed.
- OpenStack uses a consistent set of application programming interfaces (APIs) to abstract those virtual resources 1 step further into discrete pools used to power standard cloud computing tools that administrators and users interact with directly.
- Efficient, Agile and Scalable.
- https://www.redhat.com/en/topics/openstack
- OS level virtualization is called containerization : one instance of OS can have many container running. Process Isolation. Library, script, code within container. 
- Namespace allwos that each instance of container has its own OS. 
- Cgroup are responsible for monitoring and metering resources so that container remains within the limit.
- HW level virtualization is called VM. Full System virtualization (Type I Hypervization) : Out of one hardware machine you can create multiple machine.
- Typer I Hypervisor - Creating different machine.  This on top of hardware.
- Typer 2 Hypervisor - Virtualbox or Parallel (it is light weight, flexible hypervisor)
- Portability is easy in OS level virtualization. It can be put in a single file, Dockerfile. Here you can write how to build the container, how to run container, what lib are necessary, steps required to build container. We can create this file put at one place and create as much virtualization as needed, without any problem. Infinite portability. Take this dockerfile, run on our machine and spin our application. Generally there is no hardware limitation for this. Portability of the container.
- VM is isolation of machines, while Containers is isolation of processes
- The level at which virtualization happens - virtualization happens at hardware level vs. OS level
- The type of isolation achieved - isolation of machines vs. isolation of processes
- How resources are accessed - via hypervisor vs. via kernel features such as namespace and cgroups
- Flexibility of hardware vs. portability
- Memory, IO, Process and Disk required to run the program.
- compute, storage, network resource provisioning. Can indedently scaling without intervetion.
- containers are effectively virtualization
- Technology like docker is doing same thing which java did for programming lanaguage. You write once and use the class file any where. You create a machine image and put it anywhere.
- OpenStack is essentially a series of commands known as scripts. Those scripts are bundled into packages called projects that relay tasks that create cloud environments.
- OpenStack itself doesn't virtualize resources, but rather uses them to build clouds. OpenStack also doesn’t execute commands, but rather relays them to the base OS. All 3 technologies—OpenStack, virtualization, and the base OS—must work together.



# Docker  
- https://docs.docker.com/desktop/
- https://docs.docker.com/get-started/04_sharing_app/
- Docker provides a simple interface that enables you to manage your containers, applications, and images directly from your machine without having to use the CLI to perform core actions. Docker Desktop includes:
	- Docker Engine
	- Docker CLI client
	- Docker Compose
	- Docker Content Trust
	- Kubernetes
	- Credential Helper
- https://hub.docker.com/
- Access the world’s largest library of container images
- push container images to a repo on docker hub.

### What will you learn in this module?
The Python getting started guide teaches you how to create a containerized Python application using Docker. In this guide, you’ll learn how to:
- Create a sample Python application
- Create a new Dockerfile which contains instructions required to build a Python image
- Build an image and run the newly built image as a container
- Set up volumes and networking
- Orchestrate containers using Compose
- Use containers for development
- Configure a CI/CD pipeline for your application using GitHub Actions
- Deploy your application to the cloud
- After completing the Python getting started modules, you should be able to containerize your own Python application based on the examples and instructions provided in this guide.
- This page contains step-by-step instructions on how to get started with Docker. In this tutorial, you’ll learn how to:
	- Build and run an image as a container
	- Share images using Docker Hub
	- Deploy Docker applications using multiple containers with a database
- Run applications using Docker Compose
- Install :  https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64
	- $  docker run -d -p 80:80 docker/getting-started
	- -d - Run the container in detached mode (in the background).
	- docker/getting-started - Specify the image to use.
	- For example, specify -p 3000:80 and then access the tutorial via a web browser at http://localhost:3000
- Download application - https://github.com/docker/getting-started/archive/refs/heads/master.zip
- Content of Dockerfile 
```
	# syntax=docker/dockerfile:1
	FROM node:12-alpine
	RUN apk add --no-cache python2 g++ make
	WORKDIR /app
	COPY . .
	RUN yarn install --production
	CMD ["node", "src/index.js"]
	EXPOSE 3000
```
- $ docker build -t getting-started .
- $ docker run -dp 3000:3000 getting-started
- $ docker ps
- $ docker stop <the-container-id>
- $ docker rm <the-container-id>
- $ docker login -u YOUR-USER-NAME. => docker login -u harithapliyal => Sim@12.
- $ docker tag getting-started YOUR-USER-NAME/getting-started => docker tag getting-started harithapliyal/getting-started 
- $ docker push docker/getting-started => docker push harithapliyal/getting-started
- The push refers to repository [docker.io/docker/getting-started]
- An image does not exist locally with the tag: docker/getting-started
- Run the image on a new instance
	- https://labs.play-with-docker.com/
	- docker run -dp 3000:3000 YOUR-USER-NAME/getting-started => docker run -dp 3000:3000 harithapliyal/getting-started
- https://training.play-with-docker.com/
- https://training.play-with-docker.com/alacart/
- https://hub.docker.com/r/harithapliyal/getting-started
- docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"
- docker run -it ubuntu ls /
- docker exec <container-id> cat /data.txt
- docker rm -f \<container-id\>

# Container volumes
With the previous experiment, we saw that each container starts from the image definition each time it starts. While containers can create, update, and delete files, those changes are lost when the container is removed and all changes are isolated to that container. With volumes, we can change all of this.
- docker volume create todo-db
- docker rm -f <id>
- docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started
- docker ps
- docker rm -f <id>
- starting container again. with the same command.
- docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started

# where data is kept in the volume 
- docker volume inspect todo-db

# Start a dev-mode container
- Run this in powershell.
- docker run -dp 3000:3000 -w /app -v "$(pwd):/app" node:12-alpine sh -c "yarn install && yarn run dev"
- docker logs -f <container-id>

# Multiple Container App 
Up to this point, we have been working with single container apps. But, we now want to add MySQL to the application stack. The following question often arises - “Where will MySQL run? Install it in the same container or run it separately?” In general, each container should do one thing and do it well. A

# Use Docker Compose
- Docker Compose is a tool that was developed to help define and share multi-container applications. With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.


# Tue, 22-Nov-22 

variation of docker image is called tag

docker build -t hello-world .

volume: for between container, for between host & container.





 