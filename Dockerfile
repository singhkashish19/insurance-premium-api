# use python 3.11 - Base Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of application code
COPY . .

# Expose the application port
EXPOSE 8000

# command to start FastAPI Application
CMD [ "uvicorn", 'app:app', '--host', '0.0.0.0', '--port', '8000' ]



