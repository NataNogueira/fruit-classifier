import streamlit as st

def initialize_session_state():
    if "last_prediction" not in st.session_state:
        st.session_state.last_prediction = None