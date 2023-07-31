FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /mynote
ADD . /mynote/
WORKDIR /mynote
RUN pip install -r requirements.txt