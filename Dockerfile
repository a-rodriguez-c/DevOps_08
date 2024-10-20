FROM python:3.9-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

EXPOSE 3000

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000", "--no-debugger"]

# Comandos para executar el proyecto
# docker pull postgres
# docker run --name my-postgres-container --network my_network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=2024 -e POSTGRES_DB=blacklist_db -p 5432:5432 -d postgres
# docker build -t my-flask-app . --no-cache
# docker run --name my-flask-container --network my_network -p 3000:3000 my-flask-app