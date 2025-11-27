import random
import string
from .models import Constants


def generate_decoding_pairs():
    """
    Menghasilkan acakan Constants.total_items huruf dan angka.
    Huruf berupa list of uppercase letters,
    Angka berupa list of ints (1..9).
    """
    letters = random.sample(string.ascii_uppercase, Constants.total_items)
    numbers = random.sample(range(1, 10), Constants.total_items)
    return letters, numbers


def generate_target_numbers(numbers, count=5):
    """
    Menghasilkan angka target acak dari daftar numbers.
    Bisa duplikat (karena decoding biasanya boleh).
    """
    return random.choices(numbers, k=count)


def build_mapping(letters, numbers):
    """
    Buat mapping huruf -> angka.

    - letters: list of str (['A','B',...]) atau str "A B C ..."
    - numbers: list of int ([7,2,...]) atau str "7 2 3 ..."

    Return: dict, contoh {'A': 7, 'B': 2, ...}
    """
    # normalize letters
    if isinstance(letters, str):
        letters_list = letters.split()
    else:
        letters_list = list(letters)

    # normalize numbers
    if isinstance(numbers, str):
        # handle possible commas or spaces
        numbers_list = [int(x) for x in numbers.replace(',', ' ').split()]
    else:
        numbers_list = list(numbers)

    if len(letters_list) != len(numbers_list):
        raise ValueError("letters and numbers must have the same length")

    return {letters_list[i]: numbers_list[i] for i in range(len(letters_list))}


def decode_letters_to_numbers(answer_letters, mapping):
    """
    Ubah jawaban peserta (huruf) menjadi angka berdasarkan mapping.
    - answer_letters: str "A B C ..." atau list ['A','B','C']
    - mapping: {'A':7, ...}

    Return: list of ints or None (jika huruf tidak ada di mapping)
    """
    if isinstance(answer_letters, str):
        answer_list = answer_letters.split()
    else:
        answer_list = list(answer_letters)

    decoded = [mapping.get(letter, None) for letter in answer_list]
    return decoded


def check_sequence(decoded_list, correct_numbers):
    """
    Bandingkan decoded_list (list angka/None) dengan correct_numbers (list int).
    Mengembalikan tuple (is_correct_bool, mismatches)
    - mismatches = list of tuples (pos, expected, got) untuk posisi yang salah
    """
    # normalize correct_numbers if string
    if isinstance(correct_numbers, str):
        correct = [int(x) for x in correct_numbers.replace(',', ' ').split()]
    else:
        correct = list(correct_numbers)

    mismatches = []
    # if lengths differ, it's considered incorrect but we still compare up to min len
    min_len = min(len(decoded_list), len(correct))
    for i in range(min_len):
        if decoded_list[i] != correct[i]:
            mismatches.append((i, correct[i], decoded_list[i]))

    # extra length mismatches
    if len(decoded_list) != len(correct):
        # mark remaining as mismatches
        longer = max(len(decoded_list), len(correct))
        for i in range(min_len, longer):
            exp = correct[i] if i < len(correct) else None
            got = decoded_list[i] if i < len(decoded_list) else None
            mismatches.append((i, exp, got))

    is_correct = len(mismatches) == 0
    return is_correct, mismatches
