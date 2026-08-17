from otree.api import *
from .utils import (generate_decoding_pairs, generate_target_numbers, build_mapping, decode_letters_to_numbers,
                    check_sequence, validate_answer)
import json
import time

doc = """
RET - Decoding
"""

def format_seconds(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:02d}:{seconds:02d}"

class Constants(BaseConstants):
    name_in_url = "decoding"
    players_per_group = None
    num_rounds = 1
    total_items = 9 # Jumlah pasangan huruf dan angka
    target_count = 5 # Jumlah angka yang harus diterjemahkan
    decoding_time = 1000 # Durasi Decoding Task dalam detik


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    digits = models.StringField(blank=True) # Mapping digit/angka
    letters = models.StringField(blank=True) # Mapping huruf
    target_numbers = models.StringField(blank=True) # Target angka yang harus diterjemahkan
    correct_answers = models.IntegerField(initial=0)
    incorrect_answers = models.IntegerField(initial=0)
    user_answer = models.StringField(blank=True) # Jawaban terakhir peserta
    attempt_history = models.LongStringField(initial="[]", blank=True,) # History berbentuk JSON
    task_started_at = models.FloatField(blank=True,initial=None,)
    task_completed = models.BooleanField(initial=False)

    def start_decoding_task(self):
        """
        Memulai timer RET Decoding.
        Timer hanya dimulai sekali. Refresh halaman tidak akan mereset timer.
        """

        started_at = self.field_maybe_none("task_started_at")
        if started_at is None:
            self.task_started_at = time.time()

    def finish_decoding_task(self):
        """Menandai Decoding Task sebagai selesai."""

        self.task_completed = True

    def get_remaining_time(self):
        """Menghitung waktu tersisa berdasarkan waktu server."""

        started_at = self.field_maybe_none("task_started_at")

        if started_at is None:
            return Constants.decoding_time

        elapsed = time.time() - started_at
        remaining = (Constants.decoding_time - elapsed)

        return max(0, remaining)

    def record_attempt(self, target, answer, decoded, is_correct, mismatches,):
        """Menyimpan satu percobaan peserta ke dalam attempt_history."""

        history_value = self.field_maybe_none("attempt_history")

        if history_value:
            try:
                history = json.loads(history_value)
            except (json.JSONDecodeError, TypeError):
                history = []
        else:
            history = []

        attempt_number = len(history) + 1

        attempt_data = {
            "attempt": attempt_number,
            "target": target,
            "answer": answer,
            "decoded": decoded,
            "correct": is_correct,
            "mismatches": mismatches,
        }

        history.append(attempt_data)

        self.attempt_history = json.dumps(history)

    def get_attempt_history(self):
        """Mengambil seluruh attempt history dalam bentuk list."""

        history_value = self.field_maybe_none("attempt_history")

        if not history_value:
            return []

        try:
            return json.loads(history_value)
        except (json.JSONDecodeError, TypeError):
            return []

    def generate_new_question(self):
        """Membuat soal decoding baru dan menyimpannya ke Player."""

        letters, numbers = generate_decoding_pairs()
        target = generate_target_numbers(numbers, count=Constants.target_count,)

        self.letters = " ".join(letters)
        self.digits = " ".join(str(number) for number in numbers)
        self.target_numbers = " ".join(str(number) for number in target)

    def get_current_mapping(self):
        """Mengambil mapping huruf -> angka dari soal yang sedang aktif."""

        letters = self.letters.split()
        numbers = [int(number)for number in self.digits.split()]

        return build_mapping(letters,numbers)

    def get_current_target(self):
        """Mengambil target angka dari soal aktif."""

        return [int(number) for number in self.target_numbers.split()]

    def solve_answer(self, data):
        # ==========================================
        # 1. CEK APAKAH TASK SUDAH SELESAI
        # ==========================================

        if self.task_completed:
            return {
                "error": "Decoding task has ended.",
                "time_up": True,
            }

        # ==========================================
        # 2. CEK WAKTU
        # ==========================================

        remaining_time = self.get_remaining_time()

        if remaining_time <= 0:
            return {
                "error": "Time is up.",
                "time_up": True,
            }

        # ==========================================
        # 3. AMBIL DAN NORMALISASI JAWABAN
        # ==========================================

        answer = data.get(
            "answer",
            ""
        )

        expected_count = len(
            self.target_numbers.split()
        )

        valid, normalized_answer, error = (
            validate_answer(
                answer,
                expected_count
            )
        )

        if not valid:
            return {
                "error": error,
                "validation_error": True,
            }

        self.user_answer = normalized_answer

        # ==========================================
        # 4. AMBIL TARGET
        # ==========================================

        target = self.get_current_target()
        expected_length = len(target)

        # ==========================================
        # 5. VALIDASI JAWABAN
        # ==========================================

        if not answer:
            return {"error": "Please enter your answer."}

        if len(answer) != expected_length:
            return {"error": (f"Please enter exactly " f"{expected_length} letters.")}

        if not answer.isalpha():
            return {"error": "Please enter letters only."}

        # ==========================================
        # 6. SIMPAN JAWABAN TERAKHIR
        # ==========================================

        self.user_answer = answer

        # ==========================================
        # 7. AMBIL MAPPING
        # ==========================================

        mapping = self.get_current_mapping()

        # ==========================================
        # 8. DECODE JAWABAN
        # ==========================================

        decoded = decode_letters_to_numbers(answer,mapping)

        # ==========================================
        # 9. CEK JAWABAN
        # ==========================================

        is_correct, mismatches = check_sequence(decoded,target)

        # ==========================================
        # 10. UPDATE SCORE
        # ==========================================

        if is_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        # ==========================================
        # 11. SIMPAN ATTEMPT HISTORY
        # ==========================================

        self.record_attempt(
            target=target,
            answer=answer,
            decoded=decoded,
            is_correct=is_correct,
            mismatches=mismatches,
        )

        # ==========================================
        # 12. GENERATE SOAL BARU
        # ==========================================

        self.generate_new_question()

        # ==========================================
        # 13. RETURN RESPONSE
        # ==========================================

        return {
            "correct": is_correct,
            "decoded": decoded,
            "expected": target,
            "mismatches": mismatches,
            "correct_answers": self.correct_answers,
            "incorrect_answers": self.incorrect_answers,
            "letters": self.letters.split(),
            "numbers": [int(number) for number in self.digits.split()],
            "target_numbers": [int(number) for number in self.target_numbers.split()],
        }



