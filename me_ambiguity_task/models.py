from otree.api import *
import random

doc = """
Ambiguity Task - Moral Environment
Ellsberg Paradox & Partial Uncertainty
5 ronde: 2 Ellsberg, 2 Partial, 1 Full Unknown
"""


class Constants(BaseConstants):
    name_in_url = 'me_ambiguity_task'
    players_per_group = None
    num_rounds = 5
    payoff_win = 3000

    rounds_data = [
        # Ronde 1 (Ellsberg): Pilih satu warna
        dict(
            procedure='ellsberg',
            choice_type='single',
            info_text='Terdapat 100 kotak di dalam tempat tertutup. 30 kotak berwarna Merah. '
                      'Sisanya berwarna Kuning dan Biru dengan komposisi yang tidak diketahui.',
        ),
        # Ronde 2 (Ellsberg): Pilih kombinasi warna
        dict(
            procedure='ellsberg',
            choice_type='combination',
            info_text='Terdapat 100 kotak di dalam tempat tertutup. 30 kotak berwarna Merah. '
                      'Sisanya berwarna Kuning dan Biru dengan komposisi yang tidak diketahui.',
        ),
        # Ronde 3 (Partial Uncertainty): Pilih satu warna
        dict(
            procedure='partial',
            choice_type='single',
            info_text='Terdapat 100 kotak di dalam tempat tertutup. Masing-masing warna '
                      '(Merah, Kuning, Biru) memiliki minimal 10 kotak. '
                      'Sisa 70 kotak tidak diketahui komposisinya.',
        ),
        # Ronde 4 (Partial Uncertainty): Pilih kombinasi warna
        dict(
            procedure='partial',
            choice_type='combination',
            info_text='Terdapat 100 kotak di dalam tempat tertutup. Masing-masing warna '
                      '(Merah, Kuning, Biru) memiliki minimal 10 kotak. '
                      'Sisa 70 kotak tidak diketahui komposisinya.',
        ),
        # Ronde 5 (Full Unknown): Pilih satu warna
        dict(
            procedure='unknown',
            choice_type='single',
            info_text='Terdapat 100 kotak berwarna Merah, Kuning, dan Biru di dalam tempat tertutup. '
                      'Komposisi warna kotak tidak diketahui.',
        ),
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                # --- Ellsberg (ronde 1-2): Red=30, Yellow+Blue=70 ---
                yellow_e = random.randint(0, 70)
                blue_e = 70 - yellow_e
                for r in [1, 2]:
                    p = player.in_round(r)
                    p.comp_red = 30
                    p.comp_yellow = yellow_e
                    p.comp_blue = blue_e

                # --- Partial (ronde 3-4): min 10 tiap warna, sisa 70 random ---
                remaining = 70
                add_red = random.randint(0, remaining)
                remaining -= add_red
                add_yellow = random.randint(0, remaining)
                add_blue = remaining - add_yellow
                for r in [3, 4]:
                    p = player.in_round(r)
                    p.comp_red = 10 + add_red
                    p.comp_yellow = 10 + add_yellow
                    p.comp_blue = 10 + add_blue

                # --- Full Unknown (ronde 5): minimal 1 tiap warna ---
                r5_red = random.randint(1, 98)
                r5_remaining = 100 - r5_red
                r5_yellow = random.randint(1, r5_remaining - 1)
                r5_blue = r5_remaining - r5_yellow
                p5 = player.in_round(5)
                p5.comp_red = r5_red
                p5.comp_yellow = r5_yellow
                p5.comp_blue = r5_blue


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prospek_terpilih = models.StringField()
    bola_keluar = models.StringField()
    hasil_token = models.IntegerField(initial=0)
    # Komposisi sebenarnya (di-generate saat session dibuat)
    comp_red = models.IntegerField(initial=0)
    comp_yellow = models.IntegerField(initial=0)
    comp_blue = models.IntegerField(initial=0)
