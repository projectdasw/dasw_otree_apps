from otree.api import *
import random
import json

doc = """
RET - Word Search
"""

class Constants(BaseConstants):
    name_in_url = "word_search"
    players_per_group = None
    num_rounds = 1

    # game setup
    board_rows = 5  # Jumlah baris papan
    board_columns = 7  # Jumlah kolom papan
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    points_per_correct = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    total_score = models.IntegerField(initial=0)
    count_guess = models.IntegerField(initial=0)
    actual_count = models.IntegerField(initial=0)
    current_target = models.StringField()  # Target huruf/angka yang diacak setiap putaran
    puzzle_board = models.LongStringField(initial="")

def generate_puzzle():
    target = random.choice(Constants.characters)

    board = [
        [
            random.choice(Constants.characters)
            for _ in range(Constants.board_columns)
        ]
        for _ in range(Constants.board_rows)
    ]

    actual_count = sum(
        row.count(target)
        for row in board
    )

    return board, target, actual_count

def live_game(player: Player, data):
    if "count_guess" not in data:
        return

    try:
        guess = int(data["count_guess"])
    except (ValueError, TypeError):
        return {
            player.id_in_group: {
                "error": "Please enter a valid number."
            }
        }

    if guess < 0:
        return {
            player.id_in_group: {
                "error": "Please enter a valid number."
            }
        }

    # Simpan jawaban pemain
    player.count_guess = guess

    # Jawaban puzzle saat ini
    correct_answer = player.actual_count

    # Periksa jawaban
    is_correct = guess == correct_answer

    if is_correct:
        player.total_score += Constants.points_per_correct

    # =====================================
    # GENERATE PUZZLE BARU
    # =====================================

    board, target, actual_count = generate_puzzle()

    # Simpan puzzle baru
    player.puzzle_board = json.dumps(board)
    player.current_target = target
    player.actual_count = actual_count

    return {
        player.id_in_group: {
            "new_board": board,
            "new_target_character": target,
            "new_score": player.total_score,
            "correct": is_correct,
            "correct_answer": correct_answer,
        }
    }


class word_search_game(Page):
    live_method = live_game

    @staticmethod
    def vars_for_template(player: Player):
        # Jika puzzle belum pernah dibuat
        if not player.puzzle_board:
            board, target, actual_count = generate_puzzle()
            player.puzzle_board = json.dumps(board)
            player.current_target = target
            player.actual_count = actual_count
        else:
            board = json.loads(player.puzzle_board)

        return {
            "board": board,
            "target_character": player.current_target,
            "player_score": player.total_score,
        }


page_sequence = [word_search_game]
