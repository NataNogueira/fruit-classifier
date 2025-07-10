import os
import zipfile
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurações
DATASET = "icebearogo/fruit-classification-dataset"
DEST = "data"
ZIP_PATH = os.path.join(DEST, "dataset.zip")
CSV_DIR = os.path.join(DEST, "csv")
RAW_DIR = os.path.join(DEST, "raw")

# Autentica e baixa o dataset
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(), ".kaggle")
api = KaggleApi()
api.authenticate()
os.makedirs(DEST, exist_ok=True)
api.dataset_download_files(DATASET, path=DEST, unzip=False)

# Extrai para pasta temporária
TEMP = os.path.join(DEST, "temp")
os.makedirs(TEMP, exist_ok=True)
with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(TEMP)

# Move arquivos para csv/ ou raw/
for root, _, files in os.walk(TEMP):
    for f in files:
        src = os.path.join(root, f)
        ext = os.path.splitext(f)[1].lower()
        dest_dir = CSV_DIR if ext == ".csv" else RAW_DIR
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(src, os.path.join(dest_dir, f))

# Limpeza
os.remove(ZIP_PATH)
shutil.rmtree(TEMP)