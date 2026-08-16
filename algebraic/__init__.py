from otree.api import *
from otree.assets.app_template import page_sequence

doc = """
RET - Algebraic
"""

class Constants(BaseConstants):
    name_in_url = "algebraic"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
