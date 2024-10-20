FROM python:3.9

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

# Establece las variables de entorno
ENV VERSION=1.0 \
    FLASK_APP=src/main.py \
    FLASK_DEBUG=1 \
    FLASK_ENV=test \
    DB_USER=postgres \
    DB_PASSWORD=postgres \
    DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=blacklist \
    SECRET_TOKEN=token-super-secreto

EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["python", "/src/main.py"]
