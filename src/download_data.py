import os
import zipfile
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi
from config import config

# Autentica e baixa o dataset
api = KaggleApi()
api._load_config({
    'username':config.KAGGLE_USERNAME,
    'key':config.KAGGLE_KEY
})
 
api.authenticate()
os.makedirs(config.DEST, exist_ok=True)
api.dataset_download_files(config.DATASET, path=config.DEST, unzip=False)

# Extrai para pasta temporária
TEMP = os.path.join(config.DEST, "temp")
os.makedirs(TEMP, exist_ok=True)
with zipfile.ZipFile(config.ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(TEMP)

# Caminho para o dataset extraído
extracted_folder = os.path.join(TEMP, "Fruit_dataset")

# Cria pastas finais
os.makedirs(config.RAW_DIR, exist_ok=True)
os.makedirs(config.CSV_DIR, exist_ok=True)

# Move conteúdo da pasta Fruit_dataset para RAW_DIR
for item in os.listdir(extracted_folder):
    src_path = os.path.join(extracted_folder, item)
   
    if os.path.isdir(src_path):
        shutil.move(src_path, os.path.join(config.RAW_DIR, item))
    else:
        ext = os.path.splitext(item)[1].lower()
        if ext == ".csv":
            shutil.move(src_path, os.path.join(config.CSV_DIR, item))
        else:
            shutil.move(src_path, os.path.join(config.RAW_DIR, item))

# Limpeza
os.remove(config.ZIP_PATH)
shutil.rmtree(TEMP)