FROM nvidia/cuda:11.8.0-base-ubuntu20.04

# Install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-tk \
    libgl1-mesa-glx

# Install Python packages
RUN pip3 install jupyterlab tensorflow torch

# Set the working directory
WORKDIR /app

# Expose the port for JupyterLab
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

