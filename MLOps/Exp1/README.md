# Experiment 1: Introduction to Unit Testing with Pytest

## Objective
Learn the basics of unit testing in Python using the `pytest` framework.

## Prerequisites
- Python 3.x installed
- pip package manager

## Installation

```bash
pip install pytest
```

## How to Run

### Step 1: Open the Jupyter Notebook
Open `Exp1.ipynb` in VS Code or Jupyter Notebook.

### Step 2: Run the cells sequentially

The notebook covers the following test cases:

#### 1. Addition Function (`add.py`)
- Tests positive numbers
- Tests negative numbers
- Tests mixed numbers
- Tests with zero

```bash
pytest -v tadd.py
```

#### 2. Average Function (`avg.py`)
- Tests average calculation

```bash
pytest -v test_avg.py
```

#### 3. Factorial Function (`factorial.py`)
- Tests positive numbers
- Tests zero
- Tests one
- Tests negative numbers (raises ValueError)

```bash
pytest -v tfactorial.py
```

#### 4. Palindrome Function (`palindrome.py`)
- Tests odd length palindromes
- Tests even length palindromes
- Tests digit palindromes
- Tests special characters
- Tests non-palindromes

```bash
pytest -v tpalindrome.py
```

## Files Generated
After running the notebook, the following files will be created:
- `add.py` - Addition function
- `tadd.py` - Test cases for addition
- `avg.py` - Average function
- `test_avg.py` - Test cases for average
- `factorial.py` - Factorial function
- `tfactorial.py` - Test cases for factorial
- `palindrome.py` - Palindrome checker function
- `tpalindrome.py` - Test cases for palindrome

## Expected Output
All test cases should pass with output similar to:
```
========================= test session starts =========================
collected X items

test_file.py::test_name PASSED
...
========================= X passed in 0.XXs =========================
```

## Key Concepts Learned
- Writing unit tests with pytest
- Using assertions for validation
- Testing edge cases
- Handling exceptions in tests with `pytest.raises()`
