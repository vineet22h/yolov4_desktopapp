FROM python:3.7.11

RUN apt-get update 
# RUN apt install python3-opencv -y
RUN apt-get install ffmpeg libsm6 libxext6 -y

WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/app
ENTRYPOINT ["python3"]
CMD ["main.py"]
