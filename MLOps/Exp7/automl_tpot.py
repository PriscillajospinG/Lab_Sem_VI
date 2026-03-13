# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from tpot import TPOTClassifier

# # Step 1: Load dataset
# data = load_iris()

# # Step 2: Separate Features and Target
# X = data.data
# y = data.target

# # Step 3: Split Dataset
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Step 4: Create AutoML Model
# automl = TPOTClassifier(
#     generations=2,
#     population_size=10,
#     verbose=2,
#     random_state=42
# )

# # Step 5: Train Model
# automl.fit(X_train, y_train)

# # Step 6: Make Predictions
# predictions = automl.predict(X_test)

# # Step 7: Evaluate Accuracy
# accuracy = accuracy_score(y_test, predictions)
# print("Model Accuracy:", accuracy)

# # Step 8: Export Best Pipeline
# automl.export("best_pipeline.py")


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tpot import TPOTClassifier

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

automl = TPOTClassifier(
    generations=1,
    population_size=5,
    verbose=3,
    random_state=42,
    n_jobs=1
)

automl.fit(X_train, y_train)

predictions = automl.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

automl.export("best_pipeline.py")