from .models import *
from .utils import (generate_decoding_pairs, build_mapping, generate_target_numbers, decode_letters_to_numbers,
                    check_sequence)


class Info(Page):
    pass


class App(Page):
    def vars_for_template(self):
        letters, numbers = generate_decoding_pairs()

        # simpan mapping alphabet → angka
        self.player.letters = ' '.join(letters)
        self.player.digits = ' '.join(str(n) for n in numbers)

        # generate 5 angka target
        target = generate_target_numbers(numbers, count=5)

        # simpan juga agar konsisten di refresh
        self.player.target_numbers = ' '.join(str(n) for n in target)

        return dict(
            letters=letters,
            numbers=numbers,
            target_numbers=target,
        )

    def js_vars(self):
        # kirim mapping ke JavaScript
        letters = self.player.letters.split()
        numbers = [int(x) for x in self.player.digits.split()]
        mapping = build_mapping(letters, numbers)
        reverse_mapping = {v: k for k, v in mapping.items()}

        target_numbers = [int(x) for x in self.player.target_numbers.split()]

        return dict(
            mapping=mapping,
            reverse_mapping=reverse_mapping,
            target_numbers=target_numbers,
        )


class Results(Page):
    pass


page_sequence = [Info, App, Results]
