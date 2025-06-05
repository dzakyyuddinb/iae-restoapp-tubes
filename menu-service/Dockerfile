# Dockerfile for menu-service
FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY menu-service/ /app

EXPOSE 5000

ENV FLASK_RUN_PORT=5000
CMD ["python", "app.py", "--port=5000"]
