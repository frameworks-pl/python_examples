FROM python:latest
RUN pip install pytest pytest-xdist
RUN mkdir /webscrap
COPY docker/sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y vim

