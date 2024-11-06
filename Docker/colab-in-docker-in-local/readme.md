https://hub.docker.com/r/sorokine/docker-colab-local

docker pull sorokine/docker-colab-local

docker run --runtime=nvidia -it --rm -p 8081:8081 sorokine/docker-colab-local:latest

with volume
$ docker run --runtime=nvidia -it --rm -p 8081:8081 -v "$PWD":/opt/colab sorokine/docker-colab-local:latest

with GPU 
$ docker run --runtime=nvidia -it --rm -p 8081:8081 -v "$PWD":/opt/colab -v $HOME/.cache/torch:/root/.cache/torch sorokine/docker-colab-local:10.1

docker run --runtime=nvidia -it --rm -p 8081:8081 -v "$PWD":/opt/colab -v $HOME/.cache/torch:/root/.cache/torch sorokine/docker-colab-local:10.1

nvidia-smi

if some packages are missing install them with !pip install in your notebook. This has to be repeated on kernel restart.


