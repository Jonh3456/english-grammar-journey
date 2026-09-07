# -*- coding: utf-8 -*-
"""English Grammar Journey 🎮 — wrapper Streamlit (versão NUVEM + RANKING)."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="English Grammar Journey", page_icon="🦉",
                   layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
  #MainMenu, header, footer {visibility:hidden;}
  .block-container{padding:0 !important;max-width:100% !important;}
  [data-testid="stAppViewContainer"] > .main{padding:0 !important;}
  [data-testid="stHeader"]{height:0;}
  section.main > div{padding:0 !important;}
</style>""", unsafe_allow_html=True)

HTML = Path(__file__).parent / "English_Grammar_Journey.html"
if not HTML.exists():
    st.error("⚠️ English_Grammar_Journey.html não encontrado na pasta do app.")
    st.stop()

html = HTML.read_text(encoding="utf-8")

supa_url = ""; supa_key = ""
try:
    supa_url = st.secrets.get("SUPABASE_URL", "")
    supa_key = st.secrets.get("SUPABASE_ANON_KEY", "")
except Exception:
    pass
html = html.replace("__SUPABASE_URL__", supa_url).replace("__SUPABASE_KEY__", supa_key)

components.html(html, height=1000, scrolling=True)
