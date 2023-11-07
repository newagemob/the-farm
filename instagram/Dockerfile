# Use the official Python image as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install Firefox and GeckoDriver
RUN apt-get update && apt-get install -y firefox-esr
RUN apt-get install -y wget

# run the creds.sh script to set the environment variables
RUN chmod +x ./creds.sh
RUN ./creds.sh

# Run your Instagram bot when the container starts
CMD ["python", "src/main.py"]
