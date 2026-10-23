from otree.api import *

doc = """
Payment Page - Moral Environment
"""


class Constants(BaseConstants):
    name_in_url = 'me_payment_page'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    chosen_risk_round = models.IntegerField(blank=True)
    chosen_ambiguity_round = models.IntegerField(blank=True)
    chosen_company_return_round = models.IntegerField(blank=True)
    chosen_company_cap_round = models.IntegerField(blank=True)
    risk_payoff = models.IntegerField(blank=True)
    ambiguity_payoff = models.IntegerField(blank=True)
    company_return_payoff = models.IntegerField(blank=True)
    company_cap_payoff = models.IntegerField(blank=True)
    company_payoff = models.IntegerField(blank=True)
    total_token = models.IntegerField(blank=True)
    total_payment = models.IntegerField(blank=True)
