from fastapi.testclient import TestClient

from app import app
from train_model import train_and_save_model


# Ensure model.pkl exists before tests call /predict.
train_and_save_model("model.pkl")

client = TestClient(app)


def test_home_endpoint() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Iris model API is running"


def test_predict_endpoint() -> None:
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert "predicted_class_index" in body
    assert "predicted_class_name" in body
    assert body["predicted_class_name"] in {"setosa", "versicolor", "virginica"}
