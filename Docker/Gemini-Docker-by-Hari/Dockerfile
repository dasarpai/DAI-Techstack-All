# Start with an official Python image with a stable version
FROM python:3.10

# Set environment variables for Python (optional, helps with debugging and prevents .pyc files)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Jupyter Notebook and required Python libraries
RUN pip install --upgrade pip
RUN pip install \
    jupyter \
    pandas \
    numpy \
    scikit-learn \
    matplotlib \
    seaborn \
    tensorflow \
    torch \
    transformers \
    google-auth \
    google-auth-oauthlib \
    google-auth-httplib2 \
    google-api-python-client

# Create a working directory
WORKDIR /workspace

# Expose the Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook on port 8888 accessible from any IP (0.0.0.0)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# export GOOGLE_API_KEY 
# then execute this code on wsl 
# docker run -p 8888:8888 -v /mnt/d/github/Dia-forked/google-gemini-cookbook/:/workspace/data -e GOOGLE_API_KEY=($GOOGLE_API_KEY) gemini-genai-notebook
