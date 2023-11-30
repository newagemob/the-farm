# Use Python image as base
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set working directory in the container
WORKDIR /app

# Install required packages
RUN pip install -r requirements.txt
# Install local package
RUN pip install -e .

# Install Firefox and GeckoDriver
RUN apt-get update && apt-get install -y firefox-esr
RUN apt-get install -y wget

# Run the Python script
CMD ["python", "src/bot.py"]
