FROM python:3.9-alpine

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/eterlast
COPY requirements.txt  /opt/app/
COPY ../. /opt/app/eterlast
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1