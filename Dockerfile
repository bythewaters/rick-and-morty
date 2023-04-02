FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DOCKER_CONTAINER=1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -U pip && pip install -r requirements.txt

COPY . /app/
