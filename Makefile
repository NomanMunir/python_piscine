IMAGE_NAME = piscine-python
CONTAINER_NAME = piscine-container

all: build

build:
	docker build -t $(IMAGE_NAME) .

up:
	docker run -it --rm -v $${PWD}:/app --name $(CONTAINER_NAME) $(IMAGE_NAME)

up-compose:
	docker-compose up --build

down:
	docker-compose down

clean:
	docker rmi -f $(IMAGE_NAME) || true

flake:
	@flake8 ex*/*

fclean: clean
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true

re: fclean all
