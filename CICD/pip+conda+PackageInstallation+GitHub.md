   
# Accessing local machine from google colab    
## following setting will enable local machine's resources via locally installed jupyter.   
   
pip install jupyter      
pip install --upgrade jupyter_http_over_ws>=0.0.7      
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0   
   
### Output: This experiment is success. We can access the jupyter notebook from browser and we can use the url in colab to connect to local resources.   
   
# Docker way of Accessing    
- When colab does not give dedicated resources we need a local powerful machine.   
- But to install all the software installed on colab and keeping it updated those on the local machine is really painful.   
- For that we can use docker image of colab available on the docker hub.   
- https://research.google.com/colaboratory/local-runtimes.html   
   
## Method 1   
- For this we need    
	- to install docker on desktop   
	- pull colab-image from the docker hub   
	- run the container from this image    
	   
- Install Docker on your local machine. Note that europe-docker.pkg.dev and asia-docker.pkg.dev are alternative mirrors to us-docker.pkg.dev below. Downloads will be faster for users in those continents. The images are identical.    
- Start a runtime:   
	- docker run -p 127.0.0.1:9000:8080 us-docker.pkg.dev/colab-images/public/runtime   
- For GPU support, with NVIDIA drivers and the NVIDIA container toolkit installed, use:   
	- docker run --gpus=all -p 127.0.0.1:9000:8080 us-docker.pkg.dev/colab-images/public/runtime   
   
### Output: This method half success. We can access the gpu resouces and docker image from the colab. But this not be accessed on browser.   
   
## Method 2   
The problem with method 1 is when container is destroyed all the data will be lost. To make data persistent between conatiner created from the image we need to create volume and put the data or anything which we want to persist in the volume.   
   
In my cache minstral model take lot of time to download and it is expensive step therefore I want to keep this model in the local memory.   
   
- From the local memory I am adding this in volume   
- when container is run from the image then this volume should also be mounted.   
   
To achieve This   
- I created volume minstral-7b-instrut.    
	- #Mount the volume into a temporary container   
	- docker run -v mistral-7B-Instruct:/mnt/mistral --name temp-container busybox   
	- #Copy the extracted model files into the volume   
	- docker cp mistral-7B-Instruct-v0.3.tar temp-container:/mnt/mistral   
	- #Remove the temporary container   
	- docker rm temp-container   
	- docker exec temp-container tar -xvf /mnt/mistral/mistral-7B-Instruct-v0.3.tar -C /mnt/mistral   
   
   
- Imported model from the local memory into this volume.   
   
- docker run --gpus=all -v mistral-7B-Instruct:/mnt/mistral -p 127.0.0.1:9000:8080 us-docker.pkg.dev/colab-images/public/runtime   
   
Command above is half success (works in colabs but not in browser)   
   
docker exec -it 0edc11e396e1 /bin/bash      
cd mnt/mistral      
ls      
   
Above command shows volume is mounted along with container.      
   
docker run -it --gpus all -v mistral-7B-Instruct:/mnt/mistral       
acd730f3e861c99d3b0ebb5264e8552c3af3703e0714c6fd1be0885cbc8f3e00      
   
docker run -it --gpus all -v mistral-7B-Instruct:/mnt/mistral -p 127.0.0.1:9000:9000     
acd730f3e861c99d3b0ebb5264e8552c3af3703e0714c6fd1be0885cbc8f3e00      
   
docker run -it --gpus all -p 127.0.0.1:9000:8080 -v mistral-7B-Instruct:/mnt/mistral        
us-docker.pkg.dev/colab-images/public/runtime      
   
docker cp       
0157fc9774613f64872db6ec341667dcc97b5b3be6ab1044ae1604015333b116:/files/content/mistral-7B-Instruct-v0.3.tar aimodels:/   
   
docker cp       
0157fc9774613f64872db6ec341667dcc97b5b3be6ab1044ae1604015333b116:/files/content/mistral-7B-Instruct-v0.tar    
   
/host/path/to/file      
   
/content/mistral-7B-Instruct-v0.3.tar aimodels   
   
   
#setuptools    
python -m ensurepip --upgrade   
python -m pip install --upgrade pip setuptools wheel   
python -m pip install --upgrade pip   
   
   
# Install Package in Environment  from git   
```   
git clone https://github.com/skorch-dev/skorch.git   
cd skorch   
conda create -n skorch-env python=3.10   
conda activate skorch-env   
# install pytorch version for your system (see below)   
python -m pip install -r requirements.txt   
python -m pip install .   
   
   
git clone https://GitHub.com/gitproject   
Cd gitproject    
Python -m venv .env-myenv   
.\.env-myenv\Scripts\activate   
pip install -r requirements.txt   
python app.py   
```   
   
   
# pypi installation    
pip install magika   
   
# Running in Docker   
```   
git clone https://github.com/google/magika   
cd magika/   
docker build -t magika .   
docker run -it --rm -v \$(pwd):/magika magika -r /magika/tests_data   
```   
   
# Python Api   
```   
from magika import Magika   
>>> m = Magika()   
>>> res = m.identify_bytes(b"# Example\nThis is an example of markdown!")   
>>> print(res.output.ct_label)   
```   
   
# python command line   
magika -r tests_data/   
   
magika code.py --json   
   
   
# development setup    
We use poetry for development and packaging:   
```   
$ git clone https://github.com/google/magika   
$ cd magika/python   
$ poetry shell && poetry install   
$ magika -r ../tests_data   
```   
   
To run the tests:   
```   
$ cd magika/python   
$ poetry shell   
$ pytest tests/   
```   
   
   
## Upgrade pip and setuptools:   
pip install --upgrade pip setuptools   
   
## Install TensorFlow with Verbose Output:`   
pip install tensorflow -v   
   
## Check WSL Disk Performance:   
dd if=/dev/zero of=testfile bs=1G count=1 oflag=direct   
rm testfile   
   
   
   
# Conda    
   
## Download and Install Miniconda   
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh   
   
run installer       
bash Miniconda3-latest-Linux-x86_64.sh   
   
Restart your terminal or source the bashrc file to enable Conda:      
source ~/.bashrc   
   
   
   
## Verify cuDNN Installation   
find /usr/local/ -name '*cudnn*'   
   
## Verify CUDA Installation:   
nvcc --version   
   
## Check if the GPU is Accessible in WSL   
nvidia-smi   
   
   
## Installation,    
conda create -n tfenv-conwsl tensorflow   
conda activate tfenv-conwsl   
conda install -c conda-forge tensorflow-gpu   
   
   
   
## Reinstallation   
conda list --export > tfenv-conwsl-packages.txt   
conda remove --name tfenv-conwsl --all   
conda create --name tfenv-conwsl   
conda install --name tfenv-conwsl --file tfenv-conwsl-packages.txt   
   
   
   
   
   
## Test in Terminal:   
jupyter notebook   
   
   
conda env list      
conda info --envs   
   
conda activate tfenv-conwsl   
   
   
   
   
## Test TensorFlow GPU Utilization   
import tensorflow as tf   
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))   
   
   
# WSL    
   
##  Restart WSL    
wsl --shutdown   
   
## Linux pkg installation   
sudo apt update && sudo apt install ffmpeg   
   
## speed test    
speedtest-cli   
   
## Monitor System Resources:   
   
Check CPU, RAM, and disk usage using tools like htop or top in another terminal to ensure that the process is running and not stuck.   
   
Check Disk Activity: You can monitor disk activity using iostat or the dstat command to see if there are any bottlenecks with your disk I/O.   
   
   
## Navigate to the CUDA library folder:   
cd /usr/local/cuda/targets/x86_64-linux/lib/   
   
   
## Create symbolic links for the cuDNN libraries:   
sudo ln -sf libcudnn.so.8.9.7 libcudnn.so.8   
sudo ln -sf libcudnn_ops_train.so.8.9.7 libcudnn_ops_train.so.8   
sudo ln -sf libcudnn_adv_infer.so.8.9.7 libcudnn_adv_infer.so.8   
sudo ln -sf libcudnn_adv_train.so.8.9.7 libcudnn_adv_train.so.8   
sudo ln -sf libcudnn_cnn_train.so.8.9.7 libcudnn_cnn_train.so.8   
sudo ln -sf libcudnn_cnn_infer.so.8.9.7 libcudnn_cnn_infer.so.8   
sudo ln -sf libcudnn_ops_infer.so.8.9.7 libcudnn_ops_infer.so.8   
   
## extract a .tar.xz file using:   
tar -xvf /mnt/c/users/hari_/Downloads/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz   
   
-x stands for extract.   
-v is for verbose (optional, to show progress).   
-f specifies the filename.   
   
tar -xzvf cudnn-11.2-linux-x64-v8.1.<exact-version>.tgz   
   
   
   
# window 1   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ source tfenv-wsl/bin/activate   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ htop   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ htop   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ iost   
Command 'iost' not found, did you mean:   
  command 'gost' from snap gost (2.11.5)   
  command 'most' from deb most (5.0.0a-4)   
  command 'ost' from deb openstructure (2.3.1-2build1)   
  command 'host' from deb bind9-host (1:9.18.28-0ubuntu0.22.04.1)   
  command 'gost' from deb gost (0.1.0+git20181204.5afeda5e-1.1ubuntu0.22.04.2)   
See 'snap info <snapname>' for additional versions.   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ iostate   
Command 'iostate' not found, did you mean:   
  command 'iostat' from deb sysstat (12.5.2-2ubuntu0.2)   
Try: sudo apt install <deb name>   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ iostat   
Command 'iostat' not found, but can be installed with:   
sudo apt install sysstat   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo apt istall systat   
[sudo] password for hari:   
E: Invalid operation istall   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo apt istall systat   
E: Invalid operation istall   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ hari123   
hari123: command not found   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo apt istall systat   
E: Invalid operation istall   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo apt istall systat   
E: Invalid operation istall   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo apt install sysstat   
Reading package lists... Done   
Building dependency tree... Done   
Reading state information... Done   
Suggested packages:   
  isag   
The following NEW packages will be installed:   
  sysstat   
0 upgraded, 1 newly installed, 0 to remove and 57 not upgraded.   
Need to get 487 kB of archives.   
After this operation, 1507 kB of additional disk space will be used.   
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 sysstat amd64 12.5.2-2ubuntu0.2 [487 kB]   
Fetched 487 kB in 1s (331 kB/s)   
Preconfiguring packages ...   
Selecting previously unselected package sysstat.   
(Reading database ... 65008 files and directories currently installed.)   
Preparing to unpack .../sysstat_12.5.2-2ubuntu0.2_amd64.deb ...   
Unpacking sysstat (12.5.2-2ubuntu0.2) ...   
Setting up sysstat (12.5.2-2ubuntu0.2) ...   
   
Creating config file /etc/default/sysstat with new version   
update-alternatives: using /usr/bin/sar.sysstat to provide /usr/bin/sar (sar) in auto mode   
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-collect.timer → /lib/systemd/system/sysstat-collect.timer.   
Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-summary.timer → /lib/systemd/system/sysstat-summary.timer.   
Created symlink /etc/systemd/system/multi-user.target.wants/sysstat.service → /lib/systemd/system/sysstat.service.   
Processing triggers for man-db (2.10.2-1) ...   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ iostat   
Linux 5.15.153.1-microsoft-standard-WSL2 (Hari-MSI)     08/15/24        _x86_64_        (16 CPU)   
   
avg-cpu:  %user   %nice %system %iowait  %steal   %idle   
           0.31    0.00    0.54    0.01    0.00   99.14   
   
Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd   
sda               0.16         9.69         0.00         0.00     113285          0          0   
sdb               0.01         0.28         0.00         0.00       3276          4          0   
sdc               7.37       335.49      1398.38       632.98    3923934   16355616    7403380   
   
   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ speedtest-cli   
Command 'speedtest-cli' not found, but can be installed with:   
sudo snap install speedtest-cli  # version 2.1.3+pkg-d3a7, or   
sudo apt  install speedtest-cli  # version 2.1.3-2   
See 'snap info speedtest-cli' for additional versions.   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo snap install speedtest-cli   
speedtest-cli 2.1.3+pkg-d3a7 from 林博仁(Buo-ren Lin) (brlin) installed   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ speedtest-cli   
Retrieving speedtest.net configuration...   
Testing from Jio (49.43.168.64)...   
Retrieving speedtest.net server list...   
Selecting best server based on ping...   
Hosted by Jio (Shimla) [119.23 km]: 34.75 ms   
Testing download speed................................................................................   
Download: 90.19 Mbit/s   
Testing upload speed......................................................................................................   
Upload: 51.86 Mbit/s   
   
   
   
# window 2   
   
