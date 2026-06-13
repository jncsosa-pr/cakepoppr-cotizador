import streamlit as st
from datetime import datetime, timedelta

# Configuración de página con estética premium y limpia
st.set_page_config(
    page_title="CakePopPR - Cotizaciones",
    page_icon="assets/logo_cakepoppr.png",
    layout="centered"
)

# Estilos personalizados basados en la identidad visual de CakePopPR
st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 1.5rem;
        max-width: 900px;
    }

    .subtitle { 
        color: #D4A59A; 
        font-size: 17px; 
        text-align: center; 
        font-style: italic; 
        margin-top: -45px;
        margin-bottom: 32px; 
    }

    .stCheckbox label { 
        font-weight: bold; 
        color: #4A2E2B; 
    }

    .stButton>button { 
        background-color: #4A2E2B; 
        color: white; 
        border-radius: 20px; 
        border: none; 
        width: 100%; 
        font-weight: bold; 
    }

    .stButton>button:hover { 
        background-color: #D4A59A; 
        color: #4A2E2B; 
    }

    div[data-testid="stExpander"] { 
        background-color: #FDFBF7; 
        border-radius: 8px; 
        border-left: 4px solid #D4A59A; 
        margin-bottom: 10px; 
    }
    </style>
""", unsafe_allow_html=True)

# Logo oficial de CakePopPR más grande y centrado
col_logo1, col_logo2, col_logo3 = st.columns([1, 3, 1])

with col_logo2:
    st.image("assets/logo_cakepoppr.png", width=420)

# Subtítulo del sistema más cerca del logo
st.markdown(
    '<div class="subtitle">Sistema de Cotizaciones de Cookies Personalizadas</div>',
    unsafe_allow_html=True
)
