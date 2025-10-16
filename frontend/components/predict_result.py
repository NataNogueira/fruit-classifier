import streamlit as st
from frontend.utils.image_preprocessing import preprocess_image
from frontend.services.prediction import predict
from config import config

def show_result(model, uploaded_image):
    """
    Mostra a imagem enviada, processa e exibe a predição.
    """

    st.image(uploaded_image, caption="Imagem enviada", use_column_width=True)

    CONFIDENCE_THRESHOLD = 70  # Exemplo de limiar

    with st.spinner("Analisando imagem..."):
        processed = preprocess_image(uploaded_image)
        label, confidence = predict(model, processed, class_labels=config.TEST_CLASSES)
        
    st.success("Análise concluída!")

    if confidence < CONFIDENCE_THRESHOLD:
        st.warning("Não foi possível reconhecer com segurança essa imagem.")
        st.markdown(f"**Confiança muito baixa:** {confidence:.2f}%")
        st.info("Tente enviar uma imagem mais nítida ou de uma das frutas conhecidas.")
        return

    st.markdown(f"**Classe:** {label}")
    st.markdown(f"**Probabilidade:** {confidence:.2f}%")