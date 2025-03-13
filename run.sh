#!/bin/bash

# Docker control script for 42 Abu Dhabi Python Piscine
# Usage: ./run.sh [--build] [command]

IMAGE_NAME="python-piscine"
CONTAINER_NAME="piscine-container"
VOLUME_MOUNT="$(pwd):/app"
WORKDIR="/app"

# Build the Docker image (if --build is passed or image doesn't exist)
build_image() {
    echo "Building Docker image..."
    docker build -t $IMAGE_NAME . || {
        echo "Error building Docker image!"
        exit 1
    }
}

# Run the container with bind mount
run_container() {
    echo "Starting Docker container..."
    docker run -it --rm \
        --name $CONTAINER_NAME \
        -v $VOLUME_MOUNT \
        -w $WORKDIR \
        $IMAGE_NAME "$@"
}

# Main script execution
if [ "$1" == "--build" ]; then
    build_image
    shift
elif ! docker image inspect $IMAGE_NAME &> /dev/null; then
    echo "Image not found, building..."
    build_image
fi

# Run with remaining arguments as command
run_container "$@"