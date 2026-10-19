FROM python:3.12-slim

COPY requirements.txt /pybr_opendata/requirements.txt

WORKDIR /pybr_opendata/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
