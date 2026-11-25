-- PyQuest Arcade: status agregado da rodada sem expor respostas individuais
-- A tabela pyquest_answers não deve ser consultável diretamente pelo navegador.

drop policy if exists "PyQuest respostas - leitura publica" on public.pyquest_answers;
revoke select, insert, update, delete on public.pyquest_answers from anon, authenticated;

create or replace function public.pyquest_get_round_status(
  p_room_pin text,
  p_question_index integer
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_answered_count integer;
  v_player_count integer;
  v_room_status text;
  v_current_question integer;
  v_round_ends_at timestamptz;
  v_players jsonb;
begin
  select status, current_question, round_ends_at, players
    into v_room_status, v_current_question, v_round_ends_at, v_players
    from public.pyquest_rooms
   where pin = p_room_pin;

  if not found then
    raise exception 'Sala não encontrada.';
  end if;

  select count(*) into v_answered_count
    from public.pyquest_answers
   where room_pin = p_room_pin
     and question_index = p_question_index;

  select count(*) into v_player_count
    from jsonb_array_elements(coalesce(v_players, '[]'::jsonb)) p
   where coalesce(p->>'status', 'waiting') <> 'left';

  return jsonb_build_object(
    'answered_count', v_answered_count,
    'player_count', v_player_count,
    'all_answered', (v_player_count > 0 and v_answered_count >= v_player_count),
    'round_ends_at', v_round_ends_at,
    'current_question', v_current_question,
    'status', v_room_status
  );
end;
$$;

revoke all on function public.pyquest_get_round_status(text, integer) from public;
grant execute on function public.pyquest_get_round_status(text, integer) to anon, authenticated;
