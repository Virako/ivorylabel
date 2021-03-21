from python:3.9-alpine

RUN apk add --no-cache\
            gcc\
            jpeg-dev\
            musl-dev\
            python3-dev\
            zlib-dev

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn
COPY . /app

COPY docker/entrypoint /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

WORKDIR /app
