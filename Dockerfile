FROM python:3.8.2-alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

#run on unbuffered mode (no chaching)
ENV PYTHONUNBUFFERD=1

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /tmp/requirements.txt

RUN pip install -U autopep8
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create a user that can only run application (-D)
# prevent application running via the root account
RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "watchmate.wsgi"]






