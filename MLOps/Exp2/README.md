# Experiment 2: Continuous Integration (CI) with GitHub Actions

## Aim
To implement Continuous Integration for a Python project using GitHub Actions so that tests run automatically on every code change.

## Objective
- Write simple Python functions.
- Write unit tests using `pytest`.
- Configure GitHub Actions to run tests on:
  - push to `main`
  - pull request to `main`

## Project Structure
```text
Exp2/
|-- app.py
|-- test_app.py
|-- requirements.txt
|-- README.md
`-- .github/
    `-- workflows/
        `-- ci.yml
```

## Files Overview
- `app.py`: Contains simple functions (`add_numbers`, `is_even`).
- `test_app.py`: Unit tests for these functions.
- `requirements.txt`: Dependency list for CI and local testing.
- `.github/workflows/ci.yml`: GitHub Actions workflow file.

## Prerequisites
- Python 3.10+
- Git
- GitHub account
- VS Code (recommended)

## Local Setup (Windows PowerShell)

### 1. Open project folder in VS Code
Open the `Exp2` folder.

### 2. Create and activate virtual environment
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run tests locally
```powershell
pytest -v
```

Expected: all tests pass.

## GitHub Actions Workflow
Workflow file: `.github/workflows/ci.yml`

It performs the following steps:
1. Checkout code
2. Set up Python 3.11
3. Install dependencies
4. Run tests (`pytest -v`)

## How to Push and Trigger CI
Run these commands in `Exp2` folder:

```powershell
git init
git add .
git commit -m "Set up Exp2 CI with GitHub Actions"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

## How to Verify CI Run
1. Open your GitHub repository.
2. Click the **Actions** tab.
3. Open workflow: **CI Pipeline**.
4. Green status means CI passed successfully.

## Viva Questions (Practice)
1. What is Continuous Integration?
2. Why do we use automated testing in CI?
3. What triggers this GitHub Actions workflow?
4. What happens if a test fails in CI?
5. Difference between CI and CD?

## Result
Continuous Integration pipeline was successfully implemented using GitHub Actions, and tests run automatically for every push and pull request on `main`.
