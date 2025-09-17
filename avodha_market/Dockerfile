# first stage - use python slim base image
FROM python:3.13 AS builder

# create app directory
RUN mkdir /app

# set working directory in the container
WORKDIR /app

# set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# upgrade pip
RUN pip install --upgrade pip

# copy project files into the container
COPY requirements.txt /app/

# install all the required packages
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# second stage
FROM python:3.13-slim

# Copy the Python dependencies from the builder stage
COPY --from=builder /install /usr/local

# Set the working directory
WORKDIR /app

# Create /static folder inside the container
RUN mkdir static

# Copy application code
COPY . /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set environment variables
ENV DEBUG=False
ENV ALLOWED_HOSTS=127.0.0.1,localhost

# Expose the Django port
EXPOSE 8000

# set entrypoint.sh executable
RUN chmod +x ./entrypoint.sh

# run django server
ENTRYPOINT ["./entrypoint.sh"]
