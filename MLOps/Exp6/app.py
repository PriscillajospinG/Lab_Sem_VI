from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = "model.pkl"
app = FastAPI(title="Iris Prediction API")


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Global model cache so we load the file only once.
model = None


def load_model_if_needed() -> None:
    """Load model.pkl into memory if it has not been loaded yet."""
    global model

    if model is None:
        if not Path(MODEL_PATH).exists():
            raise FileNotFoundError(
                "model.pkl not found. Run train_model.py first to create the model file."
            )
        model = joblib.load(MODEL_PATH)


@app.get("/")
def home() -> dict:
    return {"message": "Iris model API is running"}


@app.post("/predict")
def predict(features: IrisFeatures) -> dict:
    try:
        load_model_if_needed()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    prediction = model.predict(
        [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width,
        ]]
    )[0]

    class_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

    return {
        "predicted_class_index": int(prediction),
        "predicted_class_name": class_map[int(prediction)],
    }
