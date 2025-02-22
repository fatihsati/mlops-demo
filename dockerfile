FROM ghcr.io/mlflow/mlflow:latest

# Install missing dependencies
RUN pip install --upgrade pip

RUN pip install boto3
RUN pip install psycopg2-binary


CMD ["mlflow", "server", "--host", "0.0.0.0"]