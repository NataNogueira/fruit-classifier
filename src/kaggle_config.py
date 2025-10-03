# Script de configuração para a API do Kaggle, através daqui será possível baixar o dataset.

import os
from kaggle.api.kaggle_api_extended import KaggleApi
from config import config

def load_kaggle_api():
    api = KaggleApi()
    
    api._load_config({
        'username': config.KAGGLE_USERNAME,
        'key': config.KAGGLE_KEY
    })
    
    api.authenticate()
    return api