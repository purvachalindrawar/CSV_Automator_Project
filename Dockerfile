# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your app
CMD ["python", "app.py"]