class decoding_information(Page):
    pass


class decoding_game(Page):
    @staticmethod
    def live_method(player, data):
        return {
            player.id_in_group: player.solve_answer(data)
        }

    @staticmethod
    def vars_for_template(player):
        player.start_decoding_task()
        letters_value = player.field_maybe_none("letters")

        if not letters_value:
            player.generate_new_question()

        letters = player.letters.split()
        numbers = [int(number) for number in player.digits.split()]
        target = [int(number) for number in player.target_numbers.split()]

        return dict(
            letters=letters,
            numbers=numbers,
            target_numbers=target,
            remaining_time=player.get_remaining_time(),
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.finish_decoding_task()


class decoding_results(Page):

    @staticmethod
    def vars_for_template(player):

        correct = player.correct_answers
        incorrect = player.incorrect_answers
        total_attempts = (correct + incorrect)

        if total_attempts > 0:
            accuracy = (correct / total_attempts * 100)

        else:
            accuracy = 0

        started_at = player.field_maybe_none("task_started_at")

        if started_at is not None:
            elapsed = (time.time() - started_at)
            elapsed = min(elapsed, Constants.decoding_time)

        else:
            elapsed = 0

        return dict(
            correct_answers=correct,
            incorrect_answers=incorrect,
            total_attempts=total_attempts,
            accuracy=accuracy,
            accuracy_formatted=f"{accuracy:.2f}",
            time_used=elapsed,
            time_used_formatted=format_seconds(elapsed),
            time_limit=Constants.decoding_time,
            time_limit_formatted=format_seconds(Constants.decoding_time),
            task_completed=player.task_completed,
        )


# page_sequence = [decoding_information, decoding_game, decoding_results]
page_sequence = [decoding_game, decoding_results]
