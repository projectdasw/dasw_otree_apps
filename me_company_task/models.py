from otree.api import *
import random

doc = """
Company Task - Moral Environment
20 ronde: 10 Risk (prob diketahui) + 10 Ambiguity (prob minimal)
Treatment: By Return atau By Capitalisation (ditentukan di session config)
hasil_token = cc_inv + return_token - kontribusi_token
kontribusi_token dihitung dari return (by_return) atau kapitalisasi (by_capitalisation),
dan selalu mengurangi hasil akhir
"""


class Constants(BaseConstants):
    name_in_url = 'me_company_task'
    players_per_group = None
    num_rounds = 20

    # ============================
    # RONDE 1-10: RISK (prob pasti)
    # ============================
    # Format return: multiplier (2 = 200%, 1.25 = 125%, dst)
    # Format prob: desimal (0.5 = 50%)
    # Damage: 20x investasi, prob 5%
    rounds_data = [
        # --- Mid-Range (R1-R3): Capital=12000, Invest=2000, CC-Inv=10000 ---
        dict(
            round_type='risk', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=0.5,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=0.2,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=0.75,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=0.6,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=0.8,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=0.7,
            damage_multiplier=20, prob_damage=0.05,
        ),
        # --- Narrow-Range (R4-R6): Capital=8000, Invest=3000, CC-Inv=5000 ---
        dict(
            round_type='risk', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=0.5,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=0.2,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=0.75,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=0.6,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=0.8,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=0.7,
            damage_multiplier=20, prob_damage=0.05,
        ),
        # --- Wide-Range (R7-R10): Capital=16000, Invest=1000, CC-Inv=15000 ---
        dict(
            round_type='risk', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=0.5,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=0.2,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=0.75,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=0.6,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=0.8,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=0.7,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='risk', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=5.55, prob_a1=0.15, ret_a2=0.2, prob_a2=0.85,
            ret_b1=4.2, prob_b1=0.2, ret_b2=0.2, prob_b2=0.8,
            damage_multiplier=20, prob_damage=0.05,
        ),

        # ============================
        # RONDE 11-20: AMBIGUITY (prob minimal)
        # ============================
        # prob_a1, prob_b1 = minimum probability (aktual di-generate >= minimum)
        # prob_damage = maximum damage probability (aktual di-generate <= max)

        # --- Mid-Range (R11-R13) ---
        dict(
            round_type='ambiguity', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=None,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=None,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Mid-Range',
            capital=12000, investasi=2000, cc_inv=10000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=None,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        # --- Narrow-Range (R14-R16) ---
        dict(
            round_type='ambiguity', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=None,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=None,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Narrow-Range',
            capital=8000, investasi=3000, cc_inv=5000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=None,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        # --- Wide-Range (R17-R20) ---
        dict(
            round_type='ambiguity', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=2, prob_a1=0.5, ret_a2=0, prob_a2=None,
            ret_b1=1.25, prob_b1=0.8, ret_b2=0, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=2.8, prob_a1=0.25, ret_a2=0.4, prob_a2=None,
            ret_b1=2.35, prob_b1=0.4, ret_b2=0.1, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=4, prob_a1=0.2, ret_a2=0.25, prob_a2=None,
            ret_b1=3, prob_b1=0.3, ret_b2=0.15, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
        dict(
            round_type='ambiguity', range_type='Wide-Range',
            capital=16000, investasi=1000, cc_inv=15000,
            ret_a1=5.55, prob_a1=0.15, ret_a2=0.2, prob_a2=None,
            ret_b1=4.2, prob_b1=0.2, ret_b2=0.2, prob_b2=None,
            damage_multiplier=20, prob_damage=0.05,
        ),
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        """Assign balanced random treatment + generate ambiguity probabilities."""
        if self.round_number == 1:
            players = self.get_players()

            # --- Balanced random treatment assignment ---
            # Only assign to participants who don't have a treatment yet
            # (single-treatment sessions set treatment via session config, skip these)
            unassigned = [
                p for p in players
                if 'treatment' not in p.participant.vars
                and 'treatment' not in self.session.config
            ]
            if unassigned:
                n = len(unassigned)
                half = n // 2
                treatments = ['by_return'] * half + ['by_capitalisation'] * (n - half)
                random.shuffle(treatments)
                for player, t in zip(unassigned, treatments):
                    player.participant.vars['treatment'] = t

            # --- Generate ambiguity probabilities for rounds 11-20 ---
            for player in players:
                for r in range(11, 21):
                    p = player.in_round(r)
                    rd = Constants.rounds_data[r - 1]

                    min_a1 = rd['prob_a1']
                    actual_a1 = min_a1 + random.random() * (1 - min_a1)
                    p.actual_prob_a1 = round(actual_a1, 4)
                    p.actual_prob_a2 = round(1 - actual_a1, 4)

                    min_b1 = rd['prob_b1']
                    actual_b1 = min_b1 + random.random() * (1 - min_b1)
                    p.actual_prob_b1 = round(actual_b1, 4)
                    p.actual_prob_b2 = round(1 - actual_b1, 4)

                    p.actual_prob_damage = round(random.random() * rd['prob_damage'], 4)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Treatment assignment (by_return atau by_capitalisation)
    treatment = models.StringField(initial='')

    # Pilihan pemain
    prospek_terpilih = models.StringField()
    kontribusi_persen = models.IntegerField(min=0, max=100)

    # Hasil random
    angka_keluar = models.IntegerField(initial=0)       # 1-100 untuk return
    angka_damage = models.IntegerField(initial=0)        # 1-10000 untuk damage

    # Hasil kalkulasi
    return_multiplier = models.FloatField(initial=0)     # multiplier yang terpilih
    return_token = models.IntegerField(initial=0)        # return dalam token
    bencana_terjadi = models.BooleanField(initial=False)
    kontribusi_token = models.IntegerField(initial=0)    # kontribusi dalam token
    hasil_token = models.IntegerField(initial=0)         # hasil akhir

    # Probabilitas aktual (untuk ronde ambiguity 11-20)
    actual_prob_a1 = models.FloatField(initial=0)
    actual_prob_a2 = models.FloatField(initial=0)
    actual_prob_b1 = models.FloatField(initial=0)
    actual_prob_b2 = models.FloatField(initial=0)
    actual_prob_damage = models.FloatField(initial=0)
