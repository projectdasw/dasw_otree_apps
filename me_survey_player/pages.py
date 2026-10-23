from .models import *


class survey_page(Page):
    form_model = 'player'
    form_fields = [
        'usia',
        'jenis_kelamin',
        'jenjang_pendidikan',
        'bidang_studi',
        'pengeluaran',
        'platform_pembayaran',
        'nomor_pembayaran',
    ]


page_sequence = [
    survey_page,
]
