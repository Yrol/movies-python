FROM python:3.8.2-alpine

#run on unbuffered mode (no chaching)
ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN pip install -U autopep8
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create a user that can only run application (-D)
# prevent application running via the root account
RUN adduser -D user
USER user






