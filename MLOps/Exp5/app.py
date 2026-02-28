from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/predict/{value}")
def predict(value:int):
    result = model.predict(np.array([[value]]))
    return {"prediction": result[0]}