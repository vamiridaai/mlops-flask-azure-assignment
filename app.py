from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request

MODEL_PATH = Path(__file__).with_name("model.pkl")
CLASS_NAMES = ["setosa", "versicolor", "virginica"]

app = Flask(__name__)


def load_model():
    if not MODEL_PATH.exists():
        from train_model import train_model
        train_model()
    return joblib.load(MODEL_PATH)


model = load_model()


@app.get("/")
def home():
    return jsonify({"application": "MLOps Flask ML Application", "status": "running", "platform": "Azure App Service"})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)
    if not data or "features" not in data:
        return jsonify({"error": "JSON body with 'features' is required."}), 400
    features = data["features"]
    if not isinstance(features, list) or len(features) != 4:
        return jsonify({"error": "Exactly four numeric features are required."}), 400
    try:
        values = np.asarray(features, dtype=float).reshape(1, -1)
    except (TypeError, ValueError):
        return jsonify({"error": "All features must be numeric."}), 400
    prediction = int(model.predict(values)[0])
    return jsonify({"prediction": prediction, "class_name": CLASS_NAMES[prediction]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
