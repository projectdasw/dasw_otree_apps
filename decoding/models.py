from otree.api import *

doc = """
RET - Decoding Task
"""


class Constants(BaseConstants):
    name_in_url = 'decoding'
    players_per_group = None
    num_rounds = 1
    total_items = 9


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    digits = models.StringField()
    letters = models.StringField()
    target_numbers = models.StringField()
