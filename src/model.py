from tensorflow.keras import layers, models

class FruitModel:
    @staticmethod

    def create_model(input_shape, qtd_classnames):
        model = models.Sequential([
            layers.Input(shape=input_shape),
            layers.Conv2D(32, (3,3), activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(),

            layers.Conv2D(64, (3,3), activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(),

            layers.Conv2D(128, (3,3), activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(),

            layers.Flatten(),
            layers.Dense(256, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(qtd_classnames, activation='softmax')
        ])
        return model