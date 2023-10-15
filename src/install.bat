@echo off

:: Check if Docker is installed
where docker >nul 2>nul
if %errorlevel% neq 0 (
    echo Docker is not installed. Please install Docker and try again.
    exit /b
)

:: Check if Docker Compose is installed
where docker-compose >nul 2>nul
if %errorlevel% neq 0 (
    echo Docker Compose is not installed. Please install Docker Compose and try again.
    exit /b
)

:: Run Docker Compose
docker-compose up -d

echo Finalized Docker Compose

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

:: Check if pip is installed
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and try again.
    exit /b
)

:: Install the required Python packages
pip install -r config\requirements.txt

echo Waiting for the database to be ready...
:: Run the Python script
python main.py

echo Finalized pushing data to the database