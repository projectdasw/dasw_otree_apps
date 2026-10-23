from otree.api import *

doc = """
Maintenance Page
"""

class Constants(BaseConstants):
    name_in_url = "maintenance_page"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class page(Page):
    pass


page_sequence = [page]
