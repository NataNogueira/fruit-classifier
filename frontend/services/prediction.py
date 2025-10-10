import numpy as np

def predict(model, processed_image, class_labels=None):
    """
    Retorna a predição e a classe prevista.
    """
    prediction = model.predict(processed_image)
    predicted_index = np.argmax(prediction, axis=1)[0]

    if class_labels:
        predicted_label = class_labels[predicted_index]
    else:
        predicted_label = str(predicted_index)

    confidence = float(np.max(prediction)) * 100
    return predicted_label, confidence