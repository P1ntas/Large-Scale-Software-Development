#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null
then
    echo "Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

# Run Docker Compose
docker-compose up -d
echo "Finalized Docker Compose"

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Install the required Python packages
pip install -r config/requirements.txt

echo "Waiting for the database to be ready..."
# Run the Python script
python main.py

echo "Finalized pushing data to the database"