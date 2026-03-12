from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("electricity_model.pkl")

class InputData(BaseModel):
    site_area: float
    water_consumption: float
    resident_count: float
    utilisation_rate: float
    structure_type: str


@app.post("/predict")
def predict(data: InputData):

    structure = data.structure_type.lower()

    commercial = 1 if structure == "commercial" else 0
    industrial = 1 if structure == "industrial" else 0
    mixed = 1 if structure == "mixed-use" else 0
    residential = 1 if structure == "residential" else 0

    features = np.array([[
        data.site_area,
        data.water_consumption,
        data.resident_count,
        data.utilisation_rate,
        commercial,
        industrial,
        mixed,
        residential
    ]])

    prediction = model.predict(features)

    return {"predicted_electricity_cost": float(prediction[0])}