#!/bin/bash

# Define your image and container names
IMAGE_NAME=escravo-do-hugo
CONTAINER_NAME=discord-bot

echo "🚧 Stopping and removing any existing container..."
docker rm -f $CONTAINER_NAME 2>/dev/null || true

echo "📦 Building Docker image..."
docker build -t $IMAGE_NAME .

echo "🚀 Running container..."
docker run --env-file .env --name $CONTAINER_NAME $IMAGE_NAME
