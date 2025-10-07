import streamlit as st
from services.model_loader import load_model
from components.uploader import image_uploader
from components.predict_result import show_result
from utils.state_manager import initialize_session_state

st.set_page_config(page_title="ML Image Analyzer", layout="centered")

st.title("Machine Learning Image Analyzer")

# Inicializar sessão
initialize_session_state()

# Carregar modelo treinado (ex: .h5, .pkl etc)
model = load_model()

# Upload da imagem
uploaded_image = image_uploader()

# Se o usuário enviou uma imagem, processar e mostrar resultado
if uploaded_image is not None and model is not None:
    show_result(model, uploaded_image)