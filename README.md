# Docker.MLFlow

- Repository for building mlflow 1.30 docker image

## build docker image

- base image : [python:3.11.0](<https://hub.docker.com/layers/library/python/3.11.0/images/sha256-c43926b6865b221fb6460da1e7e19de3143072fc6be8b64cb1e679f90c7fcaa3?context=explore>)

```bash
docker build -t mlflow:1.30 .
```

## Run docker container

```base
docker run --name mlflow -p 5000:5000 -v $(pwd):/mlflow --rm mlflow:1.30
```