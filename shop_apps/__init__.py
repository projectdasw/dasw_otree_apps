from otree.api import *

doc = """
Shop Apps
"""

class Constants(BaseConstants):
    name_in_url = "shop_apps"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


page_sequence = []
