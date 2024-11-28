FROM python:3.9-slim

WORKDIR /src

ENV VERSION=1.0 \
    FLASK_ENV=development \
    FLASK_APP=main.py \
    FLASK_DEBUG=1 \
    DB_USER=postgres \
    DB_PASSWORD=postgres*123 \
    DB_HOST=database-1.cjuqguqw88vk.us-east-1.rds.amazonaws.com \
    DB_PORT=5432 \
    DB_NAME=postgres \
    SECRET_TOKEN=token-super-secreto \
    NEW_RELIC_CONFIG_FILE=/src/newrelic.ini \
    PYTHONUNBUFFERED=1

# Copia el archivo de requisitos y el archivo de configuración de New Relic
COPY ./requirements.txt /src/requirements.txt
COPY ./newrelic.ini /src/newrelic.ini

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Copia el código fuente de la aplicación
COPY ./src /src

EXPOSE 3000

# Inicia la aplicación con New Relic
CMD ["newrelic-admin", "run-program", "flask", "run", "--host=0.0.0.0", "--port=3000", "--no-debugger"]
