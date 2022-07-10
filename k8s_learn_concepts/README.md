# Rough Notes

## python-flask-sqlalchemy-app

To run directly in local, python .\run.py 

# Run below commands in terminal to Dockerize the run it in local
### docker build -t kanishkmalik/kk-flask-app .
### docker run -d -p 5000:5000 kanishkmalik/kk-flask-app
### docker run --name kk-app -d -p 5001:5000 kanishkmalik/kk-flask-app
### In Local web browser, enter localhost:5001 to see the app
### Remove the image - docker rmi -f  kanishkmalik/kk-flask-app 


# Run below commands in terminal to run it on Kubernetes
### kubectl apply -f k-deployment.yaml
### kubectl apply -f k-service.yaml
### NodePort 30007 is opened. 
### In Local web browser, enter localhost:30007 to see the app

With Docker, you can save the state in a volume. 

# docker volume create <volume-name>

# # Run docker container with persistent volume mount. State is saved and multiple containers can be run using same db and log file. 
### docker build -t kanishkmalik/kk-flask-app-k8s .  Note that Docoker file is updated to use environment variables and application uses those environment variables to save database information and logs.
### docker build --build-arg A_LOG_FILE_PATH="persistedVolume/app1.log" -t kanishkmalik/kk-flask-app-k8s .     This argument A_LOG_FILE_PATH is referred internally by envt. variable in Dockerfile.
### docker run -d --rm -v app-db-and-logs:/python-docker/persistedVolume -p 5000:5000 kanishkmalik/kk-flask-app-k8s   ... Mounting container folder /python-docker/persistedVolume on app-db-and-logs volume. 

## Same volume concept is explored with K8s. Details mentioned below.

# K8S_LEARN_CONCEPTS folder is created to test K8s kubernetes configMap, Persistent Volume and claims, and use persistent volumes in Deployment
###  kubectl create -f .\k-configmap.yaml
### kubectl apply -f .\k-configmap.yaml  -- If any service already exists, use apply instead of create.

### kubectl get storageclass #Find out the storage classes available to mount Volume. Use that storage class while creating Persistent volume (line 8 in this example)

### kubectl create -f .\k-persistent-volume.yaml
### kubectl get pv  -- see the persistent volume that is created. Next step is to create claim.
### kubectl create -f .\k-persistent-volume-claim.yaml   -- Namespace specific. Default namespace is used in this application.

### Volume Mounts and Volumes are specified in Deployment File.  Stateful sets is a better option, but have not explored yet. For now, using deployments to run the application.
### kubectl create -f .\k-deployment-volume-claim.yaml
### kubectl create -f .\k-service.yaml

### If we remove container, or delete deployment; logs and database file is preserved on the volume and is persisted.  Note to mount the path that you want to persist in container in your Deployment file. (Line 28 in this example)

