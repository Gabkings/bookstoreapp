# Pull base image 
FROM  python:3.6

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies 

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# copy the project 

COPY . /code/
