# 🐍 Use Python base image
FROM python:3.11-slim

# 📁 Set working directory
WORKDIR /app

# 📦 Copy local files into the container
COPY . .

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🚀 Default command
CMD ["python", "app.py"]
