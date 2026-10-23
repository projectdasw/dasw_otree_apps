from otree.api import *

doc = """
Moral Survey - Moral Preference toward Environment
Anthropocentric (Q1-Q5) dan Ecocentric (Q6-Q11) orientation
Skala Likert 1-7
"""

LIKERT_CHOICES = [
    [1, '1'],
    [2, '2'],
    [3, '3'],
    [4, '4'],
    [5, '5'],
    [6, '6'],
    [7, '7'],
]


class Constants(BaseConstants):
    name_in_url = 'me_moral_survey'
    players_per_group = None
    num_rounds = 1

    questions = [
        # Anthropocentric (Q1-Q5)
        dict(
            field='q1',
            text='Lingkungan perlu dilindungi mengingat peran pentingnya dalam memberikan benefit bagi umat manusia',
            category='anthropocentric',
        ),
        dict(
            field='q2',
            text='Nilai-nilai ekologis akan muncul ketika alam menyediakan segala kebutuhan bagi manusia',
            category='anthropocentric',
        ),
        dict(
            field='q3',
            text='Kebutuhan manusia menjadi prioritas utama dibandingkan perhatian pada perlindungan terhadap lingkungan',
            category='anthropocentric',
        ),
        dict(
            field='q4',
            text='Umat manusia harus terus melindungi lingkungan karena lingkungan menyediakan segala kebutuhan manusia',
            category='anthropocentric',
        ),
        dict(
            field='q5',
            text='Kebijakan terhadap lingkungan harus berdasarkan pada apa yang terbaik bagi umat manusia',
            category='anthropocentric',
        ),
        # Ecocentric (Q6-Q11)
        dict(
            field='q6',
            text='Alam memiliki nilai-nilainya sendiri terlepas dari kemanfaatannya bagi umat manusia',
            category='ecocentric',
        ),
        dict(
            field='q7',
            text='Seluruh makhluk hidup memiliki hak asasi untuk tetap eksis di dunia',
            category='ecocentric',
        ),
        dict(
            field='q8',
            text='Manusia bukanlah spesies paling penting dibandingkan spesies lain di dunia ini',
            category='ecocentric',
        ),
        dict(
            field='q9',
            text='Alam berhak untuk memiliki konsiderasi moral tersendiri yang terpisah dari kepentingan umat manusia',
            category='ecocentric',
        ),
        dict(
            field='q10',
            text='Umat manusia memiliki kewajiban moral terhadap alam yang lebih besar daripada urusan dampak bencana alam terhadap manusia',
            category='ecocentric',
        ),
        dict(
            field='q11',
            text='Ekosistem lingkungan memiliki nilai moral intrinsiknya sendiri',
            category='ecocentric',
        ),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Anthropocentric (Q1-Q5)
    q1 = models.IntegerField(
        label='Lingkungan perlu dilindungi mengingat peran pentingnya dalam memberikan benefit bagi umat manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q2 = models.IntegerField(
        label='Nilai-nilai ekologis akan muncul ketika alam menyediakan segala kebutuhan bagi manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q3 = models.IntegerField(
        label='Kebutuhan manusia menjadi prioritas utama dibandingkan perhatian pada perlindungan terhadap lingkungan',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q4 = models.IntegerField(
        label='Umat manusia harus terus melindungi lingkungan karena lingkungan menyediakan segala kebutuhan manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q5 = models.IntegerField(
        label='Kebijakan terhadap lingkungan harus berdasarkan pada apa yang terbaik bagi umat manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    # Ecocentric (Q6-Q11)
    q6 = models.IntegerField(
        label='Alam memiliki nilai-nilainya sendiri terlepas dari kemanfaatannya bagi umat manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q7 = models.IntegerField(
        label='Seluruh makhluk hidup memiliki hak asasi untuk tetap eksis di dunia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q8 = models.IntegerField(
        label='Manusia bukanlah spesies paling penting dibandingkan spesies lain di dunia ini',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q9 = models.IntegerField(
        label='Alam berhak untuk memiliki konsiderasi moral tersendiri yang terpisah dari kepentingan umat manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q10 = models.IntegerField(
        label='Umat manusia memiliki kewajiban moral terhadap alam yang lebih besar daripada urusan dampak bencana alam terhadap manusia',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
    q11 = models.IntegerField(
        label='Ekosistem lingkungan memiliki nilai moral intrinsiknya sendiri',
        choices=LIKERT_CHOICES, widget=widgets.RadioSelectHorizontal,
    )
