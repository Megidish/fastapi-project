# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable to indicate the application is listening on port 8000
ENV PORT=8000

# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run the application
CMD ["python", "main.py"]
