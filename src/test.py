# test.py

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Caminhos
MODEL_PATH = "fruit_model.h5"
TEST_DIR = "data/raw/test1"
IMG_SIZE = (100, 100)
BATCH_SIZE = 32

# Carregar modelo treinado
model = load_model(MODEL_PATH)

# Gerador de dados
datagen = ImageDataGenerator(rescale=1./255)
test_gen = datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Avaliação
loss, acc = model.evaluate(test_gen)
print(f"\n Acurácia no teste: {acc * 100:.2f}%")