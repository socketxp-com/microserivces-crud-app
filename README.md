# microserivces-crud-app
A microservices based CRUD app that implements a student database written in python, nodejs, and html with Postgresql DB

## Overview of the microservices
Frontend(Port 3000)  -->  Backend(Port 5000)  -->  Postgres DB (Port 5432)

## Pre-requisites

Install postgresdb locally on your laptop or server.  [Alternatively you could run a postgresDB docker container and make it use the host network via the "--net host" option of the docker run command.]

Add the following entries to your /etc/hosts file in your laptop or server:

``` sh
...
127.0.0.1  frontend
127.0.0.1  backend
127.0.0.1  postgres
```

To access the frontend, point your browser to http://frontend:3000

It will open up a html form.  You can add and delete students information there.  It will display the updated DB in realtime.

