from flask import Flask, request, jsonify, render_template
import os
import joblib
import numpy as np
from pydantic import BaseModel, ValidationError

# Initialisation de l'application Flask
app = Flask(__name__)

# -------------------------------
# Classe DummyModel (fallback)
# -------------------------------
class DummyModel:
    def predict(self, X):
        return [0 for _ in range(len(X))]

    def predict_proba(self, X):
        return [[0.5, 0.5] for _ in range(len(X))]

# -------------------------------
# Chargement du modèle
# -------------------------------
def load_model():
    base = os.path.dirname(__file__)
    candidates = ["logistic_model.pkl", "model.pkl"]
    for name in candidates:
        path = os.path.join(base, name)
        if os.path.exists(path):
            try:
                model = joblib.load(path)
                print(f"✅ Modèle chargé depuis {path}")
                return model
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement {path}: {e}")
    print("⚠️ Aucun modèle trouvé, utilisation de DummyModel")
    return DummyModel()

MODEL = load_model()

# -------------------------------
# Validation des données avec Pydantic
# -------------------------------
class Features(BaseModel):
    presence_pct: float
    study_min: float
    implication: float
    interaction_ord: float
    acces_bibliotheque_ord: float

# -------------------------------
# Prétraitement des données
# -------------------------------
def preprocess_input(features):
    if isinstance(features, dict):
        arr = list(features.values())
        return np.array(arr).reshape(1, -1)
    if isinstance(features, str):
        arr = [float(x.strip()) for x in features.split(",") if x.strip() != ""]
        return np.array(arr).reshape(1, -1)
    arr = list(features)
    return np.array(arr).reshape(1, -1)

# -------------------------------
# Routes Flask
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Récupération des données
        if request.is_json:
            payload = request.get_json()
        else:
            features = request.form.get("features")
            payload = {"features": features} if features else {}

        if not payload or "features" not in payload:
            return jsonify({"error": "Aucune donnée 'features' fournie"}), 400

        # Validation avec Pydantic si dict
        if isinstance(payload["features"], dict):
            try:
                validated = Features(**payload["features"])
                X = preprocess_input(validated.dict())
            except ValidationError as ve:
                return jsonify({"error": ve.errors()}), 400
        else:
            X = preprocess_input(payload["features"])

        # Prédiction
        pred = MODEL.predict(X)
        result = {"prediction": int(pred[0])}

        if hasattr(MODEL, "predict_proba"):
            proba = MODEL.predict_proba(X)
            result["probability"] = [float(p) for p in proba[0]]

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------
# Lancement du serveur
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
