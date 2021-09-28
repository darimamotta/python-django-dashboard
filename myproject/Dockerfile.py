FROM python:3
#python: 3.7 - alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/apptask
COPY requirements.txt ./
RUN pip install -r requirements.txt