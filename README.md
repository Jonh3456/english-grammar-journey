# 🦉 English Grammar Journey — Streamlit + Nuvem (Supabase)

App de gramática inglesa gamificado (estilo Duolingo) com **login por usuário** e
**progresso salvo na nuvem** — o jogador entra com a mesma conta em qualquer
dispositivo e continua de onde parou.

- **82 capítulos** • **3 níveis** (Fácil / Médio / Difícil) • resumo do capítulo
- Timer, música, fogos, contador de pontos, XP e estrelas
- 🔐 **Login/registro** com senha (hash) • 💾 **save na nuvem** (Supabase/Postgres, grátis)
- Funciona também em **modo local** se a nuvem não estiver configurada

---

## 📁 Estrutura do repositório
```
english-grammar-journey/
├── streamlit_app.py                 ← wrapper (injeta credenciais + embute o HTML)
├── English_Grammar_Journey.html     ← app (versão nuvem)  ⚠️ nome idêntico
├── supabase_schema.sql              ← script do banco (rodar 1x no Supabase)
├── requirements.txt
├── .gitignore
└── .streamlit/
    ├── config.toml                  ← tema
    └── secrets.toml.example         ← modelo dos segredos (NÃO subir o real)
```

---

## 🟢 PARTE 1 — Criar o banco de dados grátis (Supabase)

1. Acesse **[supabase.com](https://supabase.com)** → **Start your project** → login com GitHub.
2. **New project** → dê um nome (ex.: `egj`), crie uma senha do banco e escolha a região
   mais próxima → **Create new project** (aguarde ~1 min).
3. No menu lateral, abra **SQL Editor** → **New query**.
4. **Cole todo o conteúdo de `supabase_schema.sql`** e clique **RUN** ▶.
   Isso cria a tabela `egj_players` e as funções de login/registro/save.
5. Pegue suas credenciais em **Project Settings → API**:
   - **Project URL** → ex.: `https://abcd1234.supabase.co`
   - **Project API keys → anon public** → uma chave longa `eyJ...`

> 🔒 A chave **anon** é feita para ficar no cliente. A tabela está protegida:
> o app só consegue chamar as **funções** (login/registro/save), não ler os dados direto.

---

## 🟢 PARTE 2 — Subir ao GitHub

1. Crie o repositório `english-grammar-journey` no GitHub.
2. Envie **todos os arquivos desta pasta** (incluindo a pasta `.streamlit`).
   - ⚠️ **NÃO** suba `secrets.toml` (só o `.example`). O `.gitignore` já protege.

```bash
git clone https://github.com/SEU_USUARIO/english-grammar-journey.git
cd english-grammar-journey
# copie os arquivos para cá
git add .
git commit -m "English Grammar Journey — Streamlit + Supabase"
git push
```

---

## 🟢 PARTE 3 — Publicar no Streamlit + configurar segredos

1. Acesse **[share.streamlit.io](https://share.streamlit.io)** → **New app**.
2. Repositório: `english-grammar-journey` • Branch: `main` • Main file: `streamlit_app.py`.
3. Antes (ou depois) do deploy, abra **Manage app → Settings → Secrets** e cole:
   ```toml
   SUPABASE_URL = "https://SEU-PROJETO.supabase.co"
   SUPABASE_ANON_KEY = "eyJ...sua-chave-anon..."
   ```
4. **Save** → o app reinicia e o login/nuvem passam a funcionar. 🎉

---

## 🖥️ Rodar localmente (opcional)
```bash
pip install -r requirements.txt
# crie .streamlit/secrets.toml a partir do .example e preencha suas credenciais
streamlit run streamlit_app.py
```

---

## 🔄 Como funciona o salvamento
- Ao **entrar**, o app baixa seu progresso da nuvem.
- A cada acerto/conclusão, ele **envia o progresso** para a nuvem (com pequeno atraso, para não sobrecarregar).
- Um **cache local** (localStorage) é mantido — se ficar sem internet, o jogo continua e sincroniza quando voltar.
- Sessão válida por **60 dias** (auto-login). Botão **Sair (⎋)** encerra a sessão.

## 🧰 Solução de problemas
- **"Falha de conexão" no login:** confira `SUPABASE_URL`/`SUPABASE_ANON_KEY` nos Secrets e se o `supabase_schema.sql` foi executado.
- **App em modo local (sem nuvem):** significa que os secrets não chegaram — revise a etapa 3.
- **Áudio mudo:** clique em qualquer botão (ou no 🎵) — navegadores só liberam som após o 1º clique.
