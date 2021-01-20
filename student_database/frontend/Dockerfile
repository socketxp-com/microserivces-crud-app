FROM centos:latest
RUN yum install -y nodejs
RUN mkdir -p /usr/src/app
COPY ./httpserver.js /usr/src/app
COPY ./index.html /usr/src/app
WORKDIR /usr/src/app
EXPOSE 3000 
CMD ["node","backend.js"]
