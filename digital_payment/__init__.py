from otree.api import *


doc = """
Digital Payment
"""


class C(BaseConstants):
    NAME_IN_URL = 'digital_payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
