FROM python:3.11.5-alpine

EXPOSE 8000

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt