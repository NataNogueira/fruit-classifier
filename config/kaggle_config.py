import os
from kaggle.api.kaggle_api_extended import KaggleApi

def load_kaggle_api():
    # Define o caminho absoluto para a pasta contendo kaggle.json
    kaggle_config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kaggle'))
    
    # Define a variável de ambiente que a API do Kaggle espera
    os.environ['KAGGLE_CONFIG_DIR'] = kaggle_config_dir

    # Inicializa e autentica a API
    api = KaggleApi()
    api.authenticate()
    
    return api