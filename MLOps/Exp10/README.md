# Experiment 10: Iris Classification CLI

## Objective
Build a command-line tool to train and use a machine learning model for Iris flower classification.

## Overview
This experiment provides a CLI application using Click and scikit-learn with two commands:
- `train`: Trains a Random Forest classifier on the Iris dataset and saves the model
- `predict`: Loads a saved model and predicts the flower class from 4 input features

## File Structure
```
Exp10/
├── iris_cli.py
└── README.md
```

## Requirements
- Python 3.8+
- click
- scikit-learn
- joblib

## Installation
Install dependencies:

```bash
pip install click scikit-learn joblib
```

## Usage
Run commands from the Exp10 folder.

### 1) Train the model
Basic training:

```bash
python iris_cli.py train
```

Train with custom parameters:

```bash
python iris_cli.py train --test_size 0.25 --n_estimators 150 --max_depth 6 --model_output iris.pkl
```

#### Train Options
- `--test_size` (float, default: `0.2`): Fraction of dataset used for testing
- `--n_estimators` (int, default: `100`): Number of trees in Random Forest
- `--max_depth` (int, default: `None`): Maximum depth of each tree
- `--model_output` (str, default: `model.pkl`): Output path for the trained model file

### 2) Predict using saved model
Example:

```bash
python iris_cli.py predict --model_input iris.pkl --features 5.1 3.5 1.4 0.2
```

#### Predict Options
- `--model_input` (str, default: `model.pkl`): Path to saved model
- `--features` (required, 4 float values):
  - sepal length
  - sepal width
  - petal length
  - petal width

## Output
### Train command prints:
- Training success status
- Model accuracy on test split
- Saved model filename

### Predict command prints:
- Predicted class index
- Predicted flower label (`Setosa`, `Versicolor`, or `Virginica`)

## Notes
- Ensure the model file exists before running `predict`.
- If model loading fails, the CLI prints an error and exits safely.
- Accuracy may vary between runs because train/test split randomness is not fixed.
