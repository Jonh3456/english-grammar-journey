# -*- coding: utf-8 -*-
"""
English Grammar Journey 🎮 — wrapper Streamlit (versão NUVEM)
--------------------------------------------------------------
Embute o app HTML em tela cheia e injeta as credenciais do Supabase
(URL + chave anônima) a partir do st.secrets, mantendo-as fora do GitHub.

Se as credenciais não estiverem configuradas, o app funciona normalmente
em MODO LOCAL (login/progresso salvos apenas no navegador).
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="English Grammar Journey",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      [data-testid="stHeader"] {height: 0;}
      section.main > div {padding: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "English_Grammar_Journey.html"

if not HTML_FILE.exists():
    st.error("⚠️ English_Grammar_Journey.html não encontrado na pasta do app.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

# --- Injeta credenciais do Supabase (se configuradas em Secrets) ---
supa_url = ""
supa_key = ""
try:
    supa_url = st.secrets.get("SUPABASE_URL", "")
    supa_key = st.secrets.get("SUPABASE_ANON_KEY", "")
except Exception:
    pass

html = html.replace("__SUPABASE_URL__", supa_url).replace("__SUPABASE_KEY__", supa_key)

components.html(html, height=1000, scrolling=True)
