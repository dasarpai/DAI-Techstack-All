# Base image from NVIDIA with CUDA support
FROM nvidia/cuda:12.6.1-cudnn-devel-ubuntu22.04

     
# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Git
RUN apt-get update && apt-get install -y git

# Install PyTorch with CUDA support
#RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

RUN pip install jupyter

# Set up default command
CMD ["python3"]

WORKDIR /home/project
