from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2


class FruitModel:
    @staticmethod
    def create_model(input_shape, qtd_classnames):

        # Carregar o modelo base pré-treinado
        base_model = MobileNetV2(
            input_shape=input_shape,
            include_top=False,     
            weights='imagenet'     # ImageNet
        )

        # (as convoluções não serão treinadas inicialmente)
        for layer in base_model.layers:
            layer.trainable = False

        # Construir o topo personalizado
        x = base_model.output
        x = layers.GlobalAveragePooling2D()(x)  
        x = layers.Dense(256, activation='relu')(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(qtd_classnames, activation='softmax')(x)

        # Combinar modelo base + topo
        model = models.Model(inputs=base_model.input, outputs=outputs)

        print("Modelo MobileNetV2 criado com sucesso (camadas base congeladas).")
        return model