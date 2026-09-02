from otree.api import *
from .transcription_data import TRANSCRIPTION_TASKS
import random
import time

doc = """
RET - Continuous Transcription
"""


class C(BaseConstants):
    NAME_IN_URL = 'transcription_continuous'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GAME_DURATION = 60
    REWARD_PER_CORRECT = cu(0.10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    current_text = models.LongStringField(blank=True)
    transcription_answer = models.LongStringField(blank=True)
    total_attempts = models.IntegerField(initial=0)
    correct_answers = models.IntegerField(initial=0)
    errors = models.IntegerField(initial=0)
    reward = models.CurrencyField(initial=cu(0))
    accuracy = models.FloatField(initial=0)
    start_time = models.FloatField(blank=True)
    end_time = models.FloatField(blank=True)

def calculate_accuracy(player):
    if player.total_attempts <= 0:
        return 0.0

    return (player.correct_answers / player.total_attempts) * 100

class game(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # ---------------------------------------------
        # Initialize timer
        # ---------------------------------------------
        start_time = player.field_maybe_none('start_time')
        end_time = player.field_maybe_none('end_time')

        if start_time is None or end_time is None:
            start_time = time.time()
            end_time = (start_time + C.GAME_DURATION)
            player.start_time = start_time
            player.end_time = end_time

        # ---------------------------------------------
        # Initialize current text
        # ---------------------------------------------
        current_text = player.field_maybe_none('current_text')

        if not current_text:
            current_text = random.choice(TRANSCRIPTION_TASKS)
            player.current_text = current_text

        # ---------------------------------------------
        # Remaining time
        # ---------------------------------------------
        remaining_time = max(0, end_time - time.time())

        return dict(
            transcription_text=current_text,
            total_attempts=player.total_attempts,
            correct_answers=player.correct_answers,
            errors=player.errors,
            accuracy=float(player.accuracy),
            reward=player.reward,
            remaining_time=remaining_time,
        )

    @staticmethod
    def live_method(player: Player, data):
        if data.get('action') != 'submit':
            return
        # ---------------------------------------------
        # Check server-side timer
        # ---------------------------------------------
        end_time = player.field_maybe_none('end_time')

        if end_time is None:
            return {
                player.id_in_group: dict(
                    action='finished'
                )
            }

        remaining_time = (end_time - time.time())

        if remaining_time <= 0:
            return {
                player.id_in_group: dict(
                    action='finished',
                    total_attempts=player.total_attempts,
                    correct_answers=player.correct_answers,
                    errors=player.errors,
                    reward=float(player.reward),
                )
            }

        # ---------------------------------------------
        # Get answer
        # ---------------------------------------------
        answer = data.get('answer', '')
        current_text = player.field_maybe_none('current_text')

        if not current_text:
            return

        player.total_attempts += 1 # Record attempt
        is_correct = (answer == current_text) # Validate

        # ---------------------------------------------
        # INCORRECT
        # ---------------------------------------------
        if not is_correct:
            player.errors += 1
            player.accuracy = calculate_accuracy(player)

            return {
                player.id_in_group: dict(
                    action='incorrect',
                    total_attempts=player.total_attempts,
                    correct_answers=player.correct_answers,
                    errors=player.errors,
                    accuracy=float(player.accuracy),
                    reward=float(player.reward),
                    remaining_time=max(0, end_time - time.time()),
                    current_text=current_text,
                )
            }

        # ---------------------------------------------
        # CORRECT
        # ---------------------------------------------
        player.correct_answers += 1
        player.accuracy = calculate_accuracy(player)
        player.reward += (C.REWARD_PER_CORRECT) # Add reward

        # ---------------------------------------------
        # Generate next text
        # ---------------------------------------------
        next_text = random.choice(TRANSCRIPTION_TASKS)
        player.current_text = next_text

        # ---------------------------------------------
        # Remaining time
        # ---------------------------------------------
        remaining_time = max(0,end_time - time.time())

        return {
            player.id_in_group: dict(
                action='correct',
                next_text=next_text,
                total_attempts=player.total_attempts,
                correct_answers=player.correct_answers,
                errors=player.errors,
                accuracy=float(player.accuracy),
                reward=float(player.reward),
                remaining_time=remaining_time,
            )
        }


class results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        accuracy = calculate_accuracy(player)
        player.accuracy = accuracy

        return dict(
            completed=player.correct_answers,
            total_attempts=player.total_attempts,
            correct_answers=player.correct_answers,
            errors=player.errors,
            accuracy=accuracy,
            reward=player.reward,
        )

page_sequence = [game, results]