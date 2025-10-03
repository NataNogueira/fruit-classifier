from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from config import config

# Carregar modelo treinado
model = load_model(config.MODEL_PATH)

# Gerador de dados
datagen = ImageDataGenerator(rescale=1./255)
test_gen = datagen.flow_from_directory(
    config.TEST_DIR,
    target_size=config.IMG_SIZE,
    batch_size=config.BATCH_SIZE,
    class_mode='categorical'
)

# Avaliação
loss, acc = model.evaluate(test_gen)
print(f"\n Acurácia no teste: {acc * 100:.2f}%")