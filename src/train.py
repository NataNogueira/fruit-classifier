import os 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from model import FruitModel

# Configurações
IMG_SIZE = (100, 100)
BATCH_SIZE = 32
EPOCHS = 10
TRAIN_DIR = "data/raw/train1"
VAL_DIR = "data/raw/val1"
MODEL_PATH = "fruit_model.h5"

# Pré-processamento dos dados
datagen = ImageDataGenerator(rescale=1./255)

train_gen = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_gen = datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Criar e compilar modelo
input_shape = (IMG_SIZE[0], IMG_SIZE[1], 3)
qtd_classnames = train_gen.num_classes

model = FruitModel.create_model(input_shape, qtd_classnames)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Treinamento
model.fit(train_gen, validation_data=val_gen, epochs=EPOCHS)

# Salvar modelo
model.save(MODEL_PATH)
print(f"Modelo salvo em {MODEL_PATH}") 