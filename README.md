# Local MLOps with Mlflow

## Tech Stack
- Mlflow
- Postgres (backend/registery)
- Minio (artifacts)


## How to Start the system
1. Env variables
    1. Copy .env-example to `.env` file
    2. Fill values
2. Start docker services
    ```bash
    docker compose up --build
    ```
3. Set mlflow tracking uri in your code
    ```python
    MLFLOW_URI = "http://localhost:8080"
    mlflow.set_tracking_uri(MLFLOW_URI)
    ```
4. You can start using Mlflow in your code...


