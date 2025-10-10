import streamlit as st
from tensorflow.keras.models import load_model
from config.model_path import MODEL_PATH

@st.cache_resource
def load_model():
    try:
        model = load_model(MODEL_PATH)
        st.success("✅ Modelo carregado com sucesso!")
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        return None