C:\Users\hari_\venvs>wsl   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ source tfenv-wsl/bin/activate   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ nvcc --version   
Command 'nvcc' not found, but can be installed with:   
sudo apt install nvidia-cuda-toolkit   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ nano ~/.bashrc   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ source ~/.bash   
.bash_history  .bash_logout   .bashrc   
## (tfenv-wsl) hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ source ~/.bashrc   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ nvcc --version   
nvcc: NVIDIA (R) Cuda compiler driver   
Copyright (c) 2005-2021 NVIDIA Corporation   
Built on Sun_Feb_14_21:12:58_PST_2021   
Cuda compilation tools, release 11.2, V11.2.152   
Build cuda_11.2.r11.2/compiler.29618528_0   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ldconfig -p | grep cuda   
        libnvrtc.so.11.2 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvrtc.so.11.2   
        libnvrtc.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvrtc.so   
        libnvrtc-builtins.so.11.2 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvrtc-builtins.so.11.2   
        libnvrtc-builtins.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvrtc-builtins.so   
        libnvperf_target.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvperf_target.so   
        libnvperf_host.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvperf_host.so   
        libnvjpeg.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvjpeg.so.11   
        libnvjpeg.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvjpeg.so   
        libnvblas.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvblas.so.11   
        libnvblas.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvblas.so   
        libnvToolsExt.so.1 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvToolsExt.so.1   
        libnvToolsExt.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnvToolsExt.so   
        libnpps.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnpps.so.11   
        libnpps.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnpps.so   
        libnppitc.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppitc.so.11   
        libnppitc.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppitc.so   
        libnppisu.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppisu.so.11   
        libnppisu.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppisu.so   
        libnppist.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppist.so.11   
        libnppist.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppist.so   
        libnppim.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppim.so.11   
        libnppim.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppim.so   
        libnppig.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppig.so.11   
        libnppig.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppig.so   
        libnppif.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppif.so.11   
        libnppif.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppif.so   
        libnppidei.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppidei.so.11   
        libnppidei.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppidei.so   
        libnppicc.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppicc.so.11   
        libnppicc.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppicc.so   
        libnppial.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppial.so.11   
        libnppial.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppial.so   
        libnppc.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppc.so.11   
        libnppc.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libnppc.so   
        libicudata.so.70 (libc6,x86-64) => /lib/x86_64-linux-gnu/libicudata.so.70   
        libicudata.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libicudata.so   
        libcusparse.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusparse.so.11   
        libcusparse.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusparse.so   
        libcusolverMg.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusolverMg.so.11   
        libcusolverMg.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusolverMg.so   
        libcusolver.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusolver.so.11   
        libcusolver.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcusolver.so   
        libcurand.so.10 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcurand.so.10   
        libcurand.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcurand.so   
        libcupti.so.11.2 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcupti.so.11.2   
        libcupti.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcupti.so   
        libcuinj64.so.11.2 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcuinj64.so.11.2   
        libcuinj64.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcuinj64.so   
        libcufftw.so.10 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcufftw.so.10   
        libcufftw.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcufftw.so   
        libcufft.so.10 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcufft.so.10   
        libcufft.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcufft.so   
        libcudart.so.11.0 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcudart.so.11.0   
        libcudart.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcudart.so   
        libcudadebugger.so.1 (libc6,x86-64) => /usr/lib/wsl/lib/libcudadebugger.so.1   
        libcuda.so.1 (libc6,x86-64) => /usr/lib/wsl/lib/libcuda.so.1   
        libcublasLt.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcublasLt.so.11   
        libcublasLt.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcublasLt.so   
        libcublas.so.11 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcublas.so.11   
        libcublas.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libcublas.so   
        libaccinj64.so.11.2 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libaccinj64.so.11.2   
        libaccinj64.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libaccinj64.so   
        libOpenCL.so.1 (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libOpenCL.so.1   
        libOpenCL.so (libc6,x86-64) => /usr/local/cuda/targets/x86_64-linux/lib/libOpenCL.so   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ldconfig -p | grep cudnn   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ tar -xzvf cudnn-x.x-linux-x64-vx.x.x.x.tgz   
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include   
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64   
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*   
tar (child): cudnn-x.x-linux-x64-vx.x.x.x.tgz: Cannot open: No such file or directory   
tar (child): Error is not recoverable: exiting now   
tar: Child returned status 2   
tar: Error is not recoverable: exiting now   
[sudo] password for hari:   
cp: cannot stat 'cuda/include/cudnn*.h': No such file or directory   
cp: cannot stat 'cuda/lib64/libcudnn*': No such file or directory   
chmod: cannot access '/usr/local/cuda/include/cudnn*.h': No such file or directory   
chmod: cannot access '/usr/local/cuda/lib64/libcudnn*': No such file or directory   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ nvcc --version   
nvcc: NVIDIA (R) Cuda compiler driver   
Copyright (c) 2005-2021 NVIDIA Corporation   
Built on Sun_Feb_14_21:12:58_PST_2021   
Cuda compilation tools, release 11.2, V11.2.152   
Build cuda_11.2.r11.2/compiler.29618528_0   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ tar -xzvf cudnn-11.2-linux-x64-v8.1.x.x.tgz   
tar (child): cudnn-11.2-linux-x64-v8.1.x.x.tgz: Cannot open: No such file or directory   
tar (child): Error is not recoverable: exiting now   
tar: Child returned status 2   
tar: Error is not recoverable: exiting now   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ wget https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_installers/11.x/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz/   
--2024-08-14 23:05:22--  https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_installers/11.x/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz/   
Resolving developer.nvidia.com (developer.nvidia.com)... 152.199.39.144   
Connecting to developer.nvidia.com (developer.nvidia.com)|152.199.39.144|:443... connected.   
HTTP request sent, awaiting response... 302 Found   
Location: https://developer.nvidia.com/login [following]   
--2024-08-14 23:05:32--  https://developer.nvidia.com/login   
Reusing existing connection to developer.nvidia.com:443.   
HTTP request sent, awaiting response... 200 OK   
Length: 8339 (8.1K) [text/html]   
Saving to: ‘index.html’   
   
index.html                    100%[=================================================>]   8.14K  --.-KB/s    in 0.001s   
   
2024-08-14 23:05:33 (6.20 MB/s) - ‘index.html’ saved [8339/8339]   
   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls   
docker  index.html  output  py  quantization.py  sparse_logs  tensorboard  tfenv-wsl   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ wget -c https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_   
installers/11.x/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz/   
--2024-08-14 23:11:57--  https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_installers/11.x/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz/   
Resolving developer.nvidia.com (developer.nvidia.com)... 152.199.39.144   
Connecting to developer.nvidia.com (developer.nvidia.com)|152.199.39.144|:443... connected.   
HTTP request sent, awaiting response... 302 Found   
Location: https://developer.nvidia.com/login [following]   
--2024-08-14 23:11:58--  https://developer.nvidia.com/login   
Reusing existing connection to developer.nvidia.com:443.   
HTTP request sent, awaiting response... 200 OK   
   
    The file is already fully retrieved; nothing to do.   
   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ tar -xzvf /mnt/c/users/hari_/Downloads/cudnn-linux-x86_64-8.9.7.29_cuda11-archiv   
e.tar.xz   
   
gzip: stdin: not in gzip format   
tar: Child returned status 1   
tar: Error is not recoverable: exiting now   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ tar -xvf /mnt/c/users/hari_/Downloads/cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_infer_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_infer_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_train_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_train_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_infer_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_infer_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_train_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_train_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_infer_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_infer_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_train_static.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_train_static_v8.a   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_infer.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_infer.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_infer.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_train.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_train.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_adv_train.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_infer.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_infer.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_infer.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_train.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_train.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_cnn_train.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_infer.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_infer.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_infer.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_train.so   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_train.so.8   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn_ops_train.so.8.9.7   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_backend_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_version_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_backend.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_version.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/LICENSE   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo cp cuda/include/cudnn*.h /usr/local/cuda/include   
[sudo] password for hari:   
cp: cannot stat 'cuda/include/cudnn*.h': No such file or directory   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive  docker  output  py  quantization.py  sparse_logs  tensorboard  tfenv-wsl   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls /   
Docker  dev   init   lib64       media  proc  sbin  sys  var        wslPnDdLF  wslgoEaOd  wslnfooOd   
bin     etc   lib    libx32      mnt    root  snap  tmp  wslBpFhMF  wslfGbnOd  wsliIflOd  wslokedNd   
boot    home  lib32  lost+found  opt    run   srv   usr  wslJCIjMF  wslgGPEMF  wsljcjkMF   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls /usr   
bin  games  include  lib  lib32  lib64  libexec  libx32  local  sbin  share  src   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls -l /mnt/c/users/hari_/Downloads   
total 6633180   
-rwxrwxrwx 1 hari hari  701155584 Aug 14 22:15  560.81-notebook-win10-win11-64bit-international-nsd-dch-whql.exe   
-rwxrwxrwx 1 hari hari     267336 Jul 31 20:23  GoogleCloudSDKInstaller.exe   
-rwxrwxrwx 1 hari hari    9268677 Aug  5 17:31  Llama3.1.pdf   
-rwxrwxrwx 1 hari hari   25062821 Aug  4 18:43  Object_detection.ipynb   
-rwxrwxrwx 1 hari hari    3265343 Aug  6 21:04  Web_Photo_Editor.jpg   
-rwxrwxrwx 1 hari hari    4179016 Aug  9 10:57  Windows11InstallationAssistant.exe   
-rwxrwxrwx 1 hari hari        368 Jul 31 20:59  client_secret1.json   
-rwxrwxrwx 1 hari hari        411 Jul 31 21:07  client_secret2.json   
-rwxrwxrwx 1 hari hari 3216570184 Aug 14 22:01  cuda_12.6.0_560.76_windows.exe   
-rwxrwxrwx 1 hari hari  860967256 Aug 14 23:12  cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz   
-rwxrwxrwx 1 hari hari  566118754 Aug 14 21:50  cudnn-windows-x86_64-9.3.0.75_cuda12-archive.zip   
-rwxrwxrwx 1 hari hari        282 Jun 14 23:38  desktop.ini   
-rwxrwxrwx 1 hari hari   53931311 Aug  4 09:51  ffmpeg-2024-08-01-git-bcf08c1171-full_build.7z   
drwxrwxrwx 1 hari hari        512 Aug  1 16:10  ffmpeg-full_build   
drwxrwxrwx 1 hari hari        512 Aug  9 11:27  flutter_windows_3.24.0-stable   
-rwxrwxrwx 1 hari hari 1011366683 Aug  9 11:00  flutter_windows_3.24.0-stable.zip   
-rwxrwxrwx 1 hari hari  172330104 Aug  8 18:38  jdk-22_windows-x64_bin.exe   
-rwxrwxrwx 1 hari hari   68480862 Aug  7 16:40  libtensorflow-cpu-windows-x86_64-2.9.1.zip   
-rwxrwxrwx 1 hari hari       4417 Aug  7 18:53  model.json   
-rwxrwxrwx 1 hari hari        918 Aug  7 19:09 'mymodel (1).json'   
-rwxrwxrwx 1 hari hari       1757 Aug  7 19:08  mymodel.json   
-rwxrwxrwx 1 hari hari         44 Aug  7 19:09 'mymodel.weights (1).bin'   
-rwxrwxrwx 1 hari hari         44 Aug  7 19:07  mymodel.weights.bin   
-rwxrwxrwx 1 hari hari   26574848 Aug  6 15:34 'node-v20.16.0-x64 (1).msi'   
-rwxrwxrwx 1 hari hari   26574848 Aug  6 12:23  node-v20.16.0-x64.msi   
-rwxrwxrwx 1 hari hari    2037024 Aug  6 21:18  picwish-setup.exe   
-rwxrwxrwx 1 hari hari      77490 Aug  6 23:16  pitch_type_test_data.csv   
-rwxrwxrwx 1 hari hari     657534 Aug  6 23:16  pitch_type_training_data.csv   
-rwxrwxrwx 1 hari hari   41762063 Aug  4 12:45  sample.mp3   
-rwxrwxrwx 1 hari hari       1683 Aug  4 18:53  search.html   
-rwxrwxrwx 1 hari hari    1671168 Aug  6 15:32  yarn-1.22.22.msi   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive  docker  output  py  quantization.py  sparse_logs  tensorboard  tfenv-wsl   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/   
LICENSE  include  lib   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cdnn*.h   
ls: cannot access 'cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cdnn*.h': No such file or directory   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include   
cudnn.h               cudnn_adv_train_v8.h  cudnn_cnn_infer_v8.h  cudnn_ops_infer_v8.h  cudnn_version.h   
cudnn_adv_infer.h     cudnn_backend.h       cudnn_cnn_train.h     cudnn_ops_train.h     cudnn_version_v8.h   
cudnn_adv_infer_v8.h  cudnn_backend_v8.h    cudnn_cnn_train_v8.h  cudnn_ops_train_v8.h   
cudnn_adv_train.h     cudnn_cnn_infer.h     cudnn_ops_infer.h     cudnn_v8.h   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn*.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_adv_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_backend.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_backend_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_cnn_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_infer.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_infer_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_train.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_ops_train_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_v8.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_version.h   
cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn_version_v8.h   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo cp cudnn-linux-x86_64-8.9.7.29_cuda11-archive/include/cudnn*.h /usr/local/c   
uda/include   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo cp cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib64/libcudnn* /usr/local/cu   
da/lib64   
cp: cannot stat 'cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib64/libcudnn*': No such file or directory   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/   
LICENSE  include  lib   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ ls cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib   
libcudnn.so                     libcudnn_adv_train_static.a     libcudnn_cnn_train_static_v8.a   
libcudnn.so.8                   libcudnn_adv_train_static_v8.a  libcudnn_ops_infer.so   
libcudnn.so.8.9.7               libcudnn_cnn_infer.so           libcudnn_ops_infer.so.8   
libcudnn_adv_infer.so           libcudnn_cnn_infer.so.8         libcudnn_ops_infer.so.8.9.7   
libcudnn_adv_infer.so.8         libcudnn_cnn_infer.so.8.9.7     libcudnn_ops_infer_static.a   
libcudnn_adv_infer.so.8.9.7     libcudnn_cnn_infer_static.a     libcudnn_ops_infer_static_v8.a   
libcudnn_adv_infer_static.a     libcudnn_cnn_infer_static_v8.a  libcudnn_ops_train.so   
libcudnn_adv_infer_static_v8.a  libcudnn_cnn_train.so           libcudnn_ops_train.so.8   
libcudnn_adv_train.so           libcudnn_cnn_train.so.8         libcudnn_ops_train.so.8.9.7   
libcudnn_adv_train.so.8         libcudnn_cnn_train.so.8.9.7     libcudnn_ops_train_static.a   
libcudnn_adv_train.so.8.9.7     libcudnn_cnn_train_static.a     libcudnn_ops_train_static_v8.a   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo cp cudnn-linux-x86_64-8.9.7.29_cuda11-archive/lib/libcudnn* /usr/local/cuda   
/lib64   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo ldconfig   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 is not a symbolic link   
   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ sudo ldconfig   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 is not a symbolic link   
   
/sbin/ldconfig.real: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 is not a symbolic link   
   
## hari@Hari-MSI:/mnt/c/Users/hari_/venvs\$ cd /usr/local/cuda/targets/x86_64-linux/lib/   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ ls   
libOpenCL.so                    libcudnn_ops_train_static.a     libnppidei_static.a   
libOpenCL.so.1                  libcudnn_ops_train_static_v8.a  libnppif.so   
libOpenCL.so.1.0                libcufft.so                     libnppif.so.11   
libOpenCL.so.1.0.0              libcufft.so.10                  libnppif.so.11.3.2.152   
libaccinj64.so                  libcufft.so.10.4.1.152          libnppif_static.a   
libaccinj64.so.11.2             libcufft_static.a               libnppig.so   
libaccinj64.so.11.2.152         libcufft_static_nocallback.a    libnppig.so.11   
libcublas.so                    libcufftw.so                    libnppig.so.11.3.2.152   
libcublas.so.11                 libcufftw.so.10                 libnppig_static.a   
libcublas.so.11.4.1.1043        libcufftw.so.10.4.1.152         libnppim.so   
libcublasLt.so                  libcufftw_static.a              libnppim.so.11   
libcublasLt.so.11               libcuinj64.so                   libnppim.so.11.3.2.152   
libcublasLt.so.11.4.1.1043      libcuinj64.so.11.2              libnppim_static.a   
libcublasLt_static.a            libcuinj64.so.11.2.152          libnppist.so   
libcublas_static.a              libculibos.a                    libnppist.so.11   
libcudadevrt.a                  libcupti.so                     libnppist.so.11.3.2.152   
libcudart.so                    libcupti.so.11.2                libnppist_static.a   
libcudart.so.11.0               libcupti.so.2020.3.1            libnppisu.so   
libcudart.so.11.2.152           libcupti_static.a               libnppisu.so.11   
libcudart_static.a              libcurand.so                    libnppisu.so.11.3.2.152   
libcudnn.so                     libcurand.so.10                 libnppisu_static.a   
libcudnn.so.8                   libcurand.so.10.2.3.152         libnppitc.so   
libcudnn.so.8.9.7               libcurand_static.a              libnppitc.so.11   
libcudnn_adv_infer.so           libcusolver.so                  libnppitc.so.11.3.2.152   
libcudnn_adv_infer.so.8         libcusolver.so.11               libnppitc_static.a   
libcudnn_adv_infer.so.8.9.7     libcusolver.so.11.1.0.152       libnpps.so   
libcudnn_adv_infer_static.a     libcusolverMg.so                libnpps.so.11   
libcudnn_adv_infer_static_v8.a  libcusolverMg.so.11             libnpps.so.11.3.2.152   
libcudnn_adv_train.so           libcusolverMg.so.11.1.0.152     libnpps_static.a   
libcudnn_adv_train.so.8         libcusolver_static.a            libnvToolsExt.so   
libcudnn_adv_train.so.8.9.7     libcusparse.so                  libnvToolsExt.so.1   
libcudnn_adv_train_static.a     libcusparse.so.11               libnvToolsExt.so.1.0.0   
libcudnn_adv_train_static_v8.a  libcusparse.so.11.4.1.1152      libnvblas.so   
libcudnn_cnn_infer.so           libcusparse_static.a            libnvblas.so.11   
libcudnn_cnn_infer.so.8         liblapack_static.a              libnvblas.so.11.4.1.1043   
libcudnn_cnn_infer.so.8.9.7     libmetis_static.a               libnvjpeg.so   
libcudnn_cnn_infer_static.a     libnppc.so                      libnvjpeg.so.11   
libcudnn_cnn_infer_static_v8.a  libnppc.so.11                   libnvjpeg.so.11.4.0.152   
libcudnn_cnn_train.so           libnppc.so.11.3.2.152           libnvjpeg_static.a   
libcudnn_cnn_train.so.8         libnppc_static.a                libnvperf_host.so   
libcudnn_cnn_train.so.8.9.7     libnppial.so                    libnvperf_host_static.a   
libcudnn_cnn_train_static.a     libnppial.so.11                 libnvperf_target.so   
libcudnn_cnn_train_static_v8.a  libnppial.so.11.3.2.152         libnvptxcompiler_static.a   
libcudnn_ops_infer.so           libnppial_static.a              libnvrtc-builtins.so   
libcudnn_ops_infer.so.8         libnppicc.so                    libnvrtc-builtins.so.11.2   
libcudnn_ops_infer.so.8.9.7     libnppicc.so.11                 libnvrtc-builtins.so.11.2.152   
libcudnn_ops_infer_static.a     libnppicc.so.11.3.2.152         libnvrtc.so   
libcudnn_ops_infer_static_v8.a  libnppicc_static.a              libnvrtc.so.11.2   
libcudnn_ops_train.so           libnppidei.so                   libnvrtc.so.11.2.152   
libcudnn_ops_train.so.8         libnppidei.so.11                nvrtc-prev   
libcudnn_ops_train.so.8.9.7     libnppidei.so.11.3.2.152        stubs   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ sudo ln -sf libcudnn.so.8.9.7 libcudnn.so.8   
sudo ln -sf libcudnn_ops_train.so.8.9.7 libcudnn_ops_train.so.8   
sudo ln -sf libcudnn_adv_infer.so.8.9.7 libcudnn_adv_infer.so.8   
sudo ln -sf libcudnn_adv_train.so.8.9.7 libcudnn_adv_train.so.8   
sudo ln -sf libcudnn_cnn_train.so.8.9.7 libcudnn_cnn_train.so.8   
sudo ln -sf libcudnn_cnn_infer.so.8.9.7 libcudnn_cnn_infer.so.8   
sudo ln -sf libcudnn_ops_infer.so.8.9.7 libcudnn_ops_infer.so.8   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ sudo ldconfig   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ pip install tensorflow-gpu   
Collecting tensorflow-gpu   
  Using cached tensorflow-gpu-2.12.0.tar.gz (2.6 kB)   
  Preparing metadata (setup.py) ... done   
Requirement already satisfied: python_version>"3.7" in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow-gpu) (0.0.2)   
Using legacy 'setup.py install' for tensorflow-gpu, since package 'wheel' is not installed.   
Installing collected packages: tensorflow-gpu   
  Running setup.py install for tensorflow-gpu ... error   
  error: subprocess-exited-with-error   
   
  × Running setup.py install for tensorflow-gpu did not run successfully.   
  │ exit code: 1   
  ╰─> [18 lines of output]   
      Traceback (most recent call last):   
        File "<string>", line 2, in <module>   
        File "<pip-setuptools-caller>", line 34, in <module>   
        File "/tmp/pip-install-q9x6bed8/tensorflow-gpu_c95dc661b75049b4924f43b5b9baa7a0/setup.py", line 37, in <module>   
          raise Exception(TF_REMOVAL_WARNING)   
      Exception:   
   
      =========================================================   
      The "tensorflow-gpu" package has been removed!   
   
      Please install "tensorflow" instead.   
   
      Other than the name, the two packages have been identical   
      since TensorFlow 2.1, or roughly since Sep 2019. For more   
      information, see: pypi.org/project/tensorflow-gpu   
      =========================================================   
   
   
      [end of output]   
   
  note: This error originates from a subprocess, and is likely not a problem with pip.   
