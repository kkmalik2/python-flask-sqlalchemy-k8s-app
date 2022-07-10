# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /python-docker

ARG A_LOG_FILE_PATH='persistedVolume/app.log'
ENV LOG_FILE_PATH=${ARG}
ENV DATABASE_TYPE='sqlite'
ENV DATABASE_LOCATION='persistedVolume/user-pref.db'


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

# docker build --build-arg A_LOG_FILE_PATH="app1.log" -t kanishkmalik/kk-flask-app-k8s .

# docker run -e "LOG_FILE_PATH=app1.log" -d -p 5000:5000 kanishkmalik/kk-flask-app-k8s
# docker exec -it 5fe329049efdcbceb10fe80cc00e519f1d1a095c7dbcd98bf18c4d58b6022fbb /bin/bash  -- Open bash in Container
# tail app1.log -f  -- Check file in container
# docker container stop 5fe329049efdcbceb10fe80cc00e519f1d1a095c7dbcd98bf18c4d58b6022fbb  -- Stops running container

# docker 
# docker run -d --rm -v applogs:/python-docker -e "LOG_FILE_PATH=app1.log"  -p 5000:5000 kanishkmalik/kk-flask-app-k8s

# docker run -d --rm -v applogs:/python-docker -e "LOG_FILE_PATH=app1.log" -e "DATABASE_LOCATION=/python-docker/app-db/user-pref.db" -p 5000:5000 kanishkmalik/kk-flask-app-k8s

# docker run --name kk-docker-app -d -e "LOG_FILE_PATH=app1.log" -e "DATABASE_LOCATION=/python-docker/app-db/user-pref.db" -p 5000:5000 kanishkmalik/kk-flask-app-k8s

# docker run --name kk-docker-app -d -e "LOG_FILE_PATH=app1.log" -e "DATABASE_LOCATION=user-pref-docker.db" -p 5000:5000 kanishkmalik/kk-flask-app-k8s

# docker run --name kk-docker-app -d -e "LOG_FILE_PATH=app1.log" -p 5000:5000 kanishkmalik/kk-flask-app-k8s

# docker volume create <volume-name>

# # Run docker container with persistent volume mount. State is saved and multiple containers can be run using same db and log file. 
# docker build -t kanishkmalik/kk-flask-app-k8s .
# docker build --build-arg A_LOG_FILE_PATH="persistedVolume/app1.log" -t kanishkmalik/kk-flask-app-k8s .
# docker run -d --rm -v app-db-and-logs:/python-docker/persistedVolume -p 5000:5000 kanishkmalik/kk-flask-app-k8s
