# -*- coding: utf-8 -*-
"""
English Grammar Journey 🎮 — wrapper Streamlit
------------------------------------------------
Embute o app HTML autônomo (English_Grammar_Journey.html) em tela cheia.
Todo o jogo (mapa, teoria, exercícios, timer, música, fogos, XP, estrelas,
3 níveis de dificuldade e resumo do capítulo) roda dentro do componente.
O progresso é salvo no navegador (localStorage), como no HTML original.

Estrutura esperada no repositório GitHub:
    english-grammar-journey/
    ├── streamlit_app.py                 <- este arquivo
    ├── English_Grammar_Journey.html     <- o app aprovado (v3)
    ├── requirements.txt
    └── .streamlit/config.toml           (opcional)
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ------------------------------------------------------------------
# Configuração da página (tela cheia, sem margens)
# ------------------------------------------------------------------
st.set_page_config(
    page_title="English Grammar Journey",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove paddings/margens padrão do Streamlit para o app ocupar tudo
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

# ------------------------------------------------------------------
# Carrega o HTML do app (mesmo diretório do streamlit_app.py)
# ------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "English_Grammar_Journey.html"

if not HTML_FILE.exists():
    st.error(
        "⚠️ Arquivo **English_Grammar_Journey.html** não encontrado.\n\n"
        "Coloque o HTML aprovado na mesma pasta deste `streamlit_app.py` "
        "dentro do repositório GitHub."
    )
    st.stop()

html_content = HTML_FILE.read_text(encoding="utf-8")

# ------------------------------------------------------------------
# Renderiza o app em tela cheia
# height alto para não cortar; scrolling=True permite rolar dentro do jogo
# ------------------------------------------------------------------
components.html(html_content, height=1000, scrolling=True)
