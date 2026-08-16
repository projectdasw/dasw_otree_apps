from otree.api import *

doc = """
RET - Slot Machine
"""

class Constants(BaseConstants):
    name_in_url = "slot_machine"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
