from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Calculate Permutation Feature Importance
result = permutation_importance(model, X_test, y_test, random_state=42)

# Feature names
features = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

# Plot graph
plt.bar(features, result.importances_mean)
plt.title("Permutation Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")
#plt.xticks(rotation=30)
plt.show()