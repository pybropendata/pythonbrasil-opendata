FROM python:3.9-slim-buster

RUN apt-get update -y \
    && apt-get install gcc -y \
    && apt-get clean

COPY requirements.txt /pybr_opendata/requirements.txt

WORKDIR /pybr_opendata/

RUN pip install --upgrade pip
RUN pip install -r /pybr_opendata/requirements.txt
