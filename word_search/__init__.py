from otree.api import *

doc = """
RET - Word Search
"""

class Constants(BaseConstants):
    name_in_url = "word_search"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
