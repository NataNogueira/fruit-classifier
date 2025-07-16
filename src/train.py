import os 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from model import FruitModel
from config import config

# Pré-processamento dos dados
datagen = ImageDataGenerator(rescale=1./255)

train_gen = datagen.flow_from_directory(
    config.TRAIN_DIR,
    target_size=config.IMG_SIZE,
    batch_size=config.BATCH_SIZE,
    class_mode='categorical'
)

val_gen = datagen.flow_from_directory(
    config.VAL_DIR,
    target_size=config.IMG_SIZE,
    batch_size=config.BATCH_SIZE,
    class_mode='categorical'
)

# Criar e compilar modelo
input_shape = (config.IMG_SIZE[0], config.IMG_SIZE[1], 3)
qtd_classnames = train_gen.num_classes

model = FruitModel.create_model(input_shape, qtd_classnames)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Treinamento
model.fit(train_gen, validation_data=val_gen, epochs=config.EPOCHS)

# Salvar modelo
model.save(config.MODEL_PATH)
print(f"Modelo salvo em {config.MODEL_PATH}") 