import os

# Caminho base para salvar o modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo do modelo salvo
MODEL_PATH = os.path.join(BASE_DIR, "..", "saved_models", "fruit_classifier.keras")

# Garante que a pasta existe
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)