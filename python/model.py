from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os
import numpy as np
import pandas as pd

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Load dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train a RandomForest to find top 10 features
rf_for_selection = RandomForestClassifier(random_state=42)
rf_for_selection.fit(X, y)

# Get top 10 features
importances = rf_for_selection.feature_importances_
indices = np.argsort(importances)[::-1]
top_features = X.columns[indices[:10]]

# Select only top 10 features
X_top = X[top_features]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_top)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train best model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'model/best_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')

# Also save top feature names for frontend reference
print(top_features.tolist())  # return the names here for next step