FROM python:3.7.11-slim

RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/app
ENTRYPOINT ["python3", "main.py"]