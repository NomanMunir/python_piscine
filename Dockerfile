FROM python:3.10-slim

LABEL maintainer="Nauman_Munir nmunir@student.42abudhabi.ae"

WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
