# Experiment 2: Continuous Integration (CI) with GitHub Actions

## Objective
Learn how to set up Continuous Integration using GitHub Actions to automatically run tests on code push.

## Prerequisites
- Python 3.x installed
- Git installed
- GitHub account
- Basic understanding of pytest

## Project Structure
```
Exp2/
├── app.py          # Main application file
├── test_app.py     # Test file for CI
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## How to Set Up CI

### Step 1: Create a GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

### Step 2: Add Project Files
Copy the following files to your repository:
- `app.py`
- `test_app.py`
- `requirements.txt`

### Step 3: Create GitHub Actions Workflow
1. Create a `.github/workflows` directory in your repository
2. Create a file named `ci.yml` inside it:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest -v test_app.py
```

### Step 4: Push to GitHub
```bash
git add .
git commit -m "Add CI pipeline"
git push origin main
```

### Step 5: Verify CI Pipeline
1. Go to your GitHub repository
2. Click on the "Actions" tab
3. You should see your workflow running
4. Green checkmark ✅ = All tests passed
5. Red X ❌ = Tests failed

## Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v test_app.py
```

## Files Description

| File | Description |
|------|-------------|
| `app.py` | Main application code |
| `test_app.py` | Test cases using pytest |
| `requirements.txt` | Lists pytest as dependency |

## Key Concepts Learned
- Setting up GitHub Actions for CI
- Creating workflow YAML files
- Automated testing on code push
- Viewing CI/CD pipeline results on GitHub
