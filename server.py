import os
from mlflow.server import main

# Crée les dossiers nécessaires
os.makedirs("mlruns", exist_ok=True)

# Définit les arguments du serveur MLflow
args = [
    "mlflow",
    "server",
    "--host", "0.0.0.0",
    "--port", "5001",
    "--backend-store-uri", "sqlite:///mlflow.db",
    "--default-artifact-root", "./mlruns"
]

# Lance MLflow directement via Python
if __name__ == "__main__":
    main(args)
