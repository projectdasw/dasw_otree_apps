from os import environ
SESSION_CONFIGS = [
    # Development Apps
    # Aktifkan ketika sedang dalam pembuatan/pengembangan aplikasi
    # Matikan ketika sedang dalam upload ke GitHub pembuatan/pengembangan aplikasi
    # ------------------------------------------------------------
    # dict(
    #     display_name='Development Apps',
    #     name='development_apps',
    #     app_sequence=[
    #         'me_instruction',
    #         'me_practice',
    #         'me_risk_task',
    #         'me_ambiguity_task',
    #         'me_company_task',
    #         'me_moral_survey',
    #         'me_survey_player',
    #         'me_payment_page'
    #     ],
    #     num_demo_participants=1,
    # ),

    # dict(
    #     display_name='apps_donation_with_rank - Donation with rank',
    #     name='apps_donation_with_rank',
    #     app_sequence=['apps_donation_with_rank'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     display_name='apps_investment - Investment Apps',
    #     name='apps_investment',
    #     app_sequence=['apps_investment'],
    #     num_demo_participants=1,
    # ),

    # Real Effort Task
    # ------------------------------------------------------------
    dict(
        display_name='RET Basic Algebraic',
        name='apps_algebraic',
        app_sequence=['apps_algebraic'],
        num_demo_participants=1,
    ),
    # dict(
    #     display_name='real_effort_task_decoding - RET Decoding',
    #     name='apps_decoding',
    #     app_sequence=['apps_decoding'],
    #     num_demo_participants=1,
    # ),
    dict(
        display_name='RET Continuous Transcription',
        name='apps_transcription_continuous',
        app_sequence=['apps_transcription_continuous'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET Count Word',
        name='apps_count_word',
        app_sequence=['apps_count_word'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET Exact Transcription',
        name='apps_transcription_exact',
        app_sequence=['apps_transcription_exact'],
        num_demo_participants=1,
    ),
    # dict(
    #     display_name='real_effort_task_slot_machine - RET Slot Machine',
    #     name='apps_slot_machine',
    #     app_sequence=['apps_slot_machine'],
    #     num_demo_participants=1,
    # ),
    # ------------------------------------------------------------

    # Shopping Simulation
    # ------------------------------------------------------------
    dict(
        display_name='Shopping Apps',
        name='apps_shop_apps',
        app_sequence=['apps_shop_apps'],
        num_demo_participants=1,
    ),
    # ------------------------------------------------------------

    # Research Experiment
    # ------------------------------------------------------------
    dict(
        display_name='Poor Assistance',
        name='poor_assistance',
        app_sequence=[
            'pa_welcome',
            'pa_risky_investment_purchase_practice',
            'pa_risky_investment_purchase',
            'pa_risky_investment_allocation_practice',
            'pa_risky_investment_allocation',
            'pa_decoding_practice',
            'pa_decoding',
            'pa_investment_panel_allocation_practice',
            'pa_investment_panel_allocation',
            'pa_survey',
            'pa_payment',
        ],
        num_demo_participants=1,
    ),
    dict(
        display_name='Moral Environments',
        name='moral_environments',
        app_sequence=[
            'me_instruction',
            'me_practice',
            'me_risk_task',
            'me_ambiguity_task',
            'me_company_task',
            'me_moral_survey',
            'me_survey_player',
            'me_payment_page'
        ],
        num_demo_participants=1,
    ),
    dict(
        display_name='Donation',
        name='donation',
        app_sequence=['maintenance_page'],
        num_demo_participants=1,
    ),
    dict(
        display_name='Digital Payment',
        name='digital_payment',
        app_sequence=['maintenance_page'],
        num_demo_participants=1,
    ),
    dict(
        display_name='Tax Evasion',
        name='tax_evasion',
        app_sequence=['maintenance_page'],
        num_demo_participants=1,
    ),
    dict(
        display_name='Alabama Project',
        name='alabama_project',
        app_sequence=['maintenance_page'],
        num_demo_participants=1,
    ),
    # ------------------------------------------------------------

    # Templates Custom Style
    # ------------------------------------------------------------
    dict(
        display_name='Custom Templates',
        name='templates_style',
        app_sequence=['templates_style'],
        num_demo_participants=1,
    ),
    # dict(
    #     display_name='Maintenance Page',
    #     name='maintenance_page',
    #     app_sequence=['maintenance_page'],
    #     num_demo_participants=1,
    # ),
    # ------------------------------------------------------------
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
DEBUG = True

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False

ADMIN_USERNAME = 'projectdasw'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """"""

SECRET_KEY = '6956438032015'
