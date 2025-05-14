from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS  # Allow cross-origin for frontend

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the saved model and scaler
model = joblib.load('model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data["features"]

        # Load model and scaler
        model = joblib.load("model/best_model.pkl")
        scaler = joblib.load("model/scaler.pkl")

        # List of top 10 features (must match model training order)
        feature_names = [
            "worst area",
            "worst concave points",
            "mean concave points",
            "worst radius",
            "worst perimeter",
            "mean perimeter",
            "mean concavity",
            "mean area",
            "worst concavity",
            "mean radius",
        ]

        # Create DataFrame for consistent feature naming
        input_df = pd.DataFrame([features], columns=feature_names)

        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]

        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
