# syntax=docker/dockerfile:1

FROM python:3.9.9-alpine
#
#ADD entrypoint.sh .
WORKDIR /usr/src
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

#COPY requirements.txt /filmstore/requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh

COPY . .

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["sh", "/usr/src/entrypoint.sh"]
#WORKDIR /app

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev
#
## install dependencies
#COPY requirements.txt /app/requirements.txt
#RUN pip install --upgrade pip
#RUN pip install --no-cache-dir -r requirements.txt
#
#
## copy project
#COPY . .
#
#RUN  ./manage.py runserver