from otree.api import *

doc = """
Welcome to Moral Environment Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'me_instruction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
