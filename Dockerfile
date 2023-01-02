FROM python:3.10

# app 디렉토리 생성
RUN mkdir -p /mlflow

# copy local file
COPY requirements.txt mlflow/requirements.txt

# change directory to /mlflow
WORKDIR /mlflow

# update and install requirements
RUN apt-get update && \
    pip install pip --upgrade && \
    pip install -r requirements.txt

# expose port
EXPOSE 5000

# cmd
CMD ["mlflow", "server", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "$(pwd)/artifacts"]
