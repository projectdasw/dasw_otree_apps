from otree.api import *

doc = """
Donation w/ Rank
"""

class Constants(BaseConstants):
    name_in_url = "donation_with_rank"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
