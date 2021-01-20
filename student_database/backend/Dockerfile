FROM centos:latest
RUN yum install -y python3  
RUN yum install -y gcc  postgresql-devel python3-devel 
RUN pip3 install psycopg2 
RUN pip3 install flask 
RUN pip3 install flask_cors
RUN mkdir -p /usr/src/app
COPY ./backend.py /usr/src/app
WORKDIR /usr/src/app
EXPOSE 5000 
CMD ["python3","backend.py"]
