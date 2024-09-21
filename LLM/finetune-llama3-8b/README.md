# Readme : buransh
This repository contains a copy of all my POC performed in Colab, Kaggle or Any other Clound Machine Learning Infrastructure.


# Tensorflow in Docker

## Method 1 : from Docker file

### Dockerfile for tensorflow
```
FROM tensorflow/tensorflow:2.17.0-gpu

# Install Git
RUN apt-get update && apt-get install -y git

RUN pip install jupyter

WORKDIR $HOME
```

### Commands 
```
docker build -t harithapliyal/tensorflow .
 
docker run --gpus all -d -it -p 8888:8888 -v /mnt/d/github/2-Solutions/Buransh:/home/project my-tf-jupyter jupyter notebook --ip=0.0.0.0 --allow-root

# docker run --gpus all -d -it -p 8888:8888 -v /mnt/d/github/2-Solutions/Buransh:/home/project harithapliyal/my-pytorch-gpu jupyter notebook --ip=0.0.0.0 --allow-root

docker pull harithapliyal/my-pytorch-gpu

docker exec -it <container_id> /bin/bash

```

###############################

# Pytroch in Docker

https://hub.docker.com/r/pytorch/pytorch/tags?page_size=&ordering=&name=

## Method 1 : direct pull
```
#docker pull pytorch/pytorch:2.0.0-cuda11.8-cudnn8-runtime
docker pull pytorch/pytorch:2.4.1-cuda12.4-cudnn9-runtime

## This image includes: PyTorch 2.0.0, CUDA 11.8, cuDNN 8

docker run --gpus all -it pytorch/pytorch:2.0.0-cuda11.8-cudnn8-runtime
```


## Method 2 : from Docker file
### Dockerfile for pytorch 

```
## Dokerfile content 
# Base image from NVIDIA with CUDA support
#FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
FROM nvidia/cuda:12.6.1-cudnn-devel-ubuntu22.04

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Git
RUN apt-get update && apt-get install -y git

# Install PyTorch with CUDA support
#https://pytorch.org/get-started/locally/

#RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

RUN pip install jupyter

# Set up default command
CMD ["python3"]
```

### Commands to build and run
```
docker build -t my-pytorch-gpu .

docker run --gpus all -d -it -p 8888:8888 -v /mnt/d/github/2-Solutions/Buransh:/home/project my-pytorch-gpu jupyter notebook --ip=0.0.0.0 --allow-root

```

### Commands to push into dockerhub
```
docker tag sha256:5eb673021f3cba40ea harithapliyal/my-pytorch-gpu:latest

docker push harithapliyal/my-pytorch-gpu:latest
```