# Experiment 4: Permutation Feature Importance (PFI)

## Objective
To understand and implement Permutation Feature Importance (PFI) for evaluating feature significance in machine learning models.

## Description
Permutation Feature Importance measures the importance of a feature by calculating the decrease in model performance when the feature's values are randomly shuffled. A feature is considered important if shuffling its values leads to a significant drop in accuracy.

## Datasets Used

### 1. Wine Dataset
- **Source**: sklearn.datasets
- **Features**: 13 chemical properties (alcohol, malic_acid, ash, etc.)
- **Target**: Wine class (0, 1, 2)

### 2. Cancer Dataset
- **Source**: Cancer.csv (from dataset.karunya.edu)
- **Features**: 30 tumor characteristics (radius, texture, perimeter, area, etc.)
- **Target**: Diagnosis (M = Malignant, B = Benign)

## Methodology

1. **Data Preprocessing**
   - Load dataset and separate features from target
   - Convert categorical labels to numeric values
   - Split data into training (80%) and testing (20%) sets

2. **Model Training**
   - Train a Random Forest Classifier on the training data
   - Calculate baseline accuracy on test data

3. **Permutation Feature Importance**
   - Use `sklearn.inspection.permutation_importance`
   - Perform 10 repeats of permutation for each feature
   - Calculate mean and standard deviation of importance scores

4. **Visualization**
   - Plot horizontal bar chart showing feature importance

## Requirements

```
numpy
pandas
scikit-learn
matplotlib
```

## Results
- Baseline accuracy is computed for both datasets
- Features are ranked by their permutation importance
- Higher importance values indicate features that significantly affect model predictions

## Usage

Run all cells in `ex4.ipynb` sequentially to:
1. Train models on both datasets
2. Compute permutation feature importance
3. Visualize the most important features
