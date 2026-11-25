-- PyQuest Arcade: respostas individuais por rodada
-- Execute no Supabase SQL Editor depois da migration 20261125140000_multiplayer_room_state.sql.
-- Esta etapa registra cada resposta separadamente para evitar que um jogador
-- sobrescreva a resposta de outro em atualizações concorrentes do JSONB da sala.

create table if not exists public.pyquest_answers (
  room_pin text not null,
  question_index integer not null check (question_index >= 0),
  player_id text not null,
  player_name text not null default 'Jogador',
  selected_option integer not null check (selected_option >= 0),
  is_correct boolean not null,
  points_awarded integer not null default 0 check (points_awarded >= 0),
  answered_at timestamptz not null default now(),
  primary key (room_pin, question_index, player_id)
);

create index if not exists pyquest_answers_room_round_idx
  on public.pyquest_answers (room_pin, question_index, answered_at);

alter table public.pyquest_answers enable row level security;

drop policy if exists "PyQuest respostas - leitura publica" on public.pyquest_answers;
create policy "PyQuest respostas - leitura publica"
  on public.pyquest_answers for select to anon using (true);

-- A gravação acontece por função, não por INSERT/UPDATE direto do navegador.
revoke insert, update, delete on public.pyquest_answers from anon, authenticated;

create or replace function public.pyquest_submit_answer(
  p_room_pin text,
  p_question_index integer,
  p_player_id text,
  p_player_name text,
  p_selected_option integer
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room public.pyquest_rooms%rowtype;
  v_question jsonb;
  v_answer integer;
  v_is_correct boolean;
  v_seconds_left integer;
  v_points integer;
  v_player_exists boolean;
  v_answered_count integer;
  v_player_count integer;
begin
  if p_room_pin is null or p_player_id is null or p_player_id = ''
     or p_question_index is null or p_selected_option is null
     or p_selected_option < 0 then
    raise exception 'Resposta inválida.';
  end if;

  select * into v_room
    from public.pyquest_rooms
   where pin = p_room_pin
   for update;

  if not found or v_room.status <> 'playing' then
    raise exception 'A sala não está em uma rodada ativa.';
  end if;

  if v_room.current_question <> p_question_index then
    raise exception 'Esta pergunta não está mais ativa.';
  end if;

  if v_room.round_ends_at is null or now() > v_room.round_ends_at then
    raise exception 'O tempo desta pergunta terminou.';
  end if;

  select exists (
    select 1
      from jsonb_array_elements(coalesce(v_room.players, '[]'::jsonb)) p
     where p->>'id' = p_player_id
  ) into v_player_exists;

  if not v_player_exists then
    raise exception 'Jogador não pertence a esta sala.';
  end if;

  v_question := v_room.questions -> p_question_index;
  if v_question is null then
    raise exception 'Pergunta não encontrada.';
  end if;

  v_answer := (v_question->>'answer')::integer;
  if v_answer is null or p_selected_option >= jsonb_array_length(v_question->'options') then
    raise exception 'Alternativa inválida.';
  end if;

  v_is_correct := (p_selected_option = v_answer);
  v_seconds_left := greatest(0, ceil(extract(epoch from (v_room.round_ends_at - now())))::integer);
  v_points := case when v_is_correct then 500 + (v_seconds_left * 20) else 0 end;

  insert into public.pyquest_answers (
    room_pin, question_index, player_id, player_name,
    selected_option, is_correct, points_awarded
  ) values (
    p_room_pin, p_question_index, p_player_id,
    coalesce(nullif(trim(p_player_name), ''), 'Jogador'),
    p_selected_option, v_is_correct, v_points
  )
  on conflict (room_pin, question_index, player_id) do nothing;

  select count(*) into v_answered_count
    from public.pyquest_answers
   where room_pin = p_room_pin and question_index = p_question_index;

  select count(*) into v_player_count
    from jsonb_array_elements(coalesce(v_room.players, '[]'::jsonb)) p
   where coalesce(p->>'status', 'waiting') <> 'left';

  return jsonb_build_object(
    'is_correct', v_is_correct,
    'points_awarded', v_points,
    'answered_count', v_answered_count,
    'player_count', v_player_count,
    'all_answered', (v_player_count > 0 and v_answered_count >= v_player_count)
  );
end;
$$;

revoke all on function public.pyquest_submit_answer(text, integer, text, text, integer) from public;
grant execute on function public.pyquest_submit_answer(text, integer, text, text, integer) to anon, authenticated;

comment on table public.pyquest_answers is
  'Uma linha por jogador e pergunta; evita colisões de respostas simultâneas.';
