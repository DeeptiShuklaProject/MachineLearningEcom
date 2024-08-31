from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from models.train_model import train_models

app = FastAPI()

class PredictionRequest(BaseModel):
    features: dict

@app.post("/predict")
def predict(request: PredictionRequest):
    # Assume you have a pre-trained model
    df = pd.DataFrame([request.features])
    # Make prediction (example)
    # result = model.predict(df)
    result = "prediction"
    return {"prediction": result}
