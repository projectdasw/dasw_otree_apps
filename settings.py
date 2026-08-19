from os import environ

SESSION_CONFIGS = [
    # dict(
    #     display_name='donation_with_rank - Donation with rank',
    #     name='donation_with_rank',
    #     app_sequence=['donation_with_rank'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     display_name='investment - Investment Apps',
    #     name='investment',
    #     app_sequence=['investment'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     display_name='real_effort_task_algebraic - RET Algebraic',
    #     name='algebraic',
    #     app_sequence=['algebraic'],
    #     num_demo_participants=1,
    # ),
    dict(
        display_name='real_effort_task_decoding - RET Decoding',
        name='decoding',
        app_sequence=['decoding'],
        num_demo_participants=1,
    ),
    dict(
        display_name='real_effort_task_exact_transcription - RET Exact Transcription',
        name='transcription_exact',
        app_sequence=['transcription_exact'],
        num_demo_participants=1,
    ),
    # dict(
    #     display_name='real_effort_task_slot_machine - RET Slot Machine',
    #     name='slot_machine',
    #     app_sequence=['slot_machine'],
    #     num_demo_participants=1,
    # ),
    dict(
        display_name='real_effort_task_count_word - RET Count Word',
        name='count_word',
        app_sequence=['count_word'],
        num_demo_participants=1,
    ),
    # dict(
    #     display_name='shop_apps - Shopping Apps',
    #     name='shop_apps',
    #     app_sequence=['shop_apps'],
    #     num_demo_participants=1,
    # ),
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
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
    oTree DASW Apps
"""

SECRET_KEY = '6956438032015'
