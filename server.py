import os
import sys
from mlflow.server import app
from waitress import serve

# Crée les dossiers nécessaires
os.makedirs("mlruns", exist_ok=True)

print("🚀 Démarrage du serveur MLflow sur http://0.0.0.0:5001 ...")

# Démarre le serveur avec waitress (stable, compatible Codespaces)
serve(app, host="0.0.0.0", port=5001)
