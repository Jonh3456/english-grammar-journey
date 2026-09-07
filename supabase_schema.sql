-- ============================================================
-- English Grammar Journey — Banco de dados (Supabase / Postgres)
-- Cole TODO este conteúdo no SQL Editor do Supabase e clique RUN.
-- Cria a tabela de jogadores + funções seguras de login/registro/save/ranking.
-- ============================================================

create extension if not exists pgcrypto;

-- Tabela de jogadores (senha guardada como HASH bcrypt; nunca em texto puro)
create table if not exists egj_players (
  username    text primary key,
  pass_hash   text not null,
  state       jsonb default '{}'::jsonb,
  token       uuid,
  token_exp   timestamptz,
  updated_at  timestamptz default now()
);

-- Bloqueia acesso direto à tabela pelo cliente (anon).
-- O app só consegue usar as FUNÇÕES abaixo (SECURITY DEFINER).
alter table egj_players enable row level security;

-- ---------- REGISTRO ----------
create or replace function egj_register(p_user text, p_pass text)
returns json language plpgsql security definer as $$
declare u text := lower(trim(p_user));
begin
  if length(u) < 3 then
    return json_build_object('ok', false, 'msg', 'Usuário muito curto (mín. 3).');
  end if;
  if length(p_pass) < 4 then
    return json_build_object('ok', false, 'msg', 'Senha muito curta (mín. 4).');
  end if;
  if exists (select 1 from egj_players where username = u) then
    return json_build_object('ok', false, 'msg', 'Este usuário já existe.');
  end if;
  insert into egj_players(username, pass_hash)
    values (u, crypt(p_pass, gen_salt('bf')));
  return json_build_object('ok', true);
end $$;

-- ---------- LOGIN ----------
create or replace function egj_login(p_user text, p_pass text)
returns json language plpgsql security definer as $$
declare u text := lower(trim(p_user)); r egj_players; t uuid;
begin
  select * into r from egj_players where username = u;
  if not found then
    return json_build_object('ok', false, 'msg', 'Usuário não encontrado.');
  end if;
  if r.pass_hash <> crypt(p_pass, r.pass_hash) then
    return json_build_object('ok', false, 'msg', 'Senha incorreta.');
  end if;
  t := gen_random_uuid();
  update egj_players
     set token = t, token_exp = now() + interval '60 days'
   where username = u;
  return json_build_object('ok', true, 'token', t, 'state', r.state);
end $$;

-- ---------- SALVAR PROGRESSO ----------
create or replace function egj_save(p_user text, p_token uuid, p_state jsonb)
returns json language plpgsql security definer as $$
declare u text := lower(trim(p_user)); r egj_players;
begin
  select * into r from egj_players where username = u;
  if not found then
    return json_build_object('ok', false, 'msg', 'Usuário inexistente.');
  end if;
  if r.token is null or r.token <> p_token or r.token_exp < now() then
    return json_build_object('ok', false, 'msg', 'Sessão inválida.');
  end if;
  update egj_players
     set state = p_state, updated_at = now()
   where username = u;
  return json_build_object('ok', true);
end $$;

-- ---------- CARREGAR PROGRESSO ----------
create or replace function egj_load(p_user text, p_token uuid)
returns json language plpgsql security definer as $$
declare u text := lower(trim(p_user)); r egj_players;
begin
  select * into r from egj_players where username = u;
  if not found then
    return json_build_object('ok', false);
  end if;
  if r.token is null or r.token <> p_token or r.token_exp < now() then
    return json_build_object('ok', false, 'msg', 'Sessão inválida.');
  end if;
  return json_build_object('ok', true, 'state', r.state);
end $$;

-- ---------- RANKING (top jogadores por XP) ----------
-- Retorna lista pública: usuário, XP, estrelas e capítulos concluídos.
-- Não expõe senhas nem tokens.
create or replace function egj_ranking(p_limit int default 50)
returns json language plpgsql security definer as $$
declare res json;
begin
  select coalesce(json_agg(row_to_json(t)), '[]'::json) into res
  from (
    select
      username,
      coalesce((state->>'xp')::int, 0) as xp,
      coalesce((select count(*) from jsonb_object_keys(
                 coalesce(state->'chapters','{}'::jsonb)) k
                 where (state->'chapters'->k->>'done')::boolean), 0) as done,
      coalesce((select sum( coalesce((state->'chapters'->k->>'stars')::int,0) )
                 from jsonb_object_keys(coalesce(state->'chapters','{}'::jsonb)) k), 0) as stars
    from egj_players
    where state ? 'xp'
    order by xp desc, stars desc
    limit greatest(1, least(p_limit, 200))
  ) t;
  return json_build_object('ok', true, 'rows', res);
end $$;

-- Permite que o cliente (chave anônima) execute SOMENTE estas funções.
grant execute on function egj_register(text, text)       to anon;
grant execute on function egj_login(text, text)          to anon;
grant execute on function egj_save(text, uuid, jsonb)    to anon;
grant execute on function egj_load(text, uuid)           to anon;
grant execute on function egj_ranking(int)               to anon;
