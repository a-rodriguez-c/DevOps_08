FROM python:3.9-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

EXPOSE 3000

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000", "--no-debugger"]