error: legacy-install-failure   
   
× Encountered error while trying to install package.   
╰─> tensorflow-gpu   
   
note: This is an issue with the package mentioned above, not pip.   
hint: See above for output from the failure.   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ pip install tensorflow   
Collecting tensorflow   
  Downloading tensorflow-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)   
     ━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━━━━━━━━━━ 205.1/601.3 MB 93.1 kB/s eta 1:10:55   
ERROR: Operation cancelled by user   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ ^C   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ ^C   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ ^C   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ ls   
libOpenCL.so                    libcudnn_ops_train_static.a     libnppidei_static.a   
libOpenCL.so.1                  libcudnn_ops_train_static_v8.a  libnppif.so   
libOpenCL.so.1.0                libcufft.so                     libnppif.so.11   
libOpenCL.so.1.0.0              libcufft.so.10                  libnppif.so.11.3.2.152   
libaccinj64.so                  libcufft.so.10.4.1.152          libnppif_static.a   
libaccinj64.so.11.2             libcufft_static.a               libnppig.so   
libaccinj64.so.11.2.152         libcufft_static_nocallback.a    libnppig.so.11   
libcublas.so                    libcufftw.so                    libnppig.so.11.3.2.152   
libcublas.so.11                 libcufftw.so.10                 libnppig_static.a   
libcublas.so.11.4.1.1043        libcufftw.so.10.4.1.152         libnppim.so   
libcublasLt.so                  libcufftw_static.a              libnppim.so.11   
libcublasLt.so.11               libcuinj64.so                   libnppim.so.11.3.2.152   
libcublasLt.so.11.4.1.1043      libcuinj64.so.11.2              libnppim_static.a   
libcublasLt_static.a            libcuinj64.so.11.2.152          libnppist.so   
libcublas_static.a              libculibos.a                    libnppist.so.11   
libcudadevrt.a                  libcupti.so                     libnppist.so.11.3.2.152   
libcudart.so                    libcupti.so.11.2                libnppist_static.a   
libcudart.so.11.0               libcupti.so.2020.3.1            libnppisu.so   
libcudart.so.11.2.152           libcupti_static.a               libnppisu.so.11   
libcudart_static.a              libcurand.so                    libnppisu.so.11.3.2.152   
libcudnn.so                     libcurand.so.10                 libnppisu_static.a   
libcudnn.so.8                   libcurand.so.10.2.3.152         libnppitc.so   
libcudnn.so.8.9.7               libcurand_static.a              libnppitc.so.11   
libcudnn_adv_infer.so           libcusolver.so                  libnppitc.so.11.3.2.152   
libcudnn_adv_infer.so.8         libcusolver.so.11               libnppitc_static.a   
libcudnn_adv_infer.so.8.9.7     libcusolver.so.11.1.0.152       libnpps.so   
libcudnn_adv_infer_static.a     libcusolverMg.so                libnpps.so.11   
libcudnn_adv_infer_static_v8.a  libcusolverMg.so.11             libnpps.so.11.3.2.152   
libcudnn_adv_train.so           libcusolverMg.so.11.1.0.152     libnpps_static.a   
libcudnn_adv_train.so.8         libcusolver_static.a            libnvToolsExt.so   
libcudnn_adv_train.so.8.9.7     libcusparse.so                  libnvToolsExt.so.1   
libcudnn_adv_train_static.a     libcusparse.so.11               libnvToolsExt.so.1.0.0   
libcudnn_adv_train_static_v8.a  libcusparse.so.11.4.1.1152      libnvblas.so   
libcudnn_cnn_infer.so           libcusparse_static.a            libnvblas.so.11   
libcudnn_cnn_infer.so.8         liblapack_static.a              libnvblas.so.11.4.1.1043   
libcudnn_cnn_infer.so.8.9.7     libmetis_static.a               libnvjpeg.so   
libcudnn_cnn_infer_static.a     libnppc.so                      libnvjpeg.so.11   
libcudnn_cnn_infer_static_v8.a  libnppc.so.11                   libnvjpeg.so.11.4.0.152   
libcudnn_cnn_train.so           libnppc.so.11.3.2.152           libnvjpeg_static.a   
libcudnn_cnn_train.so.8         libnppc_static.a                libnvperf_host.so   
libcudnn_cnn_train.so.8.9.7     libnppial.so                    libnvperf_host_static.a   
libcudnn_cnn_train_static.a     libnppial.so.11                 libnvperf_target.so   
libcudnn_cnn_train_static_v8.a  libnppial.so.11.3.2.152         libnvptxcompiler_static.a   
libcudnn_ops_infer.so           libnppial_static.a              libnvrtc-builtins.so   
libcudnn_ops_infer.so.8         libnppicc.so                    libnvrtc-builtins.so.11.2   
libcudnn_ops_infer.so.8.9.7     libnppicc.so.11                 libnvrtc-builtins.so.11.2.152   
libcudnn_ops_infer_static.a     libnppicc.so.11.3.2.152         libnvrtc.so   
libcudnn_ops_infer_static_v8.a  libnppicc_static.a              libnvrtc.so.11.2   
libcudnn_ops_train.so           libnppidei.so                   libnvrtc.so.11.2.152   
libcudnn_ops_train.so.8         libnppidei.so.11                nvrtc-prev   
libcudnn_ops_train.so.8.9.7     libnppidei.so.11.3.2.152        stubs   
## hari@Hari-MSI:/usr/local/cuda/targets/x86_64-linux/lib\$ cd ~   
## hari@Hari-MSI:~\$ ls   
a.txt  mistral_7b_instruct_v3  snap  tensorflow_datasets   
## hari@Hari-MSI:~\$ owd   
Command 'owd' not found, did you mean:   
  command 'wod' from deb sope-bin (5.5.1-1)   
  command 'gwd' from deb geneweb (6.08+git20181019+dfsg-3)   
  command 'owx' from deb owx (0~20110415-3.1build2)   
  command 'xwd' from deb x11-apps (7.7+8build2)   
  command 'od' from deb coreutils (8.32-4.1ubuntu1.2)   
  command 'pwd' from deb coreutils (8.32-4.1ubuntu1.2)   
