# Use official Python 3.10 image
FROM python:3.10-slim

# Metadata (optional)
LABEL maintainer="Nauman_Munir nmunir@student.42abudhabi.ae"

# Set working directory inside container
WORKDIR /app

# Copy requirements if needed (optional)
# COPY requirements.txt .

# Install build tools including make
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["bash"]
