FROM python:3.9-slim

WORKDIR /src

ENV VERSION=1.0 \
    FLASK_APP=main.py \
    FLASK_DEBUG=1 \
    FLASK_ENV=test \
    DB_USER=postgres \
    DB_PASSWORD=devops08-postgresql \
    DB_HOST=postgres.cfsmcayu0ajr.us-east-1.rds.amazonaws.com \
    DB_PORT=5432 \
    DB_NAME=postgres \
    SECRET_TOKEN=token-super-secreto

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

EXPOSE 3000

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000", "--no-debugger"]
