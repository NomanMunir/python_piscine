FROM python:3.10-slim-bullseye

# Update package lists first
RUN apt update -y && \
    # Install dependencies with --no-install-recommends to reduce size
    apt install -y --no-install-recommends \
    git \
    wget \
    curl \
    vim \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flake8 tqdm setuptools

WORKDIR /app
CMD ["/bin/bash"]