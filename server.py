import os

# Crée le dossier de stockage des expériences
os.makedirs("mlruns", exist_ok=True)

# Lancer le serveur MLflow sur le port 5001
os.system(
    "mlflow server "
    "--host 0.0.0.0 "
    "--port 5001 "
    "--backend-store-uri sqlite:///mlflow.db "
    "--default-artifact-root ./mlruns"
)
