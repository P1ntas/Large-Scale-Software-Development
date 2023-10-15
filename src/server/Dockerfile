# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y libpq-dev gcc

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["python", "flask_server.py"]

# Define environment variable
#ENV FLASK_APP=flask_server.py

# Run app.py when the container launches
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
