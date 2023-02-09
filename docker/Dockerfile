#! /bin/bash

FROM python:3.10.5-slim-buster

WORKDIR /workspace/code

COPY . /workspace/code

RUN echo "$PWD" && ls /workspace/code/users_api

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# CMD ["uvicorn", "users_crud.main:app", "--host", "0.0.0.0", "--port", "80"]