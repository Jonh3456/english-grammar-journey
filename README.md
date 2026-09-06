# 🦉 English Grammar Journey — Streamlit

App de gramática inglesa gamificado (estilo Duolingo) rodando no **Streamlit**,
com os arquivos hospedados no **GitHub** — mesmo padrão do *English Journey*.

- **82 capítulos** em 17 seções • **3 níveis** de dificuldade (Fácil / Médio / Difícil)
- Teoria + exercícios interativos (digitar, marcar, escolher) + **resumo do capítulo**
- Timer, música chiptune, fogos, contador de pontos, XP e estrelas
- Progresso salvo no navegador (localStorage)

> **Versão do app:** v3 (aprovada) — HTML já incluído neste pacote.

---

## 📁 Estrutura do repositório

```
english-grammar-journey/
├── streamlit_app.py                 ← wrapper Streamlit (embute o HTML)
├── English_Grammar_Journey.html     ← o app aprovado (v3)  ⚠️ nome idêntico
├── requirements.txt                 ← dependências
├── .gitignore
└── .streamlit/
    └── config.toml                  ← tema (opcional)
```

> ⚠️ O HTML precisa se chamar **`English_Grammar_Journey.html`** e ficar na
> **mesma pasta** do `streamlit_app.py`. (Já está assim neste pacote.)

---

## 🚀 Passo a passo (igual ao English Journey)

### 1) Criar o repositório no GitHub
1. Acesse [github.com](https://github.com) → **New repository**.
2. Nome: `english-grammar-journey` → **Create repository**.

### 2) Subir os arquivos
Pelo site do GitHub (**Add file → Upload files**) ou via Git:
```bash
git clone https://github.com/SEU_USUARIO/english-grammar-journey.git
cd english-grammar-journey

# copie para cá o conteúdo desta pasta (os 5 itens, incluindo a pasta .streamlit)

git add .
git commit -m "English Grammar Journey no Streamlit"
git push
```

> 💡 A pasta precisa se chamar **`.streamlit`** (com ponto na frente) e conter o `config.toml`.
> Ao subir pelo site do GitHub, arraste também o arquivo de dentro dela.

### 3) Publicar no Streamlit Community Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login com o GitHub.
2. **New app** → selecione o repositório `english-grammar-journey`.
3. **Branch:** `main` • **Main file path:** `streamlit_app.py`.
4. **Deploy!** 🎉

Em ~1 min o app fica no ar num link `https://SEU-APP.streamlit.app`.

---

## 🖥️ Rodar localmente (opcional)
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Abre em `http://localhost:8501`.

---

## 🔊 Áudio
Os navegadores só liberam som **após o primeiro clique** na página (política padrão).
Ao abrir, clique em qualquer botão (ou no 🎵) para ativar música e efeitos.

## 💾 Progresso
Salvo no **localStorage do navegador** (chave `egj_state_v3`), por dispositivo.
Não é compartilhado entre usuários.

## 🔄 Atualizar depois
1. Substitua `English_Grammar_Journey.html` no repositório pela nova versão aprovada.
2. `git add . && git commit -m "nova versão" && git push`
3. O Streamlit Cloud atualiza sozinho.
