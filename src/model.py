from tensorflow.keras import layers, models

class FruitModel:
    @staticmethod

    def create_model(input_shape, qtd_classnames):
        model = models.Sequential([
            layers.Input(shape=input_shape),
            layers.Conv2D(32, (3,3), activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, (3,3), activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(128, (3,3), activation='relu'),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(qtd_classnames)
        ])
        return model