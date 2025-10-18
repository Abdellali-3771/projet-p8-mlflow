import os
from mlflow.server import app
from waitress import serve

# ============================================
# 🧱 Configuration du serveur MLflow
# ============================================

# Crée le dossier pour les artefacts (logs, modèles, etc.)
os.makedirs("mlruns", exist_ok=True)

# Définit explicitement les variables d'environnement
# pour le stockage local de MLflow
os.environ["MLFLOW_BACKEND_STORE_URI"] = "sqlite:///mlflow.db"
os.environ["MLFLOW_DEFAULT_ARTIFACT_ROOT"] = "./mlruns"

# ============================================
# 🚀 Lancement du serveur MLflow
# ============================================
if __name__ == "__main__":
    print("🚀 Démarrage du serveur MLflow sur http://0.0.0.0:5001 ...")
    serve(app, host="0.0.0.0", port=5001)
