FROM python:3.8-alpine

LABEL 'Image Maintainer'='NULL Team'

# TODO: Install python3 and python3-pip, hint "apt-get install python3 python3-pip"
RUN apk update 

#RUN apt install -y python3 python3-pip
RUN apk add python3 py3-pip

# TODO: Copy application files into container
COPY . /pyblog

# TODO: Install required python libraries
RUN pip install -r /pyblog/requirements.txt

# TODO: Have the container expose port 8080
#EXPOSE 8080

#TODO Set default values for env variables
ENV APIUSER='someapiuser' APIPWD='someapipwd' WORDPRESSURL='someurl'

#USER gthomas

ENTRYPOINT [ "python3", "/pyblog/pyblog.py" ]

CMD ["help"]