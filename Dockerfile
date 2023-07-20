# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Python optimizations and unbuffered output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install the app dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY . .

# Expose the port your Flask app will listen on
EXPOSE 5000

# Command to run your Flask app using Gunicorn (adjust as needed)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
