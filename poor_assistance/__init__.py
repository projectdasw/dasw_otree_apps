from otree.api import *


doc = """
Poor Assistance
"""


class C(BaseConstants):
    NAME_IN_URL = 'poor_assistance'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
