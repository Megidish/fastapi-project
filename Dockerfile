FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the contents of the app directory to /app in the container
COPY ./app /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python", "main.py"]
