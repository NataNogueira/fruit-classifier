import os
import zipfile
import shutil
import requests
from config import config


os.makedirs(config.DEST, exist_ok=True)
print("Baixando dataset...")
response = requests.get(config.DATASET_URL, stream=True)
response.raise_for_status()

with open(config.ZIP_PATH, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
print("Download concluído!")

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