Try: sudo apt install <deb name>   
## hari@Hari-MSI:~\$ pwd   
/home/hari   
## hari@Hari-MSI:~\$ ls   
a.txt  mistral_7b_instruct_v3  snap  tensorflow_datasets   
## hari@Hari-MSI:~\$ rm mistral_7b_instruct_v3   
rm: cannot remove 'mistral_7b_instruct_v3': Is a directory   
## hari@Hari-MSI:~\$ ls mistral_7b_instruct_v3/   
consolidated.safetensors  params.json  tokenizer.model.v3   
## hari@Hari-MSI:~\$ ls tensorflow_datasets/   
downloads  imdb_reviews   
## hari@Hari-MSI:~\$ ls tensorflow_datasets/downloads   
ai.stanfor.edu_amaas_sentime_aclImdb_v1xA90oY07YfkP66HhdzDg046Ll8Bf3nAIlC6Rkj0WWP4.tar.gz       extracted   
ai.stanfor.edu_amaas_sentime_aclImdb_v1xA90oY07YfkP66HhdzDg046Ll8Bf3nAIlC6Rkj0WWP4.tar.gz.INFO   
## hari@Hari-MSI:~\$ ls tensorflow_datasets/download^C   
## hari@Hari-MSI:~\$ ls   
a.txt  mistral_7b_instruct_v3  snap  tensorflow_datasets   
## hari@Hari-MSI:~\$ ls /mnt/c/User   
ls: cannot access '/mnt/c/User': No such file or directory   
## hari@Hari-MSI:~\$ ls /mnt/c/Users   
'All Users'   Default  'Default User'   Public   desktop.ini   hari_   
## hari@Hari-MSI:~\$ ls /mnt/c/Users/hari_/Downloads   
 560.81-notebook-win10-win11-64bit-international-nsd-dch-whql.exe   jdk-22_windows-x64_bin.exe   
 GoogleCloudSDKInstaller.exe                                        libtensorflow-cpu-windows-x86_64-2.9.1.zip   
 Llama3.1.pdf                                                       model.json   
 Object_detection.ipynb                                            'mymodel (1).json'   
 Web_Photo_Editor.jpg                                               mymodel.json   
 Windows11InstallationAssistant.exe                                'mymodel.weights (1).bin'   
 client_secret1.json                                                mymodel.weights.bin   
 client_secret2.json                                               'node-v20.16.0-x64 (1).msi'   
 cuda_12.6.0_560.76_windows.exe                                     node-v20.16.0-x64.msi   
 cudnn-linux-x86_64-8.9.7.29_cuda11-archive.tar.xz                  picwish-setup.exe   
 cudnn-windows-x86_64-9.3.0.75_cuda12-archive.zip                   pitch_type_test_data.csv   
 desktop.ini                                                        pitch_type_training_data.csv   
 ffmpeg-2024-08-01-git-bcf08c1171-full_build.7z                     sample.mp3   
 ffmpeg-full_build                                                  search.html   
 flutter_windows_3.24.0-stable                                      yarn-1.22.22.msi   
 flutter_windows_3.24.0-stable.zip   
## hari@Hari-MSI:~\$ ls /mnt/c/Users/hari_/venvs/t   
tensorboard/ tfenv-wsl/   
## hari@Hari-MSI:~\$ ls /mnt/c/Users/hari_/venvs/tfenv-wsl/bin/activate   
/mnt/c/Users/hari_/venvs/tfenv-wsl/bin/activate   
## hari@Hari-MSI:~\$ source /mnt/c/Users/hari_/venvs/tfenv-wsl/bin/activate   
## (tfenv-wsl) hari@Hari-MSI:~\$ pip install tensorflow   
Collecting tensorflow   
  Downloading tensorflow-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/601.3 MB 69.9 kB/s eta 2:22:16   
ERROR: Exception:   
Traceback (most recent call last):   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/urllib3/response.py", line 438, in _error_catcher   
    yield   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/urllib3/response.py", line 519, in read   
    data = self._fp.read(amt) if not fp_closed else b""   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/cachecontrol/filewrapper.py", line 90, in read   
    data = self.__fp.read(amt)   
  File "/usr/lib/python3.10/http/client.py", line 466, in read   
    s = self.fp.read(amt)   
  File "/usr/lib/python3.10/socket.py", line 705, in readinto   
    return self._sock.recv_into(b)   
  File "/usr/lib/python3.10/ssl.py", line 1303, in recv_into   
    return self.read(nbytes, buffer)   
  File "/usr/lib/python3.10/ssl.py", line 1159, in read   
    return self._sslobj.read(len, buffer)   
TimeoutError: The read operation timed out   
   
During handling of the above exception, another exception occurred:   
   
