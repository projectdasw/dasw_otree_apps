from otree.api import *
from .transcription_data import TRANSCRIPTION_TASKS
import time
import random

doc = """
RET Transcription -  Exact Transcription
"""

class C(BaseConstants):
    NAME_IN_URL = 'transcription_exact'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GAME_TIME = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # game countdown
    start_time = models.FloatField(initial=0)
    end_time = models.FloatField(initial=0)

    # result of game
    completed_count = models.IntegerField(initial=0)
    correct_count = models.IntegerField(initial=0)
    incorrect_count = models.IntegerField(initial=0)
    score = models.IntegerField(initial=0)


# =============================================================
# TIMER
# =============================================================

def initialize_timer(player):
    if player.start_time and player.end_time:
        return

    now = time.time()
    player.start_time = now
    player.end_time = now + C.GAME_TIME

def get_remaining_time(player):
    if not player.end_time:
        return C.GAME_TIME

    return max(0, player.end_time - time.time())

def is_game_active(player):
    return get_remaining_time(player) > 0

# =============================================================
# TASK SEQUENCE
# =============================================================

def initialize_task_queue(player):
    participant = player.participant

    if 'transcription_exact_task_queue' not in participant.vars:
        task_queue = list(range(len(TRANSCRIPTION_TASKS)))
        random.shuffle(task_queue)
        participant.vars['transcription_exact_task_queue'] = task_queue

def get_current_task(player):
    participant = player.participant

    initialize_task_queue(player)
    current_task_id = participant.vars.get('transcription_exact_current_task')

    # Belum ada current task
    if current_task_id is None:
        task_queue = participant.vars['transcription_exact_task_queue']

        # Queue kosong → buat queue baru
        if not task_queue:
            task_queue = list(range(len(TRANSCRIPTION_TASKS)))
            random.shuffle(task_queue)

        # Ambil task pertama
        current_task_id = task_queue.pop(0)
        participant.vars['transcription_exact_task_queue'] = task_queue
        participant.vars['transcription_exact_current_task'] = current_task_id

    return TRANSCRIPTION_TASKS[current_task_id]

def move_to_next_task(player):
    participant = player.participant

    initialize_task_queue(player)
    task_queue = participant.vars['transcription_exact_task_queue']

    # Jika queue habis, buat queue baru
    if not task_queue:
        task_queue = list(range(len(TRANSCRIPTION_TASKS)))
        random.shuffle(task_queue)

    next_task_id = task_queue.pop(0)
    participant.vars['transcription_exact_task_queue'] = task_queue
    participant.vars['transcription_exact_current_task'] = next_task_id

    return TRANSCRIPTION_TASKS[next_task_id]

# =============================================================
# ATTEMPT HISTORY
# =============================================================

def get_attempt_history(player):
    return player.participant.vars.setdefault('transcription_exact_attempts', [])

def save_attempt(player, source_text, participant_answer, is_correct, score_earned):
    attempts = get_attempt_history(player)

    attempts.append(
        dict(
            attempt_number=player.completed_count,
            source_text=source_text,
            participant_answer=participant_answer,
            correct=is_correct,
            score=score_earned,
            timestamp=time.time(),
        )
    )

    player.participant.vars['transcription_exact_attempts'] = attempts


class introduction(Page):
    @staticmethod
    def is_displayed(player):
        return True


class instructions(Page):
    @staticmethod
    def is_displayed(player):
        return True


class game(Page):
    @staticmethod
    def is_displayed(player):
        initialize_timer(player)
        initialize_task_queue(player)

        return is_game_active(player)

    @staticmethod
    def vars_for_template(player):
        initialize_timer(player)
        transcription_text = get_current_task(player)

        return dict(
            transcription_text=transcription_text,
            remaining_time=get_remaining_time(player),
            completed_count=player.completed_count,
            correct_count=player.correct_count,
            incorrect_count=player.incorrect_count,
            score=player.score,
        )

    @staticmethod
    def live_method(player, data):
        # =====================================================
        # VALIDATE REQUEST
        # =====================================================

        if not isinstance(data, dict):
            return

        if data.get('type') != 'submit':
            return

        # =====================================================
        # CHECK SERVER TIMER
        # =====================================================

        remaining_time = get_remaining_time(player)

        if remaining_time <= 0:
            return {
                player.id_in_group: dict(
                    type='time_up',
                    score=player.score,
                    completed_count=player.completed_count,
                    correct_count=player.correct_count,
                    incorrect_count=player.incorrect_count,
                )
            }

        # =====================================================
        # GET PARTICIPANT ANSWER
        # =====================================================

        participant_answer = data.get('answer','')

        if not isinstance(participant_answer,str):
            participant_answer = str(participant_answer)

        # =====================================================
        # GET CURRENT TRANSCRIPTION
        # =====================================================

        source_text = get_current_task(player)

        # =====================================================
        # EXACT VALIDATION
        # =====================================================

        is_correct = (participant_answer == source_text)

        # =====================================================
        # SCORE
        # =====================================================

        score_earned = 1 if is_correct else 0

        # =====================================================
        # UPDATE RESULT
        # =====================================================

        player.completed_count += 1

        if is_correct:
            player.correct_count += 1
            player.score += score_earned
        else:
            player.incorrect_count += 1

        # =====================================================
        # SAVE ATTEMPT
        # =====================================================

        save_attempt(
            player=player,
            source_text=source_text,
            participant_answer=participant_answer,
            is_correct=is_correct,
            score_earned=score_earned,
        )

        # =====================================================
        # GET NEXT TASK
        # =====================================================

        next_task = move_to_next_task(player)

        # =====================================================
        # CHECK TIMER AGAIN
        # =====================================================

        remaining_time = get_remaining_time(player)

        if remaining_time <= 0:
            return {
                player.id_in_group: dict(
                    type='time_up',
                    score=player.score,
                    completed_count=player.completed_count,
                    correct_count=player.correct_count,
                    incorrect_count=player.incorrect_count,
                )
            }

        # =====================================================
        # DEBUG
        # =====================================================

        # print("TRANSCRIPTION LIVE RESPONSE:",next_task)

        # =====================================================
        # SEND RESPONSE TO BROWSER
        # =====================================================

        return {
            player.id_in_group: dict(
                type='next_task',
                next_task=next_task,
                correct=is_correct,
                score_earned=score_earned,
                score=player.score,
                completed_count=player.completed_count,
                correct_count=player.correct_count,
                incorrect_count=player.incorrect_count,
                remaining_time=remaining_time,
            )
        }


class results(Page):
    @staticmethod
    def vars_for_template(player):
        accuracy = (player.correct_count / player.completed_count * 100 if player.completed_count > 0 else 0)
        accuracy = round(accuracy, 1)

        return dict(
            score=player.score,
            completed_count=player.completed_count,
            correct_count=player.correct_count,
            incorrect_count=player.incorrect_count,
            accuracy=accuracy,
        )

    @staticmethod
    def before_next_page(player,timeout_happened):
        participant = player.participant

        participant.vars['transcription_exact_score'] = player.score
        participant.vars['transcription_exact_completed'] = player.completed_count
        participant.vars['transcription_exact_correct'] = player.correct_count
        participant.vars['transcription_exact_incorrect'] = player.incorrect_count
        participant.vars['transcription_exact_accuracy'] = (
            player.correct_count / player.completed_count * 100 if player.completed_count > 0 else 0
        )


page_sequence = [introduction, instructions, game, results]
