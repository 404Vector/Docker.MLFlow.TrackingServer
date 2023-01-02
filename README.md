# Docker.MLFlow

- Repository for building mlflow 2.1.1 docker image

## build docker image

- base image : [python:3.10.9](<https://hub.docker.com/layers/library/python/3.10.9/images/sha256-08dfb526b02f1b849ca4ce479b51f100448053a67b64905a63dcdad2fe6802c5?context=explore>)

```bash
docker build -t mlflow:2.1.1 .
```

## Display docker image list

```bash
docker images | grep mlflow
```

## Run docker container

```bash
docker run --name mlflow -p 15000:5000 -v $(pwd):/mlflow --rm mlflow:2.1.1
```

## Run Example Project

- init directory

```bash
pipenv install --dev
```

- run example project

```base
pipenv run mlflow run ./example_project --experiment-name "my-first-experiment" --no-conda
```

## Ref Example Link
 - [mlflow/examples](<https://github.com/mlflow/mlflow/tree/branch-1.30/examples>)