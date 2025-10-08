from PIL import Image
import numpy as np

def preprocess_image(image, target_size=(224, 224)):
    """
    Redimensiona e normaliza a imagem para entrada no modelo.
    """
    img = Image.open(image).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0  # Normaliza para [0,1]
    img_array = np.expand_dims(img_array, axis=0)  # Adiciona dimensão batch
    return img_array