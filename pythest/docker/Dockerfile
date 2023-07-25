FROM python:latest
#COPY docker/sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install pytest
#RUN pip install pytest-xdist
RUN mkdir /webscrap
RUN apt-get install -y vim

