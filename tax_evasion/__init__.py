from otree.api import *


doc = """
Tax Evasion
"""


class C(BaseConstants):
    NAME_IN_URL = 'tax_evasion'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
