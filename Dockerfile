# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["python3","./run.py","--host=0.0.0.0"]

CMD ["python3","./run.py"]

#### Run below commands in terminal
# docker build -t kanishkmalik/kk-flask-app .
# docker run -d -p 5000:5000 kanishkmalik/kk-flask-app
# docker run --name kk-app -d -p 5001:5000 kanishkmalik/kk-flask-app
# docker rmi -f  kanishkmalik/kk-flask-app 