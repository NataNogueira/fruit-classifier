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

# Move arquivos para csv/ ou raw/
for root, _, files in os.walk(TEMP):
    for f in files:
        src = os.path.join(root, f)
        ext = os.path.splitext(f)[1].lower()
        dest_dir = config.CSV_DIR if ext == ".csv" else config.RAW_DIR
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(src, os.path.join(dest_dir, f))

# Limpeza
os.remove(config.ZIP_PATH)
shutil.rmtree(TEMP)