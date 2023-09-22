# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

# Copy the source code and and store it in a folder named app
ADD . /app

# Set the working directory to /app
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port 5000
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
