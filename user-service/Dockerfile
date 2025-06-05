# Dockerfile for user-service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy service files
COPY user-service/ /app

EXPOSE 5000

# Override port to 5000 by setting environment variable and running app
ENV FLASK_RUN_PORT=5000
CMD ["python", "app.py", "--port=5000"]
