# Accessing local gpu machine and local virtual env from colab.

## create virtual env 
python -m venv .venv 
.\.venv\Scripts\Activate

## Install Jupyter on your local machine:

bash
pip install jupyter

## Install Jupyter HTTP-over-WebSocket extension:

bash
pip install jupyter_http_over_ws

jupyter server extension enable --py jupyter_http_over_ws


## Start Jupyter notebook on your local machine:
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888

## Connect Colab to the local runtime:

In Google Colab, go to Edit > Notebook settings and set the Hardware accelerator to None. Then, click on the Connect button, select Connect to local runtime, and follow the instructions to enter the local server's port (usually 8888).


## for gpu


## Download and install cuda 
https://developer.nvidia.com/cuda-downloads

## Download and install cuDNN (optional but recommended)
https://developer.nvidia.com/cudnn   
The NVIDIA CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, attention, matmul, pooling, and normalization.


## Verify CUDA Installation:
Open a new PowerShell window and run:

nvcc --version

### set env. 
$env:Path += ";C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin"

## install torch or tensorflow 

pip uninstall torch torchvision torchaudio

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

or    
pip install tensorflow-gpu

## from colab after connection
import torch   
print(torch.cuda.is_available())  # Should return True   
print(torch.cuda.device_count())  # Should return the number of GPUs available   
print(torch.cuda.get_device_name(0))  # Should return the name of the GPU   





