# Experiment 5: ML Model Deployment with FastAPI

## Objective
Deploy a machine learning model as a REST API using FastAPI.

## Overview
This experiment demonstrates how to:
1. Train a simple Linear Regression model
2. Save the trained model using joblib
3. Serve predictions via a FastAPI web service

## Project Structure
```
Exp5/
├── train_model.py    # Script to train and save the model
├── app.py            # FastAPI application for serving predictions
├── requirements.txt  # Python dependencies
└── model.pkl         # Saved model (generated after training)
```

## Requirements
- Python 3.x
- FastAPI
- Uvicorn
- Scikit-learn
- Joblib

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Train the Model
```bash
python train_model.py
```
This creates a `model.pkl` file containing the trained Linear Regression model.

### Step 2: Run the API
```bash
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check - returns API status |
| `/predict/{value}` | GET | Returns prediction for the given input value |

### Example Requests

**Health Check:**
```bash
curl http://127.0.0.1:8000/
```
Response: `{"message": "API Running"}`

**Prediction:**
```bash
curl http://127.0.0.1:8000/predict/6
```
Response: `{"prediction": 12.0}`

## How It Works
1. **Training**: The model learns a simple linear relationship (y = 2x) from sample data
2. **Serialization**: The trained model is saved to disk using joblib
3. **Serving**: FastAPI loads the model and exposes a REST endpoint for predictions

## Interactive Documentation
Once the server is running, access the auto-generated API docs at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
