#!/bin/sh

# Check if Docker Compose is installed
if ! command -v docker-compose >/dev/null 2>&1
then
    echo "Docker Compose could not be found. Please install it first."
    exit 1
fi

echo "Docker Compose is not running. Building and starting..."
docker compose down -v --remove-orphans --rmi
docker-compose up --build -d Mongo
