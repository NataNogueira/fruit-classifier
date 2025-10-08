import streamlit as st
from frontend.utils.image_preprocessing import preprocess_image
from frontend.services.prediction import predict

def show_result(model, uploaded_image):
    """
    Mostra a imagem enviada, processa e exibe a predição.
    """
    st.image(uploaded_image, caption="Imagem enviada", use_column_width=True)

    with st.spinner("Analisando imagem..."):
        processed = preprocess_image(uploaded_image)
        label, confidence = predict(model, processed, class_labels=["Maçã", "Banana", "Laranja", "Uva"])
    
    st.success("Análise concluída!")
    st.markdown(f"**Classe prevista:** {label}")
    st.markdown(f"**Confiança:** {confidence:.2f}%")