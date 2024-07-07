# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry install

# Copy the rest of the application code
COPY src /app/src

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "src/app/app.py"]