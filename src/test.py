import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from config import config
from config.model_path import MODEL_PATH

def load_classnames(filepath: str):
    """Carrega nomes das classes a partir de um arquivo TXT."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo de classes não encontrado em: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def evaluate_model():
    """Avalia o modelo treinado com o dataset de teste."""
    print("🔹 Carregando modelo treinado...")
    model = load_model(MODEL_PATH)

    print("🔹 Preparando gerador de dados de teste...")
    datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

    test_dir = config.TEST_DIR
    if not os.path.exists(test_dir):
        raise FileNotFoundError(f"Diretório de teste não encontrado: {test_dir}")

    test_gen = datagen.flow_from_directory(
        directory=test_dir,
        target_size=config.IMG_SIZE,
        batch_size=config.BATCH_SIZE,
        class_mode='categorical',
        classes=config.TEST_CLASSES,
        shuffle=False
    )

    print("🔹 Avaliando modelo...")
    loss, acc = model.evaluate(test_gen, verbose=1)
    print(f"\n Acurácia no teste: {acc * 100:.2f}%")
    print(f"Loss: {loss:.4f}")

    # # Exibir nomes das classes detectadas (opcional)
    # current_dir = os.path.dirname(__file__)
    # classnames_path = os.path.join(current_dir, "data", "raw", "classname.txt")
    # print(f"\n Total de classes: {len(load_classnames(classnames_path))}")

if __name__ == "__main__":
    evaluate_model()