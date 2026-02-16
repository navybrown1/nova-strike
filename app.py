import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="NOVA STRIKE - Neon Space Assault",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome for immersive experience
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #01030a;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

game_html = Path(__file__).parent / "game.html"
html_content = game_html.read_text(encoding="utf-8")

components.html(html_content, height=800, scrolling=False)
