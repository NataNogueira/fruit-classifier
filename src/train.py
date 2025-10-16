import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras import layers, models, optimizers
from config import config
from config.model_path import MODEL_PATH

# Data loading e preprocessamento
train_gen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
).flow_from_directory(
    config.TRAIN_DIR,
    target_size=config.IMG_SIZE,
    batch_size=config.BATCH_SIZE,
    class_mode='categorical',
    classes=config.TEST_CLASSES,
    shuffle=True
)

val_gen = ImageDataGenerator(
    preprocessing_function=preprocess_input
).flow_from_directory(
    config.VAL_DIR,
    target_size=config.IMG_SIZE,
    batch_size=config.BATCH_SIZE,
    class_mode='categorical',
    classes=config.TEST_CLASSES,
)


# Modelo base: MobileNetV2 pré-treinada no ImageNet

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(config.IMG_SIZE[0], config.IMG_SIZE[1], 3)
)
base_model.trainable = False  # Começa congelada


# Cabeçalho personalizado (topo do classificador)

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(train_gen.num_classes, activation='softmax')
])

model.compile(
    optimizer=optimizers.Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# Treinamento inicial

history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=config.EPOCHS
)


# Fine-tuning (descongela últimas camadas)

for layer in base_model.layers[-40:]:
    layer.trainable = True

model.compile(
    optimizer=optimizers.Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history_ft = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=10
)


# Salvando modelo no formato moderno (.keras)

save_path = MODEL_PATH.replace(".h5", ".keras")
model.save(save_path)
print(f"Modelo salvo com sucesso em: {save_path}")