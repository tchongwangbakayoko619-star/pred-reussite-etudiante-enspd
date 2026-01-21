from django.shortcuts import render
# Create your views here.
import json
import numpy as np
import pandas as pd
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .schemas import DonneesEntree

# Charger ton modèle sérialisé
modele = joblib.load("mlmodel/logistic_model.pkl")

@csrf_exempt
def predict_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Utilisez POST avec un JSON"}, status=405)

    try:
        payload = json.loads(request.body.decode("utf-8"))
        # Validation avec Pydantic
        donnees = DonneesEntree(**payload)
        donnees_df = pd.DataFrame([donnees.dict()])

        # Prédiction
        predictions = modele.predict(donnees_df)
        probabilities = modele.predict_proba(donnees_df)[:, 1]

        resultats = donnees.dict()
        resultats["prediction"] = int(predictions[0])
        resultats["probabilite_reussite"] = float(probabilities[0])

        return JsonResponse({"resultats": resultats})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
