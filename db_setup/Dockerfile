# Use an official Python runtime as a parent image
FROM python:3.8

# Install Flask and other dependencies
RUN pip install -r requirements.txt

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements into the container at /app
# COPY requirements.txt .



# # Copy the project contents into the container at /app
# COPY ./app .

# # Expose port 5000 for Flask
# EXPOSE 5000

# # Define the command to run when the container starts
# CMD ["python", "app.py"]

# FROM postgres:latest
# RUN #!/bin/bash && set -e && export PGPASSWORD=$POSTGRES_PASSWORD;
# RUN psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -W -h "root" -d "$POSTGRES_DB"
# RUN \i schema.sql

# EXPOSE 5432
# COPY ./schema.sql /docker-entrypoint-initdb.d/config.sql