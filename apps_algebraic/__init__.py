from otree.api import *
import random
import time

doc = """
RET - Algebraic
"""

class Constants(BaseConstants):
    name_in_url = "apps_algebraic"
    players_per_group = None
    num_rounds = 1
    duration = 5 # timer permainan
    points_correct = 1 # skor per jawaban benar


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    total_questions = models.IntegerField(initial=0)
    correct_count = models.IntegerField(initial=0)
    wrong_count = models.IntegerField(initial=0)
    score_earned = models.LongStringField(initial='')
    total_score = models.IntegerField(initial=0)
    correct_answer = models.LongStringField(initial='')
    player_answer = models.LongStringField(initial='')
    is_correct = models.LongStringField(initial='')


def get_duration(player):
    return Constants.duration


def get_points_correct(player):
    return Constants.points_correct


def append_history(field_value, new_value):
    """Menambahkan nilai ke riwayat teks yang dipisahkan koma."""
    if field_value:
        return f'{field_value},{new_value}'
    return str(new_value)


def generate_question():
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a + b
        symbol = '+'
    elif operation == '-':
        a = random.randint(1, 100)
        b = random.randint(1, a)
        answer = a - b
        symbol = '−'
    elif operation == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        answer = a * b
        symbol = '×'
    else:
        divisor = random.randint(1, 12)
        quotient = random.randint(1, 12)
        a = divisor * quotient
        b = divisor
        answer = quotient
        symbol = '÷'

    question = f'{a} {symbol} {b} = ?'
    return question, answer

def create_next_question(player):
    participant = player.participant
    question, answer = generate_question()

    participant.vars['aljebraic_question'] = question
    participant.vars['aljebraic_answer'] = answer
    participant.vars['aljebraic_question_id'] = (participant.vars.get('aljebraic_question_id', 0) + 1)

    # Menghitung setiap soal yang ditampilkan.
    player.total_questions += 1


class instruction(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            duration=get_duration(player),
            points_correct=get_points_correct(player),
        )


class game(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        duration = get_duration(player)

        # Waktu mulai hanya dibuat satu kali.
        # Refresh halaman tidak mengulang timer.
        if 'aljebraic_start_time' not in participant.vars:
            participant.vars['aljebraic_start_time'] = time.time()

        elapsed = time.time() - participant.vars['aljebraic_start_time']
        return max(0, duration - elapsed)

    @staticmethod
    def vars_for_template(player):
        game.get_timeout_seconds(player)
        participant = player.participant

        if 'aljebraic_question' not in participant.vars:
            create_next_question(player)

        start_time = participant.vars['aljebraic_start_time']
        remaining = max(0, get_duration(player) - (time.time() - start_time))

        return dict(
            question=participant.vars['aljebraic_question'],
            question_id=participant.vars['aljebraic_question_id'],
            remaining_seconds=remaining,
            correct_count=player.correct_count,
            wrong_count=player.wrong_count,
            total_score=player.total_score,
        )

    @staticmethod
    def live_method(player, data):
        participant = player.participant
        duration = get_duration(player)
        start_time = participant.vars.get('aljebraic_start_time')

        if start_time is None:
            return {
                player.id_in_group: {
                    'finished': True,
                }
            }

        elapsed = time.time() - start_time

        # Validasi timer di server.
        if elapsed >= duration:
            return {
                player.id_in_group: {
                    'finished': True,
                    'correct_count': player.correct_count,
                    'wrong_count': player.wrong_count,
                    'total_score': player.total_score,
                }
            }

        if data.get('type') == 'finish':
            return {
                player.id_in_group: {
                    'finished': True,
                    'correct_count': player.correct_count,
                    'wrong_count': player.wrong_count,
                    'total_score': player.total_score,
                }
            }

        if data.get('type') != 'answer':
            return

        # Validasi jawaban berupa bilangan bulat.
        try:
            player_answer = int(str(data.get('answer', '')).strip())
        except (TypeError, ValueError):
            return {
                player.id_in_group: {
                    'error': 'Masukkan jawaban berupa bilangan bulat.',
                }
            }

        submitted_question_id = data.get('question_id')
        current_question_id = participant.vars.get('aljebraic_question_id')

        # Mencegah jawaban ganda atau jawaban untuk soal lama.
        if submitted_question_id != current_question_id:
            return {
                player.id_in_group: {
                    'stale': True,
                }
            }

        correct_answer = participant.vars['aljebraic_answer']
        is_correct = player_answer == correct_answer
        score_earned = (get_points_correct(player) if is_correct else 0)

        # Simpan seluruh riwayat jawaban di model Player.
        player.correct_answer = append_history(
            player.correct_answer,
            correct_answer,
        )
        player.player_answer = append_history(
            player.player_answer,
            player_answer,
        )
        player.is_correct = append_history(
            player.is_correct,
            str(is_correct).lower(),
        )
        player.score_earned = append_history(
            player.score_earned,
            score_earned,
        )

        # Perbarui rekapitulasi hasil.
        if is_correct:
            player.correct_count += 1
            player.total_score += score_earned
        else:
            player.wrong_count += 1

        # Periksa kembali waktu sebelum membuat soal berikutnya.
        if time.time() - start_time >= duration:
            return {
                player.id_in_group: {
                    'finished': True,
                    'correct_count': player.correct_count,
                    'wrong_count': player.wrong_count,
                    'total_score': player.total_score,
                }
            }

        create_next_question(player)

        return {
            player.id_in_group: {
                'question': participant.vars['aljebraic_question'],
                'question_id': participant.vars[
                    'aljebraic_question_id'
                ],
                'correct_count': player.correct_count,
                'wrong_count': player.wrong_count,
                'total_score': player.total_score,
            }
        }


class results(Page):
    @staticmethod
    def vars_for_template(player):
        unanswered = max(0, player.total_questions - player.correct_count - player.wrong_count)

        return dict(
            total_questions=player.total_questions,
            correct_count=player.correct_count,
            wrong_count=player.wrong_count,
            unanswered=unanswered,
            total_score=player.total_score,
        )



page_sequence = [instruction, game, results]
