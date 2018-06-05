FROM python:3

ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/

RUN pip3 install --upgrade pipenv
RUN apt-get -y update && apt-get -y install wkhtmltopdf
RUN pipenv install --system && pipenv install --dev --system

EXPOSE 8000
