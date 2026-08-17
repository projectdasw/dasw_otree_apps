import random
import string


def generate_decoding_pairs(total_items=9):
    """
    Menghasilkan pasangan huruf dan angka secara acak.

    Contoh:
        letters = ['A', 'Q', 'M', ...]
        numbers = [7, 2, 9, ...]

    Setiap huruf dan angka hanya muncul satu kali.
    """

    letters = random.sample(
        string.ascii_uppercase,
        total_items,
    )

    numbers = random.sample(
        range(1, total_items + 1),
        total_items,
    )

    return letters, numbers

def generate_target_numbers(numbers, count=5):
    """
    Menghasilkan angka target secara acak.

    Angka dapat muncul lebih dari satu kali.
    """

    if not numbers:
        raise ValueError(
            "numbers cannot be empty"
        )

    if count <= 0:
        raise ValueError(
            "count must be greater than 0"
        )

    return random.choices(
        numbers,
        k=count,
    )

def build_mapping(letters, numbers):
    """
    Membuat mapping:

        huruf -> angka

    Contoh:

        A -> 7
        B -> 2
        C -> 9
    """

    if isinstance(letters, str):
        letters = letters.split()

    if isinstance(numbers, str):
        numbers = numbers.replace(",", " ").split()
        numbers = [
            int(number)
            for number in numbers
        ]

    letters = list(letters)
    numbers = list(numbers)

    if len(letters) != len(numbers):
        raise ValueError(
            "letters and numbers must have the same length"
        )

    return dict(
        zip(
            letters,
            numbers,
        )
    )

def decode_letters_to_numbers(answer_letters, mapping):
    """
    Mengubah jawaban huruf menjadi angka.

    Contoh:

        answer = "ABCDE"

        mapping = {
            "A": 7,
            "B": 2,
            "C": 9,
            "D": 4,
            "E": 1,
        }

        result = [7, 2, 9, 4, 1]
    """

    if not isinstance(answer_letters, str):
        answer_letters = "".join(answer_letters)

    answer_letters = (
        answer_letters
        .replace(" ", "")
        .upper()
    )

    return [
        mapping.get(letter)
        for letter in answer_letters
    ]

def check_sequence(decoded_list, correct_numbers):
    """
    Membandingkan hasil decoding dengan target.

    Return:

        (
            is_correct,
            mismatches
        )

    mismatches:

        [
            (position, expected, got)
        ]
    """

    if isinstance(correct_numbers, str):
        correct_numbers = (
            correct_numbers
            .replace(",", " ")
            .split()
        )

        correct_numbers = [
            int(number)
            for number in correct_numbers
        ]

    decoded_list = list(decoded_list)
    correct_numbers = list(correct_numbers)

    mismatches = []

    max_length = max(
        len(decoded_list),
        len(correct_numbers),
    )

    for index in range(max_length):

        expected = (
            correct_numbers[index]
            if index < len(correct_numbers)
            else None
        )

        got = (
            decoded_list[index]
            if index < len(decoded_list)
            else None
        )

        if expected != got:
            mismatches.append(
                (
                    index,
                    expected,
                    got,
                )
            )

    is_correct = not mismatches

    return (
        is_correct,
        mismatches,
    )

def validate_answer(answer, expected_count):
    """
    Validasi jawaban peserta.

    Return:
        valid: bool
        normalized_answer: str
        error: str | None
    """

    if not isinstance(answer, str):
        return False, "", "Invalid answer."

    answer = answer.strip().upper()

    # Kosong
    if not answer:
        return False, "", "Please enter your answer."

    # Hilangkan whitespace
    answer = "".join(answer.split())

    # Harus berisi huruf A-Z saja
    if not answer.isalpha():
        return False, "", "Please enter letters only."

    # Pastikan ASCII A-Z
    if not all(
        "A" <= char <= "Z"
        for char in answer
    ):
        return False, "", "Please enter letters only."

    # Jumlah huruf
    if len(answer) != expected_count:
        return (
            False,
            "",
            f"Please enter exactly {expected_count} letters."
        )

    # Normalisasi menjadi format backend
    normalized_answer = " ".join(answer)

    return True, normalized_answer, None