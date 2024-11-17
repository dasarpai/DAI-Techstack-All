
# COG
Cog: Containers for machine learning
Cog is an open-source tool that lets you package machine learning models in a standard, production-ready container.

You can deploy your packaged model to your own infrastructure, or to Replicate.

Highlights
📦 Docker containers without the pain. Writing your own Dockerfile can be a bewildering process. With Cog, you define your environment with a simple configuration file and it generates a Docker image with all the best practices: Nvidia base images, efficient caching of dependencies, installing specific Python versions, sensible environment variable defaults, and so on.

🤬️ No more CUDA hell. Cog knows which CUDA/cuDNN/PyTorch/Tensorflow/Python combos are compatible and will set it all up correctly for you.

✅ Define the inputs and outputs for your model with standard Python. Then, Cog generates an OpenAPI schema and validates the inputs and outputs with Pydantic.

🎁 Automatic HTTP prediction server: Your model's types are used to dynamically generate a RESTful HTTP API using FastAPI.

🥞 Automatic queue worker. Long-running deep learning models or batch processing is best architected with a queue. Cog models do this out of the box. Redis is currently supported, with more in the pipeline.

☁️ Cloud storage. Files can be read and written directly to Amazon S3 and Google Cloud Storage. (Coming soon.)

🚀 Ready for production. Deploy your model anywhere that Docker images run. Your own infrastructure, or Replicate.


Running cog on Windows is now possible thanks to WSL 2. Follow this guide to enable WSL 2 and GPU passthrough on Windows 11.

## Why Cog?
It's really hard for researchers to ship machine learning models to production.

Part of the solution is Docker, but it is so complex to get it to work: Dockerfiles, pre-/post-processing, Flask servers, CUDA versions. More often than not the researcher has to sit down with an engineer to get the damn thing deployed.

Andreas and Ben created Cog. Andreas used to work at Spotify, where he built tools for building and deploying ML models with Docker. Ben worked at Docker, where he created Docker Compose.

## Prerequisites
macOS, Linux or Windows 11. Cog works on macOS, Linux and Windows 11 with WSL 2
Docker. Cog uses Docker to create a container for your model. You'll need to install Docker before you can run Cog. If you install Docker Engine instead of Docker Desktop, you will need to install Buildx as well.

## Using cog on Windows 11 with WSL 2
1. Install the GPU driver
2. Unlocking features
	- at admin terminal: dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
	- enable virtulization: dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
3. Update MS Linux kernel
	- wsl cat /proc/version
4. Configure WSL 2
	- wsl --set-default-version 2
5. Configure CUDA WSL-Ubuntu Toolkit
	- wsl.exe 
6. Install Docker
7. Install cog and pull an image
	- sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`
	- sudo chmod +x /usr/local/bin/cog
8. Run a model in WSL 2
	- cog predict 'r8.im/afiaka87/glid-3-xl' -i prompt="a fresh avocado floating in the water" -o prediction.json
	This model just barely manages to fit under 8 GB of VRAM.   
	Notice that output is returned as JSON for this model as it has a complex return type. You will want to convert the base64 string in the json array to an image.   
	jq can help with this:
	- sudo apt install jq
	- The following bash uses jq to grab the first element in our prediction array and converts it from a base64 string to a png file.
	- jq -cs '.[0][0][0]' prediction.json | cut --delimiter "," --field 2 | base64 --ignore-garbage --decode > prediction.png

## Commands 

sudo apt install jq

## Resources
- https://github.com/replicate/cog?tab=readme-ov-file
- https://github.com/replicate/cog/blob/main/docs/wsl2/wsl2.md

