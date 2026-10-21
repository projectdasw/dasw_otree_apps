from otree.api import *

doc = """
Custom Templates
"""

class Constants(BaseConstants):
    name_in_url = "templates_style"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# class Loading(WaitPage):
#     title_text = "Please wait" # use {% title_text %} on HTML for display Wait Page title text


class wait_pages_templates(Page):
    pass


class introduction_templates(Page):
    pass


class instruction_templates(Page):
    pass


class confirmation_templates(Page):
    pass


class game_templates(Page):
    pass


class single_results_templates(Page):
    pass


class final_results_templates(Page):
    pass


page_sequence = [
    # Loading,
    wait_pages_templates,
    introduction_templates,
    instruction_templates,
    confirmation_templates,
    game_templates,
    single_results_templates,
    final_results_templates,
]
