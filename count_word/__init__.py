from otree.api import *
import random
import json
import time

doc = """
RET - Count Word
"""


class Constants(BaseConstants):
    name_in_url = 'count_word'
    players_per_group = None
    num_rounds = 1
    board_rows = 5
    board_columns = 7
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    game_duration = 10000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    count_guess = models.IntegerField(initial=0)
    actual_count = models.IntegerField(initial=0)
    current_target = models.StringField(initial="")
    total_score = models.IntegerField(initial=0)
    current_board = models.LongStringField(initial="") # Menyimpan board dalam bentuk JSON
    correct_answers = models.IntegerField(initial=0)
    wrong_answers = models.IntegerField(initial=0)
    total_attempts = models.IntegerField(initial=0)
    game_start_time = models.FloatField(initial=0)
    game_end_time = models.FloatField(initial=0)
    game_finished = models.BooleanField(initial=False) # Menandakan apakah game sudah selesai


def generate_board():
    """Generate board baru."""
    return [
        [
            random.choice(Constants.characters)
            for _ in range(Constants.board_columns)
        ]
        for _ in range(Constants.board_rows)
    ]

def generate_game():
    """Generate target, board, dan jumlah target."""
    target = random.choice(Constants.characters)
    board = generate_board()
    actual_count = sum(
        row.count(target)
        for row in board
    )

    return target, board, actual_count

def start_game_timer(player):
    now = time.time()
    player.game_start_time = now
    player.game_end_time = now + Constants.game_duration

def get_remaining_time(player):
    if not player.game_end_time:
        return Constants.game_duration

    remaining = player.game_end_time - time.time()
    return max(0, remaining)

def save_game_state(player, target, board, actual_count):
    """Simpan state game ke database."""
    player.current_target = target
    player.current_board = json.dumps(board)
    player.actual_count = actual_count

def validate_guess(value):
    """
    Validasi jawaban Count Word.
    Return:
        (True, integer_value)
    atau
        (False, None)
    """

    if value is None:
        return False, None

    if isinstance(value, bool):
        return False, None

    if isinstance(value, float):
        return False, None

    if isinstance(value, int):
        guess = value

    elif isinstance(value, str):
        value = value.strip()

        if not value:
            return False, None

        if not value.isdigit():
            return False, None

        guess = int(value)

    else:
        return False, None

    if guess < 0:
        return False, None

    max_count = (Constants.board_rows * Constants.board_columns)

    if guess > max_count:
        return False, None

    return True, guess

def live_game(player: Player, data):
    # Game sudah selesai?
    if player.game_finished:
        return

    # Timer selesai?
    if data.get('timer_finished'):
        if get_remaining_time(player) <= 0:
            player.game_finished = True

            return {
                player.id_in_group: {
                    'game_finished': True,
                    'new_score': player.total_score,
                }
            }

        return

    # Cek waktu server
    remaining_time = get_remaining_time(player)

    if remaining_time <= 0:
        player.game_finished = True

        return {
            player.id_in_group: {
                'game_finished': True,
                'new_score': player.total_score,
            }
        }

    # Pastikan ada jawaban
    if 'count_guess' not in data:
        return

    # Validasi jawaban
    is_valid, guess = validate_guess(data.get('count_guess'))

    if not is_valid:
        return {
            player.id_in_group: {
                'validation_error': True,
                'message': 'Masukkan jumlah berupa bilangan bulat 0 atau lebih.'
            }
        }

    # Batas maksimum
    max_count = (Constants.board_rows * Constants.board_columns)

    if guess > max_count:
        return {
            player.id_in_group: {
                'validation_error': True,
                'message': f'Jumlah tidak boleh lebih dari {max_count}.'
            }
        }

    player.count_guess = guess # Simpan jawaban
    is_correct = guess == player.actual_count # Cek jawaban
    score_earned = 0
    player.total_attempts += 1

    if is_correct:
        score_earned = 3
        player.total_score += score_earned
        player.correct_answers += 1
    else:
        player.wrong_answers += 1

    # Cek waktu lagi
    remaining_time = get_remaining_time(player)

    if remaining_time <= 0:
        player.game_finished = True

        return {
            player.id_in_group: {
                'game_finished': True,
                'new_score': player.total_score,
            }
        }

    # Generate soal berikutnya
    target, board, actual_count = generate_game()
    save_game_state(player, target, board, actual_count)

    return {
        player.id_in_group: {
            'new_board': board,
            'new_target_character': target,
            'new_score': player.total_score,
            'score_earned': score_earned,
            'is_correct': is_correct,
            'remaining_time': remaining_time,
        }
    }


class game(Page):
    live_method = live_game

    @staticmethod
    def vars_for_template(player: Player):
        # Generate game HANYA jika belum ada game
        if not player.current_board:
            target, board, actual_count = generate_game()
            save_game_state(player, target, board, actual_count)
            start_game_timer(player)

        board = json.loads(player.current_board)
        remaining_time = get_remaining_time(player)

        return {
            'board': board,
            'target_character': player.current_target,
            'player_score': player.total_score,
            'remaining_time': remaining_time,

        }


class results(Page):
    @staticmethod
    def vars_for_template(player):

        return {
            'total_score': player.total_score,
            'correct_answers': player.correct_answers,
            'wrong_answers': player.wrong_answers,
            'total_attempts': player.total_attempts,
        }


page_sequence = [game, results]