from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle
import uvicorn

try:
    with open("simple_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    raise Exception("Model file not found.")

class PredictRequest(BaseModel):
    x: float

app = FastAPI(title="SynthexAI Take Home Assignment")

@app.get("/predict")
def predict_get(x: float):
    try:
        x_array = np.array([[x]])
        pred= model.predict(x_array)
        return {"prediction": float(pred[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict")
def predict_post(request: PredictRequest):
    try:
        x_array = np.array([[request.x]])
        pred = model.predict(x_array)
        return {"prediction": float(pred[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
