-- PyQuest Arcade: estado sincronizado de partidas multiplayer
-- Execute este arquivo no Supabase SQL Editor antes de ativar a sincronizacao de rodadas.
-- A tabela pyquest_rooms e as colunas basicas ja existem.

alter table public.pyquest_rooms
  add column if not exists host_player_id text,
  add column if not exists questions jsonb not null default '[]'::jsonb,
  add column if not exists round_started_at timestamptz,
  add column if not exists round_duration_seconds integer not null default 25,
  add column if not exists round_ends_at timestamptz,
  add column if not exists answers jsonb not null default '{}'::jsonb,
  add column if not exists game_started_at timestamptz;

-- Garante que os campos JSON tenham o formato esperado.
alter table public.pyquest_rooms
  drop constraint if exists pyquest_rooms_questions_is_array,
  add constraint pyquest_rooms_questions_is_array
    check (jsonb_typeof(questions) = 'array'),
  drop constraint if exists pyquest_rooms_answers_is_object,
  add constraint pyquest_rooms_answers_is_object
    check (jsonb_typeof(answers) = 'object'),
  drop constraint if exists pyquest_rooms_round_duration_valid,
  add constraint pyquest_rooms_round_duration_valid
    check (round_duration_seconds between 5 and 180);

comment on column public.pyquest_rooms.host_player_id is
  'ID do jogador que criou a sala e controla a partida.';
comment on column public.pyquest_rooms.questions is
  'Deck unico de perguntas compartilhado por todos os participantes da sala.';
comment on column public.pyquest_rooms.round_started_at is
  'Horario de inicio da pergunta atual, definido pelo servidor.';
comment on column public.pyquest_rooms.round_ends_at is
  'Horario limite da pergunta atual, definido pelo servidor.';
comment on column public.pyquest_rooms.answers is
  'Respostas recebidas na rodada atual, indexadas pelo ID do jogador.';
