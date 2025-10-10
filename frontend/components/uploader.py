import streamlit as st

def image_uploader():
    """
    Cria o componente de upload e retorna o arquivo enviado.
    """
    st.subheader("Envie uma imagem para análise")
    uploaded_file = st.file_uploader(
        "Selecione uma imagem (jpg, png, jpeg)",
        type=["jpg", "jpeg", "png"]
    )
    return uploaded_file