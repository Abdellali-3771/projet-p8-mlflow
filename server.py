import os
import mlflow.server

# Crée le dossier local pour stocker les runs
os.makedirs("mlruns", exist_ok=True)

# Démarre le serveur MLflow en Python pur (pas de commande shell)
if __name__ == "__main__":
    from mlflow.server import app
    from waitress import serve  # waitress = serveur web stable pour Python
    
    print("🚀 Démarrage du serveur MLflow sur http://0.0.0.0:5001 ...")
    serve(app, host="0.0.0.0", port=5001)
