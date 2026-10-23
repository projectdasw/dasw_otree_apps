from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'pa_welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Loading(WaitPage):
    title_text = "Ruang Tunggu Eksperimen"


class welcome(Page):
    pass


class general_instruction(Page):
    pass


class risky_investment_purchase_instruction(Page):
    pass


class risky_investment_allocation_instruction(Page):
    pass


class real_effort_decoding_instruction(Page):
    pass


class investment_panel_allocation_instruction(Page):
    pass


class confirmation(Page):
    pass


page_sequence = [
    welcome,
    general_instruction,
    risky_investment_purchase_instruction,
    risky_investment_allocation_instruction,
    real_effort_decoding_instruction,
    investment_panel_allocation_instruction,
    confirmation,
    Loading
]
