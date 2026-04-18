# Experiment 6: Continuous Delivery for Machine Learning Models

## Aim
To implement a simple Continuous Delivery (CD) pipeline for a Machine Learning model using Python, FastAPI, and GitHub Actions.

## Objective
This experiment shows how to automate these tasks on every push to the `main` branch:
- install dependencies
- run tests
- train ML model
- verify model artifact (`model.pkl`)
- check FastAPI app syntax

## Project Structure
```text
Exp6/
|-- app.py
|-- train_model.py
|-- test_app.py
|-- requirements.txt
|-- README.md
`-- .github/
    `-- workflows/
        `-- deploy.yml
```

## Tech Stack
- Python
- scikit-learn
- FastAPI
- pytest
- GitHub Actions

## File Description
- `train_model.py`: Trains a Random Forest model on Iris dataset and saves `model.pkl`.
- `app.py`: FastAPI app with prediction endpoint.
- `test_app.py`: Unit tests for API endpoints.
- `requirements.txt`: Project dependencies.
- `.github/workflows/deploy.yml`: CI/CD workflow for Continuous Delivery.

## Step-by-Step Local Setup (VS Code, Windows)

### 1. Open project folder
Open `Exp6` folder in VS Code.

### 2. Create virtual environment
```powershell
python -m venv .venv
```

### 3. Activate virtual environment
```powershell
.venv\Scripts\activate
```

### 4. Install dependencies
```powershell
pip install -r requirements.txt
```

### 5. Train model
```powershell
python train_model.py
```
Expected result: `model.pkl` gets created.

### 6. Run tests
```powershell
pytest -v
```
Expected result: tests should pass.

### 7. Run FastAPI server
```powershell
uvicorn app:app --reload
```
Open in browser:
- API root: http://127.0.0.1:8000/
- Swagger docs: http://127.0.0.1:8000/docs

### 8. Test prediction endpoint
Use Swagger UI (`/docs`) or PowerShell:

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/predict" -ContentType "application/json" -Body '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

## GitHub Actions Workflow Explanation
Workflow file: `.github/workflows/deploy.yml`

### Trigger
- Runs on push to `main` branch.

### Pipeline Steps
1. Checkout repository
2. Set up Python 3.11
3. Install dependencies from `requirements.txt`
4. Run `pytest -v`
5. Run `python train_model.py`
6. Verify `model.pkl` exists
7. Run FastAPI syntax check (`python -m py_compile app.py`)
8. Print success message

## How to Upload to GitHub and Trigger Workflow
Run these commands inside `Exp6` folder:

```powershell
git init
git add .
git commit -m "Add Experiment 6 Continuous Delivery project"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

After push:
1. Open your GitHub repository.
2. Go to **Actions** tab.
3. Open latest workflow run named **ML Continuous Delivery Pipeline**.
4. Verify all steps are green.

## Viva Preparation Points
- Continuous Delivery means every code push is automatically validated and prepared for deployment.
- `model.pkl` is the trained model artifact used by API for inference.
- Tests ensure API endpoints keep working after changes.
- GitHub Actions automates quality checks and model training without manual work.
- This experiment demonstrates the MLOps flow: Train -> Test -> Validate -> Deliver.

## Result
A complete beginner-friendly ML Continuous Delivery pipeline was successfully implemented using FastAPI and GitHub Actions.
