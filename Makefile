# Variables
IMAGE_NAME = piscine-python
CONTAINER_NAME = piscine-container

# Default rule
all: build

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run Docker container with volume mount
up:
	docker run -it --rm -v $${PWD}:/app --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Run container using docker-compose
up-compose:
	docker-compose up --build

# Stop docker-compose (if used)
down:
	docker-compose down

# Clean just Docker image
clean:
	docker rmi -f $(IMAGE_NAME) || true

flake8:
	flake8 ex*/*

# Full clean: image + Python bytecode
fclean: clean
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true

# Rebuild everything
re: fclean all
