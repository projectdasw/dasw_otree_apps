from otree.api import *
import random

doc = """
Practice Session - 3 soal latihan (1 Risk, 1 Ambiguity, 1 Company)
Hasil tidak dihitung untuk pembayaran.
"""


class Constants(BaseConstants):
    name_in_url = 'me_practice'
    players_per_group = None
    num_rounds = 1

    # === Data soal latihan (diambil dari main task) ===

    # Risk Task: Ronde 1 (CR), EV A=3000, EV B=3000
    risk_data = dict(
        paradox='CR',
        a_outcomes=[(3000, 1.0)],
        b_outcomes=[(3750, 0.8), (0, 0.2)],
        ev_a=3000, ev_b=3000,
    )

    # Ambiguity Task: Ronde 1 (Ellsberg, single color)
    ambiguity_data = dict(
        procedure='ellsberg',
        choice_type='single',
        info_text='Terdapat 100 kotak di dalam tempat tertutup. 30 kotak berwarna Merah. '
                  'Sisanya berwarna Kuning dan Biru dengan komposisi yang tidak diketahui.',
    )
    ambiguity_payoff_win = 3000

    # Company Task: Ronde 1 (risk, Mid-Range)
    company_data = dict(
        round_type='risk', range_type='Mid-Range',
        capital=12000, investasi=2000, cc_inv=10000,
        ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=0.5,
        ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=0.2,
        damage_multiplier=20, prob_damage=0.05,
    )


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            # Generate komposisi bola untuk ambiguity me_practice (Ellsberg)
            yellow_e = random.randint(0, 70)
            blue_e = 70 - yellow_e
            player.amb_comp_red = 30
            player.amb_comp_yellow = yellow_e
            player.amb_comp_blue = blue_e


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- Risk Task Practice ---
    risk_prospek_terpilih = models.StringField(blank=True)
    risk_angka_keluar = models.IntegerField(initial=0)
    risk_hasil_token = models.IntegerField(initial=0)

    # --- Ambiguity Task Practice ---
    amb_prospek_terpilih = models.StringField(blank=True)
    amb_bola_keluar = models.StringField(blank=True)
    amb_hasil_token = models.IntegerField(initial=0)
    amb_comp_red = models.IntegerField(initial=0)
    amb_comp_yellow = models.IntegerField(initial=0)
    amb_comp_blue = models.IntegerField(initial=0)

    # --- Company Task Practice ---
    comp_prospek_terpilih = models.StringField(blank=True)
    comp_kontribusi_persen = models.IntegerField(min=0, max=100, initial=0)
    comp_angka_keluar = models.IntegerField(initial=0)
    comp_angka_damage = models.IntegerField(initial=0)
    comp_return_multiplier = models.FloatField(initial=0)
    comp_return_token = models.IntegerField(initial=0)
    comp_bencana_terjadi = models.BooleanField(initial=False)
    comp_kontribusi_token = models.IntegerField(initial=0)
    comp_hasil_token = models.IntegerField(initial=0)
