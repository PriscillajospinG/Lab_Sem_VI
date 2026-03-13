# Experiment 7: Creating a Machine Learning Model Using AutoML

## Objective
To create and train a machine learning model automatically using AutoML. The AutoML system selects the best algorithm and optimizes hyperparameters without manual model selection.

## Description
AutoML (Automated Machine Learning) simplifies the machine learning workflow by automatically searching for the best model and pipeline for a given dataset. In this experiment, the **TPOT (Tree-based Pipeline Optimization Tool)** library is used.

TPOT uses genetic programming to explore multiple machine learning pipelines and selects the one that gives the best performance. The selected pipeline can also be exported as a Python script for reuse.

## Dataset Used

### Iris Dataset
- **Source**: sklearn.datasets
- **Samples**: 150 flower samples
- **Features**:
  - sepal length
  - sepal width
  - petal length
  - petal width
- **Target**: Iris species (Setosa, Versicolor, Virginica)

## Methodology

1. **Data Preprocessing**
   - Load the Iris dataset using sklearn
   - Separate features and target variables
   - Split the dataset into training (80%) and testing (20%)

2. **AutoML Model Creation**
   - Use the `TPOTClassifier` from the TPOT library
   - Configure parameters such as generations and population size

3. **Model Training**
   - Train the AutoML model using the training dataset
   - TPOT automatically tests multiple machine learning pipelines

4. **Prediction**
   - Use the trained model to make predictions on the test dataset

5. **Model Evaluation**
   - Calculate model accuracy using `accuracy_score`

6. **Export Best Pipeline**
   - Export the best performing machine learning pipeline as a Python script

## Requirements
numpy
pandas
scikit-learn
tpot

