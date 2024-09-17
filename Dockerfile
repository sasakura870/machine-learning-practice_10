FROM python:3.9.20-slim-bullseye

WORKDIR /app
COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
