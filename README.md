# Docker.MLFlow

- Repository for building mlflow 1.30 docker image

## build docker image

```bash
docker build -t mlflow:1.30
```

## Run docker container

```base
docker run --name mlflow -p 5000:5000 -v $(pwd):/mlflow --rm mlflow:1.30
```
