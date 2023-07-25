FROM python:latest
RUN pip install pytest
#RUN pip install pytest-xdist
COPY test_simple.py /tmp/test_simple.py
WORKDIR /tmp
ENTRYPOINT pytest