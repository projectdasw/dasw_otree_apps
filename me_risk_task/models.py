from otree.api import *

doc = """
Risk Task - Moral Environment
Allais Paradox: Common Ratio (CR) dan Common Consequence (CC)
"""


class Constants(BaseConstants):
    name_in_url = 'me_risk_task'
    players_per_group = None
    num_rounds = 5

    # Parameter per ronde dari CSV
    # Format: (payoff, probabilitas) — probabilitas dalam desimal
    # Outcome dengan p=0 tidak ditampilkan tapi tetap ada untuk kalkulasi
    rounds_data = [
        # Ronde 1 (CR): EV A=3000, EV B=3000
        dict(
            paradox='CR',
            a_outcomes=[(3000, 1.0)],
            b_outcomes=[(3750, 0.8), (0, 0.2)],
            ev_a=3000, ev_b=3000,
        ),
        # Ronde 2 (CR): EV A=750, EV B=750
        dict(
            paradox='CR',
            a_outcomes=[(3000, 0.25), (0, 0.75)],
            b_outcomes=[(3750, 0.2), (0, 0.8)],
            ev_a=750, ev_b=750,
        ),
        # Ronde 3 (CC): EV A=3000, EV B=3050
        dict(
            paradox='CC',
            a_outcomes=[(3000, 1.0)],
            b_outcomes=[(3000, 0.85), (5000, 0.1), (0, 0.05)],
            ev_a=3000, ev_b=3050,
        ),
        # Ronde 4 (CC): EV A=1500, EV B=1550
        dict(
            paradox='CC',
            a_outcomes=[(3000, 0.5), (0, 0.5)],
            b_outcomes=[(3000, 0.35), (5000, 0.1), (0, 0.55)],
            ev_a=1500, ev_b=1550,
        ),
        # Ronde 5 (CC): EV A=450, EV B=500
        dict(
            paradox='CC',
            a_outcomes=[(3000, 0.15), (0, 0.85)],
            b_outcomes=[(5000, 0.1), (0, 0.9)],
            ev_a=450, ev_b=500,
        ),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prospek_terpilih = models.StringField()
    angka_keluar = models.IntegerField(initial=0)
    hasil_token = models.IntegerField(initial=0)
