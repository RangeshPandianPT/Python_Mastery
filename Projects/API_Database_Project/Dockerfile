# Use official Python lightweight image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file (we will just copy everything and install)
COPY . /app

# Install dependencies (assuming standard ones for FastAPI + SQLite)
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
