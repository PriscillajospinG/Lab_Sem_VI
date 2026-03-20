import click
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


# Create CLI group
@click.group()
def cli():
    pass


# ------------------ TRAIN COMMAND ------------------
@cli.command()
@click.option('--test_size', default=0.2, type=float, help='Test data size (e.g., 0.2)')
@click.option('--n_estimators', default=100, type=int, help='Number of trees')
@click.option('--max_depth', default=None, type=int, help='Max depth of trees')
@click.option('--model_output', default='model.pkl', type=str, help='Output model file')
def train(test_size, n_estimators, max_depth, model_output):
    """Train a Random Forest model on Iris dataset"""

    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size
    )

    # Create model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth
    )

    # Train model
    model.fit(X_train, y_train)

    # Evaluate
    accuracy = model.score(X_test, y_test)

    # Save model
    joblib.dump(model, model_output)

    print("\n✅ Model trained successfully!")
    print(f"📊 Accuracy: {accuracy:.2f}")
    print(f"💾 Model saved as: {model_output}")


# ------------------ PREDICT COMMAND ------------------
@cli.command()
@click.option('--model_input', default='model.pkl', type=str, help='Model file')
@click.option(
    '--features',
    nargs=4,
    type=float,
    required=True,
    help='Input: sepal_len sepal_wid petal_len petal_wid'
)
def predict(model_input, features):
    """Predict Iris class using trained model"""

    try:
        # Load model
        model = joblib.load(model_input)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    # Predict
    prediction = model.predict([features])[0]

    # Convert to class name
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    predicted_label = class_names[prediction]

    print("\n🔮 Prediction Result:")
    print(f"👉 Predicted class index: {prediction}")
    print(f"🌸 Predicted flower: {predicted_label}")


# Run CLI
if __name__ == '__main__':
    cli()