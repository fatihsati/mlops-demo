from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mlflow import MlflowClient
import mlflow
from src.config import settings


mlflow.set_tracking_uri(settings.mlflow.uri)

client = MlflowClient(
    tracking_uri=settings.mlflow.uri,
    registry_uri=settings.mlflow.uri
)

print(f"loading model with uri= {settings.model.uri}")

model = mlflow.sklearn.load_model(settings.model.uri)


class PredictionInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    label: str


app = FastAPI()


@app.post("/predict", response_model=PredictionOutput)
async def prediction(input: PredictionInput):

    try:
        response = model.predict([input.text])[0]
        return PredictionOutput(label=response)
    except Exception as e:
        # TODO: log error here
        raise HTTPException(status_code=500, detail={"message": "An error occured while making the prediction"})
        
