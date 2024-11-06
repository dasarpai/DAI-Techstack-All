# Use the TensorFlow image as the base
FROM tensorflow/tensorflow:latest

# Create a new user and group
RUN groupadd -r hari && useradd -r -g hari hari

# Set the user
USER hari

# Set the working directory
WORKDIR /home/hari

# Run the container
CMD ["bash"]