from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_and_save_model(model_path: str = "model.pkl") -> float:
    """Train a simple classifier on Iris and save it as a .pkl file.

    Returns:
        float: Accuracy score on the test split.
    """
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    joblib.dump(model, model_path)

    return accuracy


if __name__ == "__main__":
    output_file = "model.pkl"
    score = train_and_save_model(output_file)

    # Simple prints to help beginners verify the script worked.
    print(f"Model trained successfully with accuracy: {score:.2f}")
    print(f"Saved model file at: {Path(output_file).resolve()}")
