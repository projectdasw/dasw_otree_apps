from .models import *


class moral_survey_page1(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

    def vars_for_template(self):
        return dict(
            questions=Constants.questions[:5],
            likert_values=[1, 2, 3, 4, 5, 6, 7],
            page_number=1,
            total_pages=2,
        )


class moral_survey_page2(Page):
    form_model = 'player'
    form_fields = ['q6', 'q7', 'q8', 'q9', 'q10', 'q11']

    def vars_for_template(self):
        questions_with_number = []
        for i, q in enumerate(Constants.questions[5:], start=6):
            questions_with_number.append(dict(**q, number=i))
        return dict(
            questions=questions_with_number,
            likert_values=[1, 2, 3, 4, 5, 6, 7],
            page_number=2,
            total_pages=2,
        )


page_sequence = [
    moral_survey_page1,
    moral_survey_page2,
]
