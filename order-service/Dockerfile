# Dockerfile for order-service
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for cryptography and MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY order-service/ /app

EXPOSE 5000

ENV FLASK_RUN_PORT=5000
CMD ["python", "app.py", "--port=5000"]
