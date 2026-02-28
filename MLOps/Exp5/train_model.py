from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# sample data
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10])

model = LinearRegression()
model.fit(X,y)

# save model
joblib.dump(model,"model.pkl")

print("Model trained and saved")