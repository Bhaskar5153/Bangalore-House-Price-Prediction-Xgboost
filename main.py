# create API using FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import os

# create the house price request

class HousePriceRequest(BaseModel):
    area_type: str
    availability: str
    location: str
    total_sqft: float
    bath: int
    balcony: int
    bhk: int

model_path = os.path.join("artifacts", "xgb_model.pkl")
with open(file=model_path, mode='rb') as f:
    model = pickle.load(f)

# create fastapi for the model

app = FastAPI(title="House Price Prediction")

@app.get("/")
def root():
    return "Welcome to the House Price Prediction App"


@app.post("/predict")
def predict(request: HousePriceRequest):
    data = pd.DataFrame([request.model_dump()])
    prediction = model.predict(data)[0]
    return {"Predicted charges" : round(float(prediction), 2)}