Traceback (most recent call last):   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/cli/base_command.py", line 165, in exc_logging_wrapper   
    status = run_func(*args)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/cli/req_command.py", line 205, in wrapper   
    return func(self, options, args)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/commands/install.py", line 339, in run   
    requirement_set = resolver.resolve(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 94, in resolve   
    result = self._result = resolver.resolve(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/resolvelib/resolvers.py", line 481, in resolve   
    state = resolution.resolve(requirements, max_rounds=max_rounds)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/resolvelib/resolvers.py", line 348, in resolve   
    self._add_to_criteria(self.state.criteria, r, parent=None)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/resolvelib/resolvers.py", line 172, in _add_to_criteria   
    if not criterion.candidates:   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/resolvelib/structs.py", line 151, in __bool__   
    return bool(self._sequence)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 155, in __bool__   
    return any(self)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 143, in <genexpr>   
    return (c for c in iterator if id(c) not in self._incompatible_ids)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py", line 47, in _iter_built   
    candidate = func()   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 215, in _make_candidate_from_link   
    self._link_candidate_cache[link] = LinkCandidate(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 288, in __init__   
    super().__init__(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 158, in __init__   
    self.dist = self._prepare()   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 227, in _prepare   
    dist = self._prepare_distribution()   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 299, in _prepare_distribution   
    return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/operations/prepare.py", line 487, in prepare_linked_requirement   
    return self._prepare_linked_requirement(req, parallel_builds)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/operations/prepare.py", line 532, in _prepare_linked_requirement   
    local_file = unpack_url(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/operations/prepare.py", line 214, in unpack_url   
    file = get_http_url(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/operations/prepare.py", line 94, in get_http_url   
    from_path, content_type = download(link, temp_dir.path)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/network/download.py", line 146, in __call__   
    for chunk in chunks:   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/cli/progress_bars.py", line 304, in _rich_progress_bar   
    for chunk in iterable:   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_internal/network/utils.py", line 63, in response_chunks   
    for chunk in response.raw.stream(   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/urllib3/response.py", line 576, in stream   
    data = self.read(amt=amt, decode_content=decode_content)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/urllib3/response.py", line 512, in read   
    with self._error_catcher():   
  File "/usr/lib/python3.10/contextlib.py", line 153, in __exit__   
    self.gen.throw(typ, value, traceback)   
  File "/mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages/pip/_vendor/urllib3/response.py", line 443, in _error_catcher   
    raise ReadTimeoutError(self._pool, None, "Read timed out.")   
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.   
## (tfenv-wsl) hari@Hari-MSI:~\$ pip install tensorflow   
Collecting tensorflow   
  Downloading tensorflow-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 601.3/601.3 MB 7.1 MB/s eta 0:00:00   
Collecting astunparse>=1.6.0   
  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)   
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1   
  Downloading gast-0.6.0-py3-none-any.whl (21 kB)   
Collecting requests<3,>=2.21.0   
  Downloading requests-2.32.3-py3-none-any.whl (64 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 KB 16.3 MB/s eta 0:00:00   
Collecting tensorflow-io-gcs-filesystem>=0.23.1   
  Downloading tensorflow_io_gcs_filesystem-0.37.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.1 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 17.1 MB/s eta 0:00:00   
Collecting flatbuffers>=24.3.25   
  Downloading flatbuffers-24.3.25-py2.py3-none-any.whl (26 kB)   
Collecting absl-py>=1.0.0   
  Downloading absl_py-2.1.0-py3-none-any.whl (133 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.7/133.7 KB 26.9 MB/s eta 0:00:00   
Collecting six>=1.12.0   
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)   
Collecting termcolor>=1.1.0   
  Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)   
Collecting libclang>=13.0.0   
  Downloading libclang-18.1.1-py2.py3-none-manylinux2010_x86_64.whl (24.5 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.5/24.5 MB 12.5 MB/s eta 0:00:00   
Collecting typing-extensions>=3.6.6   
  Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)   
Collecting h5py>=3.10.0   
  Downloading h5py-3.11.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.3 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 16.5 MB/s eta 0:00:00   
Collecting google-pasta>=0.1.1   
  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 KB 13.7 MB/s eta 0:00:00   
Collecting numpy<2.0.0,>=1.23.5   
  Downloading numpy-1.26.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 12.6 MB/s eta 0:00:00   
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3   
  Downloading protobuf-4.25.4-cp37-abi3-manylinux2014_x86_64.whl (294 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.6/294.6 KB 14.5 MB/s eta 0:00:00   
Requirement already satisfied: setuptools in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (59.6.0)   
Collecting ml-dtypes<0.5.0,>=0.3.1   
  Downloading ml_dtypes-0.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 30.0 MB/s eta 0:00:00   
Collecting tensorboard<2.18,>=2.17   
  Downloading tensorboard-2.17.0-py3-none-any.whl (5.5 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 16.6 MB/s eta 0:00:00   
Collecting keras>=3.2.0   
  Downloading keras-3.5.0-py3-none-any.whl (1.1 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 27.6 MB/s eta 0:00:00   
Collecting opt-einsum>=2.3.2   
  Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.5/65.5 KB 25.3 MB/s eta 0:00:00   
Collecting wrapt>=1.11.0   
  Downloading wrapt-1.16.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (80 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.3/80.3 KB 25.9 MB/s eta 0:00:00   
Collecting packaging   
  Downloading packaging-24.1-py3-none-any.whl (53 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.0/54.0 KB 17.4 MB/s eta 0:00:00   
Collecting grpcio<2.0,>=1.24.3   
  Downloading grpcio-1.65.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.7 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 16.4 MB/s eta 0:00:00   
Collecting wheel<1.0,>=0.23.0   
  Downloading wheel-0.44.0-py3-none-any.whl (67 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.1/67.1 KB 15.0 MB/s eta 0:00:00   
Collecting optree   
  Downloading optree-0.12.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (347 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.7/347.7 KB 28.7 MB/s eta 0:00:00   
Collecting rich   
  Downloading rich-13.7.1-py3-none-any.whl (240 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 240.7/240.7 KB 55.9 MB/s eta 0:00:00   
Collecting namex   
  Downloading namex-0.0.8-py3-none-any.whl (5.8 kB)   
Collecting urllib3<3,>=1.21.1   
  Downloading urllib3-2.2.2-py3-none-any.whl (121 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.4/121.4 KB 36.2 MB/s eta 0:00:00   
Collecting idna<4,>=2.5   
  Downloading idna-3.7-py3-none-any.whl (66 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.8/66.8 KB 18.6 MB/s eta 0:00:00   
Collecting certifi>=2017.4.17   
  Downloading certifi-2024.7.4-py3-none-any.whl (162 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.0/163.0 KB 56.1 MB/s eta 0:00:00   
Collecting charset-normalizer<4,>=2   
  Downloading charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (142 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 142.1/142.1 KB 33.9 MB/s eta 0:00:00   
Collecting tensorboard-data-server<0.8.0,>=0.7.0   
  Downloading tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 15.9 MB/s eta 0:00:00   
Collecting werkzeug>=1.0.1   
  Downloading werkzeug-3.0.3-py3-none-any.whl (227 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.3/227.3 KB 15.4 MB/s eta 0:00:00   
Collecting markdown>=2.6.8   
  Downloading Markdown-3.6-py3-none-any.whl (105 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 105.4/105.4 KB 40.5 MB/s eta 0:00:00   
Collecting MarkupSafe>=2.1.1   
  Downloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)   
Collecting pygments<3.0.0,>=2.13.0   
  Downloading pygments-2.18.0-py3-none-any.whl (1.2 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 48.2 MB/s eta 0:00:00   
Collecting markdown-it-py>=2.2.0   
  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 KB 42.9 MB/s eta 0:00:00   
Collecting mdurl~=0.1   
  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)   
Installing collected packages: namex, libclang, flatbuffers, wrapt, wheel, urllib3, typing-extensions, termcolor, tensorflow-io-gcs-filesystem, tensorboard-data-server, six, pygments, protobuf, packaging, numpy, mdurl, MarkupSafe, markdown, idna, grpcio, gast, charset-normalizer, certifi, absl-py, werkzeug, requests, optree, opt-einsum, ml-dtypes, markdown-it-py, h5py, google-pasta, astunparse, tensorboard, rich, keras, tensorflow   
^CERROR: Operation cancelled by user   
## (tfenv-wsl) hari@Hari-MSI:~\$ pip install tensorflow   
Collecting tensorflow   
  Using cached tensorflow-2.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)   
Requirement already satisfied: typing-extensions>=3.6.6 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (4.12.2)   
Requirement already satisfied: six>=1.12.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (1.16.0)   
Requirement already satisfied: packaging in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (24.1)   
Requirement already satisfied: ml-dtypes<0.5.0,>=0.3.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (0.4.0)   
Requirement already satisfied: absl-py>=1.0.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (2.1.0)   
Requirement already satisfied: tensorboard<2.18,>=2.17 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (2.17.0)   
Requirement already satisfied: libclang>=13.0.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (18.1.1)   
Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (0.6.0)   
Requirement already satisfied: google-pasta>=0.1.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (0.2.0)   
Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (0.37.1)   
Requirement already satisfied: opt-einsum>=2.3.2 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (3.3.0)   
Requirement already satisfied: flatbuffers>=24.3.25 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (24.3.25)   
Requirement already satisfied: grpcio<2.0,>=1.24.3 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (1.65.4)   
Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (4.25.4)   
Requirement already satisfied: termcolor>=1.1.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (2.4.0)   
Requirement already satisfied: astunparse>=1.6.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (1.6.3)   
Requirement already satisfied: keras>=3.2.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (3.5.0)   
Requirement already satisfied: wrapt>=1.11.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (1.16.0)   
Requirement already satisfied: requests<3,>=2.21.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (2.32.3)   
Requirement already satisfied: h5py>=3.10.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (3.11.0)   
Requirement already satisfied: setuptools in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (59.6.0)   
Requirement already satisfied: numpy<2.0.0,>=1.23.5 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorflow) (1.26.4)   
Requirement already satisfied: wheel<1.0,>=0.23.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from astunparse>=1.6.0->tensorflow) (0.44.0)   
Requirement already satisfied: optree in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from keras>=3.2.0->tensorflow) (0.12.1)   
Requirement already satisfied: rich in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from keras>=3.2.0->tensorflow) (13.7.1)   
Requirement already satisfied: namex in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from keras>=3.2.0->tensorflow) (0.0.8)   
Requirement already satisfied: idna<4,>=2.5 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorflow) (3.7)   
Requirement already satisfied: certifi>=2017.4.17 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorflow) (2024.7.4)   
Requirement already satisfied: urllib3<3,>=1.21.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorflow) (2.2.2)   
Requirement already satisfied: charset-normalizer<4,>=2 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorflow) (3.3.2)   
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorboard<2.18,>=2.17->tensorflow) (0.7.2)   
Requirement already satisfied: werkzeug>=1.0.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorboard<2.18,>=2.17->tensorflow) (3.0.3)   
Requirement already satisfied: markdown>=2.6.8 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from tensorboard<2.18,>=2.17->tensorflow) (3.6)   
Requirement already satisfied: MarkupSafe>=2.1.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from werkzeug>=1.0.1->tensorboard<2.18,>=2.17->tensorflow) (2.1.5)   
Requirement already satisfied: markdown-it-py>=2.2.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from rich->keras>=3.2.0->tensorflow) (3.0.0)   
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from rich->keras>=3.2.0->tensorflow) (2.18.0)   
Requirement already satisfied: mdurl~=0.1 in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich->keras>=3.2.0->tensorflow) (0.1.2)   
Installing collected packages: tensorflow   
^CERROR: Operation cancelled by user   
## (tfenv-wsl) hari@Hari-MSI:~\$ ^C   
## (tfenv-wsl) hari@Hari-MSI:~\$ pip install numpy protobuf grpcio   
Requirement already satisfied: numpy in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (1.26.4)   
Requirement already satisfied: protobuf in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (4.25.4)   
Requirement already satisfied: grpcio in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (1.65.4)   
## (tfenv-wsl) hari@Hari-MSI:~\$ pip install --upgrade pip setuptools   
Requirement already satisfied: pip in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (22.0.2)   
Collecting pip   
  Downloading pip-24.2-py3-none-any.whl (1.8 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 16.9 MB/s eta 0:00:00   
Requirement already satisfied: setuptools in /mnt/c/Users/hari_/venvs/tfenv-wsl/lib/python3.10/site-packages (59.6.0)   
Collecting setuptools   
  Downloading setuptools-72.2.0-py3-none-any.whl (2.3 MB)   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 31.0 MB/s eta 0:00:00   
Installing collected packages: setuptools, pip   
  Attempting uninstall: setuptools   
    Found existing installation: setuptools 59.6.0   
    Uninstalling setuptools-59.6.0:   
      Successfully uninstalled setuptools-59.6.0   
  Attempting uninstall: pip   
    Found existing installation: pip 22.0.2   
    Uninstalling pip-22.0.2:   
      Successfully uninstalled pip-22.0.2   
Successfully installed pip-24.2 setuptools-72.2.0   
   
   
# window 3   
   
C:\Users\hari_>conda activate tfenv-conwsl   
'conda' is not recognized as an internal or external command,   
operable program or batch file.   
   
C:\Users\hari_>wsl   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ exit   
logout   
   
C:\Users\hari_>wsl   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ mnt/d/   
-bash: mnt/d/: No such file or directory   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ cd mnt/d/github   
-bash: cd: mnt/d/github: No such file or directory   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ cd /mnt/d/github   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github\$ ls   
0-DELETE  1-Dasarpai-Projects  3-DevExp       5-Management    8-forked-repos  Dataset-Multimedia   
0-Junk    2-Solutions          4-MyDSCourses  6-My-Education  Dataset         workspaces   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github\$ cd 8-forked-repos/   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos\$ dir   
100Days-ML                               evalml                                  shapash   
GFPGAN                                   forked-repo-readmd.md\ -\ Shortcut.lnk  skorch   
Learning-Pandas-Second-Edition           gcp-python-docs-samples                 tensorboard   
LeetCode-js                              google-gemini-cookbook                  tensorflow   
ML+DL-Code-for-my-YouTube-Channel-Rohan  langchain                               tensorflow-examples   
Sandhi_Prakarana                         langgraph                               tfjs-examples   
chroma                                   pandasql   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos\$ cd tensorboard/   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ code .   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ conda install tensorflow-gpu   
Channels:   
 - defaults   
 - conda-forge   
Platform: linux-64   
Collecting package metadata (repodata.json): done   
Solving environment: | warning  libmamba Added empty dependency for problem type SOLVER_RULE_UPDATE   
done   
   
## Package Plan ##   
   
  environment location: /home/hari/miniconda3/envs/tfenv-conwsl   
   
  added / updated specs:   
    - tensorflow-gpu   
   
   
The following packages will be downloaded:   
   
    package                    |            build   
    ---------------------------|-----------------   
    c-ares-1.33.0              |       ha66036c_0         178 KB  conda-forge   
    cached-property-1.5.2      |             py_0          11 KB   
    cryptography-42.0.5        |  py311hdda0065_1         2.1 MB   
    cuda-crt-tools-12.4.131    |       h06a4308_0          25 KB   
    cuda-cudart-12.4.127       |       h99ab3db_0          21 KB   
    cuda-cudart_linux-64-12.4.127|       hd681fbe_0         207 KB   
    cuda-nvcc-tools-12.4.131   |       h99ab3db_0        24.9 MB   
    cuda-nvrtc-12.4.127        |       h99ab3db_1        19.8 MB   
    cuda-nvtx-12.4.127         |       h6a678d5_1          30 KB   
    cuda-nvvm-tools-12.4.131   |       h6a678d5_0        12.4 MB   
    cuda-version-12.4          |       hbda6634_3          19 KB   
    cudnn-8.9.7.29             |       h092f7fd_3       446.6 MB  conda-forge   
    giflib-5.2.2               |       hd590300_0          75 KB  conda-forge   
    grpcio-1.62.2              |  py311ha6695c7_0         1.0 MB  conda-forge   
    h5py-3.11.0                |nompi_py311h439e445_102         1.2 MB  conda-forge   
    hdf5-1.14.3                |nompi_hdf9ad27_105         3.7 MB  conda-forge   
    icu-75.1                   |       he02047a_0        11.6 MB  conda-forge   
    intel-openmp-2021.4.0      |    h06a4308_3561         4.2 MB   
    keras-3.4.1                |  py311h06a4308_0         2.8 MB   
    keyutils-1.6.1             |       h166bdaf_0         115 KB  conda-forge   
    krb5-1.21.3                |       h659f571_0         1.3 MB  conda-forge   
    libabseil-20240116.2       | cxx17_h6a678d5_0         1.3 MB   
    libaec-1.1.3               |       h59595ed_0          35 KB  conda-forge   
    libcublas-12.4.5.8         |       h99ab3db_1       247.6 MB   
    libcufft-11.2.1.3          |       h99ab3db_1       174.5 MB   
    libcurand-10.3.5.147       |       h99ab3db_1        42.4 MB   
    libcurl-8.9.1              |       hdb1bdb2_0         406 KB  conda-forge   
    libcusolver-11.6.1.9       |       h99ab3db_1        83.5 MB   
    libcusparse-12.3.1.170     |       h99ab3db_1       120.0 MB   
    libexpat-2.6.2             |       h59595ed_0          72 KB  conda-forge   
    libgfortran-ng-14.1.0      |       h69a702a_0          49 KB  conda-forge   
    libgfortran5-14.1.0        |       hc5f4f2c_0         1.4 MB  conda-forge   
    libgrpc-1.62.2             |       h15f2491_0         7.0 MB  conda-forge   
    libjpeg-turbo-3.0.3        |       h5eee18b_0         639 KB   
    libnghttp2-1.58.0          |       h47da74e_1         617 KB  conda-forge   
    libnsl-2.0.1               |       hd590300_0          33 KB  conda-forge   
    libnvjitlink-12.4.127      |       h99ab3db_1        17.4 MB   
    libpng-1.6.43              |       h2797004_0         281 KB  conda-forge   
    libprotobuf-4.25.3         |       h08a7969_0         2.7 MB  conda-forge   
    libre2-11-2023.09.01       |       h5a48ba9_2         227 KB  conda-forge   
    libsqlite-3.46.0           |       hde9e2c9_0         845 KB  conda-forge   
    libssh2-1.11.0             |       h0841786_0         265 KB  conda-forge   
    libstdcxx-ng-14.1.0        |       hc0a3c3a_0         3.7 MB  conda-forge   
    libuuid-2.38.1             |       h0b41bf4_0          33 KB  conda-forge   
    libxcrypt-4.4.36           |       hd590300_1          98 KB  conda-forge   
    libzlib-1.3.1              |       h4ab18f5_1          60 KB  conda-forge   
    markdown-it-py-2.2.0       |  py311h06a4308_1         145 KB   
    mdurl-0.1.0                |  py311h06a4308_0          22 KB   
    mkl-2021.4.0               |     h06a4308_640       142.6 MB   
    mkl-service-2.4.0          |  py311h5eee18b_0          53 KB   
    mkl_fft-1.3.1              |  py311h30b3d60_0         183 KB   
    mkl_random-1.2.2           |  py311hba01205_0         289 KB   
    ml_dtypes-0.4.0            |  py311ha02d727_0         171 KB   
    namex-0.0.7                |  py311h06a4308_0          16 KB   
    nccl-2.22.3.1              |       hbc370b7_1       107.2 MB  conda-forge   
    numpy-1.24.3               |  py311hc206e33_0          11 KB   
    numpy-base-1.24.3          |  py311hfd5febd_0         8.0 MB   
    openssl-3.3.1              |       h4bc722e_2         2.8 MB  conda-forge   
    optree-0.12.1              |  py311hdb19cb5_0         331 KB   
    pooch-1.7.0                |  py311h06a4308_0         106 KB   
    protobuf-4.25.3            |  py311h12ddb61_0         411 KB   
    pyopenssl-24.2.1           |  py311h06a4308_0         121 KB   
    python-3.11.8              |hab00c5b_0_cpython        29.3 MB  conda-forge   
    re2-2023.09.01             |       h7f4b329_2          26 KB  conda-forge   
    rich-13.7.1                |  py311h06a4308_0         624 KB   
    scipy-1.10.1               |  py311hc206e33_0        25.5 MB   
    sqlite-3.31.1              |       h7b6447c_0         1.1 MB   
    tensorboard-2.17.0         |  py311h06a4308_0         5.7 MB   
    tensorflow-2.17.0          |cuda120py311h51447cc_0          40 KB  conda-forge   
    tensorflow-base-2.17.0     |cuda120py311h013dac2_0       368.9 MB  conda-forge   
    tensorflow-estimator-2.17.0|cuda120py311h0c188d0_0         700 KB  conda-forge   
    tensorflow-gpu-2.17.0      |cuda120py311hb76ca00_0          39 KB  conda-forge   
    tk-8.6.13                  |noxft_h4845f30_101         3.2 MB  conda-forge   
    typing-extensions-4.11.0   |  py311h06a4308_0           9 KB   
    zlib-1.3.1                 |       h4ab18f5_1          91 KB  conda-forge   
    zstd-1.5.6                 |       ha6fb4c9_0         542 KB  conda-forge   
    ------------------------------------------------------------   
                                           Total:        1.89 GB   
   
The following NEW packages will be INSTALLED:   
   
  cached-property    pkgs/main/noarch::cached-property-1.5.2-py_0   
  cuda-crt-tools     pkgs/main/linux-64::cuda-crt-tools-12.4.131-h06a4308_0   
  cuda-cudart        pkgs/main/linux-64::cuda-cudart-12.4.127-h99ab3db_0   
  cuda-cudart_linux~ pkgs/main/noarch::cuda-cudart_linux-64-12.4.127-hd681fbe_0   
  cuda-nvcc-tools    pkgs/main/linux-64::cuda-nvcc-tools-12.4.131-h99ab3db_0   
  cuda-nvrtc         pkgs/main/linux-64::cuda-nvrtc-12.4.127-h99ab3db_1   
  cuda-nvtx          pkgs/main/linux-64::cuda-nvtx-12.4.127-h6a678d5_1   
  cuda-nvvm-tools    pkgs/main/linux-64::cuda-nvvm-tools-12.4.131-h6a678d5_0   
  cuda-version       pkgs/main/noarch::cuda-version-12.4-hbda6634_3   
  cudnn              conda-forge/linux-64::cudnn-8.9.7.29-h092f7fd_3   
  keyutils           conda-forge/linux-64::keyutils-1.6.1-h166bdaf_0   
  libabseil          pkgs/main/linux-64::libabseil-20240116.2-cxx17_h6a678d5_0   
  libaec             conda-forge/linux-64::libaec-1.1.3-h59595ed_0   
  libcublas          pkgs/main/linux-64::libcublas-12.4.5.8-h99ab3db_1   
  libcufft           pkgs/main/linux-64::libcufft-11.2.1.3-h99ab3db_1   
  libcurand          pkgs/main/linux-64::libcurand-10.3.5.147-h99ab3db_1   
  libcusolver        pkgs/main/linux-64::libcusolver-11.6.1.9-h99ab3db_1   
  libcusparse        pkgs/main/linux-64::libcusparse-12.3.1.170-h99ab3db_1   
  libexpat           conda-forge/linux-64::libexpat-2.6.2-h59595ed_0   
  libgrpc            conda-forge/linux-64::libgrpc-1.62.2-h15f2491_0   
  libjpeg-turbo      pkgs/main/linux-64::libjpeg-turbo-3.0.3-h5eee18b_0   
  libnsl             conda-forge/linux-64::libnsl-2.0.1-hd590300_0   
  libnvjitlink       pkgs/main/linux-64::libnvjitlink-12.4.127-h99ab3db_1   
  libre2-11          conda-forge/linux-64::libre2-11-2023.09.01-h5a48ba9_2   
  libsqlite          conda-forge/linux-64::libsqlite-3.46.0-hde9e2c9_0   
  libxcrypt          conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1   
  libzlib            conda-forge/linux-64::libzlib-1.3.1-h4ab18f5_1   
  markdown-it-py     pkgs/main/linux-64::markdown-it-py-2.2.0-py311h06a4308_1   
  mdurl              pkgs/main/linux-64::mdurl-0.1.0-py311h06a4308_0   
  ml_dtypes          pkgs/main/linux-64::ml_dtypes-0.4.0-py311ha02d727_0   
  namex              pkgs/main/linux-64::namex-0.0.7-py311h06a4308_0   
  nccl               conda-forge/linux-64::nccl-2.22.3.1-hbc370b7_1   
  optree             pkgs/main/linux-64::optree-0.12.1-py311hdb19cb5_0   
  pooch              pkgs/main/linux-64::pooch-1.7.0-py311h06a4308_0   
  rich               pkgs/main/linux-64::rich-13.7.1-py311h06a4308_0   
  tensorflow-gpu     conda-forge/linux-64::tensorflow-gpu-2.17.0-cuda120py311hb76ca00_0   
  typing-extensions  pkgs/main/linux-64::typing-extensions-4.11.0-py311h06a4308_0   
  zstd               conda-forge/linux-64::zstd-1.5.6-ha6fb4c9_0   
   
The following packages will be REMOVED:   
   
  abseil-cpp-20211102.0-hd4dd3e8_0   
  grpc-cpp-1.48.2-h5bf31a4_0   
  jpeg-9e-h5eee18b_3   
   
The following packages will be UPDATED:   
   
  c-ares                pkgs/main::c-ares-1.19.1-h5eee18b_0 --> conda-forge::c-ares-1.33.0-ha66036c_0   
  cryptography                       41.0.3-py311h130f0dd_0 --> 42.0.5-py311hdda0065_1   
  giflib                 pkgs/main::giflib-5.2.1-h5eee18b_3 --> conda-forge::giflib-5.2.2-hd590300_0   
  grpcio             pkgs/main::grpcio-1.48.2-py311h5bf31a~ --> conda-forge::grpcio-1.62.2-py311ha6695c7_0   
  h5py               pkgs/main::h5py-3.11.0-py311h865a13c_0 --> conda-forge::h5py-3.11.0-nompi_py311h439e445_102   
  hdf5                    pkgs/main::hdf5-1.12.1-h70be1eb_2 --> conda-forge::hdf5-1.14.3-nompi_hdf9ad27_105   
  icu                        pkgs/main::icu-58.2-he6710b0_3 --> conda-forge::icu-75.1-he02047a_0   
  keras                              2.12.0-py311h06a4308_0 --> 3.4.1-py311h06a4308_0   
  krb5                    pkgs/main::krb5-1.20.1-h568e23c_1 --> conda-forge::krb5-1.21.3-h659f571_0   
  libcurl               pkgs/main::libcurl-8.2.1-h91b91d3_0 --> conda-forge::libcurl-8.9.1-hdb1bdb2_0   
  libgfortran-ng     pkgs/main::libgfortran-ng-11.2.0-h003~ --> conda-forge::libgfortran-ng-14.1.0-h69a702a_0   
  libgfortran5       pkgs/main::libgfortran5-11.2.0-h12345~ --> conda-forge::libgfortran5-14.1.0-hc5f4f2c_0   
  libnghttp2         pkgs/main::libnghttp2-1.52.0-ha637b67~ --> conda-forge::libnghttp2-1.58.0-h47da74e_1   
  libpng                pkgs/main::libpng-1.6.39-h5eee18b_0 --> conda-forge::libpng-1.6.43-h2797004_0   
  libprotobuf        pkgs/main::libprotobuf-3.20.3-he621ea~ --> conda-forge::libprotobuf-4.25.3-h08a7969_0   
  libssh2              pkgs/main::libssh2-1.10.0-h37d81fd_2 --> conda-forge::libssh2-1.11.0-h0841786_0   
  libstdcxx-ng       pkgs/main::libstdcxx-ng-11.2.0-h12345~ --> conda-forge::libstdcxx-ng-14.1.0-hc0a3c3a_0   
  libuuid              pkgs/main::libuuid-1.41.5-h5eee18b_0 --> conda-forge::libuuid-2.38.1-h0b41bf4_0   
  numpy                              1.23.5-py311h08b1b3b_1 --> 1.24.3-py311hc206e33_0   
  numpy-base                         1.23.5-py311hf175353_1 --> 1.24.3-py311hfd5febd_0   
  openssl                                 1.1.1w-hd590300_0 --> 3.3.1-h4bc722e_2   
  protobuf                           3.20.3-py311h6a678d5_0 --> 4.25.3-py311h12ddb61_0   
  pyopenssl                          23.2.0-py311h06a4308_0 --> 24.2.1-py311h06a4308_0   
  python                pkgs/main::python-3.11.5-h7a1cb2a_0 --> conda-forge::python-3.11.8-hab00c5b_0_cpython   
  re2                  pkgs/main::re2-2022.04.01-h295c915_0 --> conda-forge::re2-2023.09.01-h7f4b329_2   
  tensorboard                        2.12.1-py311h06a4308_0 --> 2.17.0-py311h06a4308_0   
  tensorflow         pkgs/main::tensorflow-2.12.0-mkl_py31~ --> conda-forge::tensorflow-2.17.0-cuda120py311h51447cc_0   
  tensorflow-base    pkgs/main::tensorflow-base-2.12.0-mkl~ --> conda-forge::tensorflow-base-2.17.0-cuda120py311h013dac2_0   
  tensorflow-estima~ pkgs/main::tensorflow-estimator-2.12.~ --> conda-forge::tensorflow-estimator-2.17.0-cuda120py311h0c188d0_0   
  zlib                    pkgs/main::zlib-1.2.13-h5eee18b_1 --> conda-forge::zlib-1.3.1-h4ab18f5_1   
   
The following packages will be SUPERSEDED by a higher-priority channel:   
   
  certifi            conda-forge/noarch::certifi-2024.7.4-~ --> pkgs/main/linux-64::certifi-2024.7.4-py311h06a4308_0   
  tk                        pkgs/main::tk-8.6.14-h39e8969_0 --> conda-forge::tk-8.6.13-noxft_h4845f30_101   
   
The following packages will be DOWNGRADED:   
   
  intel-openmp                      2023.1.0-hdb19cb5_46306 --> 2021.4.0-h06a4308_3561   
  mkl                               2023.1.0-h213fc3f_46344 --> 2021.4.0-h06a4308_640   
  mkl-service                         2.4.0-py311h5eee18b_1 --> 2.4.0-py311h5eee18b_0   
  mkl_fft                             1.3.8-py311h5eee18b_0 --> 1.3.1-py311h30b3d60_0   
  mkl_random                          1.2.4-py311hdb19cb5_0 --> 1.2.2-py311hba01205_0   
  scipy                              1.13.1-py311h08b1b3b_0 --> 1.10.1-py311hc206e33_0   
  sqlite                                  3.45.3-h5eee18b_0 --> 3.31.1-h7b6447c_0   
   
   
Proceed ([y]/n)? y   
   
   
Downloading and Extracting Packages:   
   
Preparing transaction: done   
Verifying transaction: done   
Executing transaction: \ By downloading and using the cuDNN conda packages, you accept the terms and conditions of the NVIDIA cuDNN EULA -   
  https://docs.nvidia.com/deeplearning/cudnn/sla/index.html   
   
done   
```
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ code .   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ code .   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ code .   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/d/github/8-forked-repos/tensorboard\$ exit   
logout   
```
   
C:\Users\hari_>conda activate tfevn-conws   
'conda' is not recognized as an internal or external command,   
operable program or batch file.   
   
C:\Users\hari_>conda activate tfevn-conwsl   
'conda' is not recognized as an internal or external command,   
operable program or batch file.   
   
C:\Users\hari_>conda   
'conda' is not recognized as an internal or external command,   
operable program or batch file.   
   
C:\Users\hari_>wsl   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl   
```
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl^C   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda install --force-reinstall sqlite python   
Channels:   
 - defaults   
 - conda-forge   
Platform: linux-64   
Collecting package metadata (repodata.json): done   
Solving environment: done   
```
   
## Package Plan ##   
   
  environment location: /home/hari/miniconda3/envs/tfenv-conwsl   
   
  added / updated specs:   
    - python   
    - sqlite   
   
   
   
Proceed ([y]/n)? y   
   
   
Downloading and Extracting Packages:   
   
Preparing transaction: done   
Verifying transaction: done   
Executing transaction: done   
```
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda list --export > tfenv-conwsl-packages.txt   
```
conda remove --name tfenv-conwsl --all   
conda create --name tfenv-conwsl   
conda install --name tfenv-conwsl --file tfenv-conwsl-packages.txt   
   
CondaEnvironmentError: cannot remove current environment. deactivate and run conda remove again   
   
WARNING: A conda environment already exists at '/home/hari/miniconda3/envs/tfenv-conwsl'   
Remove existing environment (y/[n])? y   
   
Channels:   
 - defaults   
Platform: linux-64   
Collecting package metadata (repodata.json): \done   
Solving environment: done   
   
## Package Plan ##   
   
  environment location: /home/hari/miniconda3/envs/tfenv-conwsl   
   
   
   
Proceed ([y]/n)? y   
Invalid choice: yy   
Proceed ([y]/n)? y   
   
Preparing transaction: done   
Verifying transaction: done   
Executing transaction: done  
 
```   
# To activate this environment, use   
#   
#     \$ conda activate tfenv-conwsl   
#   
# To deactivate an active environment, use   
#   
#     \$ conda deactivate   
```
   
Channels:   
 - defaults   
Platform: linux-64   
Collecting package metadata (repodata.json): done   
Solving environment: failed   
   
LibMambaUnsatisfiableError: Encountered problems while solving:   
  - nothing provides requested zstd ==1.5.6 ha6fb4c9_0   
  - nothing provides requested zlib ==1.3.1 h4ab18f5_1   
  - nothing provides requested zipp ==3.20.0 pyhd8ed1ab_0   
  - nothing provides requested wcwidth ==0.2.13 pyhd8ed1ab_0   
  - nothing provides requested traitlets ==5.14.3 pyhd8ed1ab_0   
  - nothing provides requested tornado ==6.4.1 py311h331c9d8_0   
  - nothing provides requested tk ==8.6.13 noxft_h4845f30_101   
  - nothing provides requested tensorflow-gpu ==2.17.0 cuda120py311hb76ca00_0   
  - nothing provides requested tensorflow-estimator ==2.17.0 cuda120py311h0c188d0_0   
  - nothing provides requested tensorflow-base ==2.17.0 cuda120py311h013dac2_0   
  - nothing provides requested tensorflow ==2.17.0 cuda120py311h51447cc_0   
  - nothing provides requested stack_data ==0.6.2 pyhd8ed1ab_0   
  - nothing provides requested re2 ==2023.09.01 h7f4b329_2   
  - nothing provides requested python_abi ==3.11 2_cp311   
  - nothing provides requested python-dateutil ==2.9.0 pyhd8ed1ab_0   
  - nothing provides requested python ==3.11.8 hab00c5b_0_cpython   
  - nothing provides requested pygments ==2.18.0 pyhd8ed1ab_0   
  - nothing provides requested pure_eval ==0.2.3 pyhd8ed1ab_0   
  - nothing provides requested ptyprocess ==0.7.0 pyhd3deb0d_0   
  - nothing provides requested psutil ==6.0.0 py311h331c9d8_0   
  - nothing provides requested prompt-toolkit ==3.0.47 pyha770c72_0   
  - nothing provides requested platformdirs ==4.2.2 pyhd8ed1ab_0   
  - nothing provides requested pickleshare ==0.7.5 py_1003   
  - nothing provides requested pexpect ==4.9.0 pyhd8ed1ab_0   
  - nothing provides requested parso ==0.8.4 pyhd8ed1ab_0   
  - nothing provides requested openssl ==3.3.1 h4bc722e_2   
  - nothing provides requested nest-asyncio ==1.6.0 pyhd8ed1ab_0   
  - nothing provides requested nccl ==2.22.3.1 hbc370b7_1   
  - nothing provides requested matplotlib-inline ==0.1.7 pyhd8ed1ab_0   
  - nothing provides requested libzlib ==1.3.1 h4ab18f5_1   
  - nothing provides requested libxcrypt ==4.4.36 hd590300_1   
  - nothing provides requested libuuid ==2.38.1 h0b41bf4_0   
  - nothing provides requested libstdcxx-ng ==14.1.0 hc0a3c3a_0   
  - nothing provides requested libssh2 ==1.11.0 h0841786_0   
  - nothing provides requested libsqlite ==3.46.0 hde9e2c9_0   
  - nothing provides requested libsodium ==1.0.18 h36c2ea0_1   
  - nothing provides requested libre2-11 ==2023.09.01 h5a48ba9_2   
  - nothing provides requested libprotobuf ==4.25.3 h08a7969_0   
  - nothing provides requested libpng ==1.6.43 h2797004_0   
  - nothing provides requested libnsl ==2.0.1 hd590300_0   
  - nothing provides requested libnghttp2 ==1.58.0 h47da74e_1   
  - nothing provides requested libgrpc ==1.62.2 h15f2491_0   
  - nothing provides requested libgomp ==14.1.0 h77fa898_0   
  - nothing provides requested libgfortran5 ==14.1.0 hc5f4f2c_0   
  - nothing provides requested libgfortran-ng ==14.1.0 h69a702a_0   
  - nothing provides requested libgcc-ng ==14.1.0 h77fa898_0   
  - nothing provides requested libexpat ==2.6.2 h59595ed_0   
  - nothing provides requested libcurl ==8.9.1 hdb1bdb2_0   
  - nothing provides requested libaec ==1.1.3 h59595ed_0   
  - nothing provides requested krb5 ==1.21.3 h659f571_0   
  - nothing provides requested keyutils ==1.6.1 h166bdaf_0   
  - nothing provides requested jupyter_core ==5.7.2 py311h38be061_0   
  - nothing provides requested jupyter_client ==8.6.2 pyhd8ed1ab_0   
  - nothing provides requested jedi ==0.19.1 pyhd8ed1ab_0   
  - nothing provides requested ipython ==8.26.0 pyh707e725_0   
  - nothing provides requested ipykernel ==6.29.5 pyh3099207_0   
  - nothing provides requested importlib_metadata ==8.2.0 hd8ed1ab_0   
  - nothing provides requested importlib-metadata ==8.2.0 pyha770c72_0   
  - nothing provides requested icu ==75.1 he02047a_0   
  - nothing provides requested hdf5 ==1.14.3 nompi_hdf9ad27_105   
  - nothing provides requested h5py ==3.11.0 nompi_py311h439e445_102   
  - nothing provides requested grpcio ==1.62.2 py311ha6695c7_0   
  - nothing provides requested giflib ==5.2.2 hd590300_0   
  - nothing provides requested executing ==2.0.1 pyhd8ed1ab_0   
  - nothing provides requested exceptiongroup ==1.2.2 pyhd8ed1ab_0   
  - nothing provides requested decorator ==5.1.1 pyhd8ed1ab_0   
  - nothing provides requested cudnn ==8.9.7.29 h092f7fd_3   
  - nothing provides requested comm ==0.2.2 pyhd8ed1ab_0   
  - nothing provides requested ca-certificates ==2024.7.4 hbcca054_0   
  - nothing provides requested c-ares ==1.33.0 ha66036c_0   
  - nothing provides requested asttokens ==2.4.1 pyhd8ed1ab_0   
  - nothing provides requested _openmp_mutex ==4.5 2_gnu   
  - nothing provides requested _libgcc_mutex ==0.1 conda_forge   
  - package absl-py-2.1.0-py311h06a4308_0 requires python >=3.11,<3.12.0a0, but none of the providers can be installed   
   
Could not solve for environment specs   
The following packages are incompatible   
├─ _libgcc_mutex ==0.1 conda_forge does not exist (perhaps a typo or a missing channel);   
├─ _openmp_mutex ==4.5 2_gnu does not exist (perhaps a typo or a missing channel);   
├─ absl-py ==2.1.0 py311h06a4308_0 is installable and it requires   
│  └─ python >=3.11,<3.12.0a0  with the potential options   
│     ├─ python 3.11.0 would require   
│     │  └─ sqlite >=3.40.1,<4.0a0 , which can be installed;   
│     ├─ python 3.11.2 would require   
│     │  └─ sqlite >=3.41.1,<4.0a0 , which can be installed;   
│     └─ python [3.11.3|3.11.4|...|3.11.9] would require   
│        └─ sqlite >=3.41.2,<4.0a0 , which can be installed;   
├─ asttokens ==2.4.1 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ c-ares ==1.33.0 ha66036c_0 does not exist (perhaps a typo or a missing channel);   
├─ ca-certificates ==2024.7.4 hbcca054_0 does not exist (perhaps a typo or a missing channel);   
├─ comm ==0.2.2 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ cudnn ==8.9.7.29 h092f7fd_3 does not exist (perhaps a typo or a missing channel);   
├─ decorator ==5.1.1 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ exceptiongroup ==1.2.2 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ executing ==2.0.1 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ giflib ==5.2.2 hd590300_0 does not exist (perhaps a typo or a missing channel);   
├─ grpcio ==1.62.2 py311ha6695c7_0 does not exist (perhaps a typo or a missing channel);   
├─ h5py ==3.11.0 nompi_py311h439e445_102 does not exist (perhaps a typo or a missing channel);   
├─ hdf5 ==1.14.3 nompi_hdf9ad27_105 does not exist (perhaps a typo or a missing channel);   
├─ icu ==75.1 he02047a_0 does not exist (perhaps a typo or a missing channel);   
├─ importlib-metadata ==8.2.0 pyha770c72_0 does not exist (perhaps a typo or a missing channel);   
├─ importlib_metadata ==8.2.0 hd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ ipykernel ==6.29.5 pyh3099207_0 does not exist (perhaps a typo or a missing channel);   
├─ ipython ==8.26.0 pyh707e725_0 does not exist (perhaps a typo or a missing channel);   
├─ jedi ==0.19.1 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ jupyter_client ==8.6.2 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ jupyter_core ==5.7.2 py311h38be061_0 does not exist (perhaps a typo or a missing channel);   
├─ keyutils ==1.6.1 h166bdaf_0 does not exist (perhaps a typo or a missing channel);   
├─ krb5 ==1.21.3 h659f571_0 does not exist (perhaps a typo or a missing channel);   
├─ libaec ==1.1.3 h59595ed_0 does not exist (perhaps a typo or a missing channel);   
├─ libcurl ==8.9.1 hdb1bdb2_0 does not exist (perhaps a typo or a missing channel);   
├─ libexpat ==2.6.2 h59595ed_0 does not exist (perhaps a typo or a missing channel);   
├─ libgcc-ng ==14.1.0 h77fa898_0 does not exist (perhaps a typo or a missing channel);   
├─ libgfortran-ng ==14.1.0 h69a702a_0 does not exist (perhaps a typo or a missing channel);   
├─ libgfortran5 ==14.1.0 hc5f4f2c_0 does not exist (perhaps a typo or a missing channel);   
├─ libgomp ==14.1.0 h77fa898_0 does not exist (perhaps a typo or a missing channel);   
├─ libgrpc ==1.62.2 h15f2491_0 does not exist (perhaps a typo or a missing channel);   
├─ libnghttp2 ==1.58.0 h47da74e_1 does not exist (perhaps a typo or a missing channel);   
├─ libnsl ==2.0.1 hd590300_0 does not exist (perhaps a typo or a missing channel);   
├─ libpng ==1.6.43 h2797004_0 does not exist (perhaps a typo or a missing channel);   
├─ libprotobuf ==4.25.3 h08a7969_0 does not exist (perhaps a typo or a missing channel);   
├─ libre2-11 ==2023.09.01 h5a48ba9_2 does not exist (perhaps a typo or a missing channel);   
├─ libsodium ==1.0.18 h36c2ea0_1 does not exist (perhaps a typo or a missing channel);   
├─ libsqlite ==3.46.0 hde9e2c9_0 does not exist (perhaps a typo or a missing channel);   
├─ libssh2 ==1.11.0 h0841786_0 does not exist (perhaps a typo or a missing channel);   
├─ libstdcxx-ng ==14.1.0 hc0a3c3a_0 does not exist (perhaps a typo or a missing channel);   
├─ libuuid ==2.38.1 h0b41bf4_0 does not exist (perhaps a typo or a missing channel);   
├─ libxcrypt ==4.4.36 hd590300_1 does not exist (perhaps a typo or a missing channel);   
├─ libzlib ==1.3.1 h4ab18f5_1 does not exist (perhaps a typo or a missing channel);   
├─ matplotlib-inline ==0.1.7 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ nccl ==2.22.3.1 hbc370b7_1 does not exist (perhaps a typo or a missing channel);   
├─ nest-asyncio ==1.6.0 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ openssl ==3.3.1 h4bc722e_2 does not exist (perhaps a typo or a missing channel);   
├─ parso ==0.8.4 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ pexpect ==4.9.0 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ pickleshare ==0.7.5 py_1003 does not exist (perhaps a typo or a missing channel);   
├─ platformdirs ==4.2.2 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ prompt-toolkit ==3.0.47 pyha770c72_0 does not exist (perhaps a typo or a missing channel);   
├─ psutil ==6.0.0 py311h331c9d8_0 does not exist (perhaps a typo or a missing channel);   
├─ ptyprocess ==0.7.0 pyhd3deb0d_0 does not exist (perhaps a typo or a missing channel);   
├─ pure_eval ==0.2.3 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ pygments ==2.18.0 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ python-dateutil ==2.9.0 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ python ==3.11.8 hab00c5b_0_cpython does not exist (perhaps a typo or a missing channel);   
├─ python_abi ==3.11 2_cp311 does not exist (perhaps a typo or a missing channel);   
├─ re2 ==2023.09.01 h7f4b329_2 does not exist (perhaps a typo or a missing channel);   
├─ sqlite ==3.31.1 h7b6447c_0 is not installable because it conflicts with any installable versions previously reported;   
├─ stack_data ==0.6.2 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ tensorflow-base ==2.17.0 cuda120py311h013dac2_0 does not exist (perhaps a typo or a missing channel);   
├─ tensorflow-estimator ==2.17.0 cuda120py311h0c188d0_0 does not exist (perhaps a typo or a missing channel);   
├─ tensorflow-gpu ==2.17.0 cuda120py311hb76ca00_0 does not exist (perhaps a typo or a missing channel);   
├─ tensorflow ==2.17.0 cuda120py311h51447cc_0 does not exist (perhaps a typo or a missing channel);   
├─ tk ==8.6.13 noxft_h4845f30_101 does not exist (perhaps a typo or a missing channel);   
├─ tornado ==6.4.1 py311h331c9d8_0 does not exist (perhaps a typo or a missing channel);   
├─ traitlets ==5.14.3 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ wcwidth ==0.2.13 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ zipp ==3.20.0 pyhd8ed1ab_0 does not exist (perhaps a typo or a missing channel);   
├─ zlib ==1.3.1 h4ab18f5_1 does not exist (perhaps a typo or a missing channel);   
└─ zstd ==1.5.6 ha6fb4c9_0 does not exist (perhaps a typo or a missing channel).   

```   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda install --name tfenv-conwsl --file tfenv-conwsl-packages.txt^C   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda list --export > tfenv-conwsl-packages.txt   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda remove --name tfenv-conwsl --all   

   
CondaEnvironmentError: cannot remove current environment. deactivate and run conda remove again   
   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ deactivate   
deactivate: command not found   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ exit   
logout   
```   
C:\Users\hari_>conda remove --name tfenv-conwsl --all   
'conda' is not recognized as an internal or external command,   
operable program or batch file.   
   
C:\Users\hari_>wsl   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda remove --name tfenv-conwsl --all   
   
Remove all packages in environment /home/hari/miniconda3/envs/tfenv-conwsl:   
   
No packages found in /home/hari/miniconda3/envs/tfenv-conwsl. Continuing environment removal   
Everything found within the environment (/home/hari/miniconda3/envs/tfenv-conwsl), including any conda environment configurations and any non-conda files, will be deleted. Do you wish to continue?   
 (y/[n])? y   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda create --name tfenv-conwsl   
Channels:   
 - defaults   
Platform: linux-64   
Collecting package metadata (repodata.json): done   
Solving environment: done   
   
## Package Plan ##   
   
  environment location: /home/hari/miniconda3/envs/tfenv-conwsl   
   
   
   
Proceed ([y]/n)? y   
   
Preparing transaction: done   
Verifying transaction: done   
Executing transaction: done   
#   
# To activate this environment, use   
#   
#     $ conda activate tfenv-conwsl   
#   
# To deactivate an active environment, use   
#   
#     $ conda deactivate   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda install --name tfenv-conwsl --file tfenv-conwsl-packages.txt   
Channels:   
 - defaults   
Platform: linux-64   
Collecting package metadata (repodata.json): done   
Solving environment: done   
   
# All requested packages already installed.   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ nvcc --version   
nvcc: NVIDIA (R) Cuda compiler driver   
Copyright (c) 2005-2021 NVIDIA Corporation   
Built on Sun_Feb_14_21:12:58_PST_2021   
Cuda compilation tools, release 11.2, V11.2.152   
Build cuda_11.2.r11.2/compiler.29618528_0   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda list   
# packages in environment at /home/hari/miniconda3:   
#   
# Name                    Version                   Build  Channel   
_libgcc_mutex             0.1                        main   
_openmp_mutex             5.1                       1_gnu   
anaconda-anon-usage       0.4.4           py312hfc0e8ea_100   
archspec                  0.2.3              pyhd3eb1b0_0   
boltons                   23.0.0          py312h06a4308_0   
brotli-python             1.0.9           py312h6a678d5_8   
bzip2                     1.0.8                h5eee18b_6   
c-ares                    1.19.1               h5eee18b_0   
ca-certificates           2024.3.11            h06a4308_0   
certifi                   2024.6.2        py312h06a4308_0   
cffi                      1.16.0          py312h5eee18b_1   
charset-normalizer        2.0.4              pyhd3eb1b0_0   
conda                     24.5.0          py312h06a4308_0   
conda-content-trust       0.2.0           py312h06a4308_1   
conda-libmamba-solver     24.1.0             pyhd3eb1b0_0   
conda-package-handling    2.3.0           py312h06a4308_0   
conda-package-streaming   0.10.0          py312h06a4308_0   
cryptography              42.0.5          py312hdda0065_1   
distro                    1.9.0           py312h06a4308_0   
expat                     2.6.2                h6a678d5_0   
fmt                       9.1.0                hdb19cb5_1   
frozendict                2.4.2           py312h06a4308_0   
icu                       73.1                 h6a678d5_0   
idna                      3.7             py312h06a4308_0   
jsonpatch                 1.33            py312h06a4308_1   
jsonpointer               2.1                pyhd3eb1b0_0   
krb5                      1.20.1               h143b758_1   
ld_impl_linux-64          2.38                 h1181459_1   
libarchive                3.6.2                h6ac8c49_3   
libcurl                   8.7.1                h251f7ec_0   
libedit                   3.1.20230828         h5eee18b_0   
libev                     4.33                 h7f8727e_1   
libffi                    3.4.4                h6a678d5_1   
libgcc-ng                 11.2.0               h1234567_1   
libgomp                   11.2.0               h1234567_1   
libmamba                  1.5.8                hfe524e5_2   
libmambapy                1.5.8           py312h2dafd23_2   
libnghttp2                1.57.0               h2d74bed_0   
libsolv                   0.7.24               he621ea3_1   
libssh2                   1.11.0               h251f7ec_0   
libstdcxx-ng              11.2.0               h1234567_1   
libuuid                   1.41.5               h5eee18b_0   
libxml2                   2.10.4               hfdd30dd_2   
lz4-c                     1.9.4                h6a678d5_1   
menuinst                  2.1.1           py312h06a4308_0   
ncurses                   6.4                  h6a678d5_0   
openssl                   3.0.14               h5eee18b_0   
packaging                 23.2            py312h06a4308_0   
pcre2                     10.42                hebb0a14_1   
pip                       24.0            py312h06a4308_0   
platformdirs              3.10.0          py312h06a4308_0   
pluggy                    1.0.0           py312h06a4308_1   
pybind11-abi              5                    hd3eb1b0_0   
pycosat                   0.6.6           py312h5eee18b_1   
pycparser                 2.21               pyhd3eb1b0_0   
pysocks                   1.7.1           py312h06a4308_0   
python                    3.12.4               h5148396_1   
readline                  8.2                  h5eee18b_0   
reproc                    14.2.4               h6a678d5_2   
reproc-cpp                14.2.4               h6a678d5_2   
requests                  2.32.2          py312h06a4308_0   
ruamel.yaml               0.17.21         py312h5eee18b_0   
setuptools                69.5.1          py312h06a4308_0   
sqlite                    3.45.3               h5eee18b_0   
tk                        8.6.14               h39e8969_0   
tqdm                      4.66.4          py312he106c6f_0   
truststore                0.8.0           py312h06a4308_0   
tzdata                    2024a                h04d1e81_0   
urllib3                   2.2.2           py312h06a4308_0   
wheel                     0.43.0          py312h06a4308_0   
xz                        5.4.6                h5eee18b_1   
yaml-cpp                  0.8.0                h6a678d5_1   
zlib                      1.2.13               h5eee18b_1   
zstandard                 0.22.0          py312h2c38b39_0   
zstd                      1.5.5                hc292b87_2   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda   
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...   
   
conda is a tool for managing and deploying applications, environments and packages.   
   
options:   
  -h, --help          Show this help message and exit.   
  -v, --verbose       Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG   
                      logging, four times for TRACE logging.   
  --no-plugins        Disable all plugins that are not built into conda.   
  -V, --version       Show the conda version number and exit.   
   
commands:   
  The following built-in and plugins subcommands are available.   
   
  COMMAND   
    activate          Activate a conda environment.   
    clean             Remove unused packages and caches.   
    compare           Compare packages between conda environments.   
    config            Modify configuration values in .condarc.   
    content-trust     Signing and verification tools for Conda   
    create            Create a new conda environment from a list of specified packages.   
    deactivate        Deactivate the current active conda environment.   
    doctor            Display a health report for your environment.   
    export            Export a given environment   
    info              Display information about current conda install.   
    init              Initialize conda for shell interaction.   
    install           Install a list of packages into a specified conda environment.   
    list              List installed packages in a conda environment.   
    notices           Retrieve latest channel notifications.   
    package           Create low-level conda packages. (EXPERIMENTAL)   
    remove (uninstall)   
                      Remove a list of packages from a specified conda environment.   
    rename            Rename an existing environment.   
    repoquery         Advanced search for repodata.   
    run               Run an executable in a conda environment.   
    search            Search for packages and display associated information using the MatchSpec format.   
    update (upgrade)  Update conda packages to the latest compatible version.   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda doctor   
Environment Health Report for: /home/hari/miniconda3   
   
Altered Files:   
   
✅ There are no packages with altered files.   
   
Environment listed in environments.txt file: ✅   
   
Missing Files:   
   
✅ There are no packages with missing files.   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda info   
   
     active environment : base   
    active env location : /home/hari/miniconda3   
            shell level : 1   
       user config file : /home/hari/.condarc   
 populated config files :   
          conda version : 24.5.0   
    conda-build version : not installed   
         python version : 3.12.4.final.0   
                 solver : libmamba (default)   
       virtual packages : __archspec=1=skylake   
                          __conda=24.5.0=0   
                          __cuda=12.5=0   
                          __glibc=2.35=0   
                          __linux=5.15.153.1=0   
                          __unix=0=0   
       base environment : /home/hari/miniconda3  (writable)   
      conda av data dir : /home/hari/miniconda3/etc/conda   
  conda av metadata url : None   
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64   
                          https://repo.anaconda.com/pkgs/main/noarch   
                          https://repo.anaconda.com/pkgs/r/linux-64   
                          https://repo.anaconda.com/pkgs/r/noarch   
          package cache : /home/hari/miniconda3/pkgs   
                          /home/hari/.conda/pkgs   
       envs directories : /home/hari/miniconda3/envs   
                          /home/hari/.conda/envs   
               platform : linux-64   
             user-agent : conda/24.5.0 requests/2.32.2 CPython/3.12.4 Linux/5.15.153.1-microsoft-standard-WSL2 ubuntu/22.04.3 glibc/2.35 solver/libmamba conda-libmamba-solver/24.1.0 libmambapy/1.5.8 aau/0.4.4 c/. s/. e/.   
                UID:GID : 1000:1000   
             netrc file : None   
           offline mode : False   
   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda env list   
# conda environments:   
#   
base                  *  /home/hari/miniconda3   
tfenv-conwsl             /home/hari/miniconda3/envs/tfenv-conwsl   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl-packages.txt   
.android/   
.aws/   
.azure/   
.bash_history   
.boto   
.bundle/   
.cache/   
.chocolatey/   
.config/   
.docker/   
.emulator_console_auth_token   
.gitconfig   
.gradle/   
.ipython/   
.javacpp/   
.jupyter/   
.keras/   
.local/   
.matplotlib/   
.ms-ad/   
.node_repl_history   
.ollama/   
.ssh/   
.vscode/   
.windows-build-tools/   
.wslconfig   
.yarnrc   
AppData/   
Application Data/   
Contacts/   
Cookies/   
Documents/   
--More--                                                                                  ^C   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda env list   
# conda environments:   
#   
base                  *  /home/hari/miniconda3   
tfenv-conwsl             /home/hari/miniconda3/envs/tfenv-conwsl   
   
## (base) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda activate tfenv-conwsl   
(tfenv-conwsl) ## hari@Hari-MSI:/mnt/c/Users/hari_$ conda list   
   
   
   
