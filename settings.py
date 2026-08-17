from os import environ

SESSION_CONFIGS = [
    dict(
        display_name='Donation w/ Rank',
        name='donation_with_rank',
        app_sequence=['donation_with_rank'],
        num_demo_participants=1,
    ),
    dict(
        display_name='Investment Apps',
        name='investment',
        app_sequence=['investment'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET - Algebraic',
        name='algebraic',
        app_sequence=['algebraic'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET - Decoding',
        name='decoding',
        app_sequence=['decoding'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET - Transcription',
        name='transcription',
        app_sequence=['transcription'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET - Slot Machine',
        name='slot_machine',
        app_sequence=['slot_machine'],
        num_demo_participants=1,
    ),
    dict(
        display_name='RET - Word Search',
        name='word_search',
        app_sequence=['word_search'],
        num_demo_participants=1,
    ),
    dict(
        display_name='Shop Apps',
        name='shop_apps',
        app_sequence=['shop_apps'],
        num_demo_participants=1,
    ),
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
