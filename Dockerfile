FROM python:2.7
MAINTAINER chenleji@wise2c.com

RUN pip install python-consul && \
    pip install flask
COPY ./hello.py /
ENTRYPOINT python /hello.py
