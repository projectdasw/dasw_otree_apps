from otree.api import *


class welcome(Page):
    pass


class instruction(Page):
    pass


class risk_task_example(Page):
    pass


class ambiguity_task_example(Page):
    pass


class company_task_example(Page):
    def vars_for_template(self):
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )
        return dict(treatment=treatment)


class practice_session(Page):
    pass


page_sequence = [
    welcome,
    instruction,
    risk_task_example,
    ambiguity_task_example,
    company_task_example,
    practice_session,
]
