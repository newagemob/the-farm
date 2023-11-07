# Use a basic Ubuntu image as the parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Update and install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Firefox and Geckodriver
RUN apt-get update && apt-get install -y wget bzip2 libxtst6 libgtk-3-0 libx11-xcb-dev libdbus-glib-1-2 libxt6 libpci-dev && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y firefox
RUN apt-get install -y wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.33.0-linux64.tar.gz
RUN chmod +x ./geckodriver
RUN mv geckodriver /usr/local/bin/
RUN export PATH=$PATH:/usr/local/bin/geckodriver

# Install any needed Python packages specified in requirements.txt and local modules
RUN pip install -r requirements.txt
RUN pip install -e .

# Run your SoundCloud bot when the container starts
CMD ["python3", "src/main.py"]
