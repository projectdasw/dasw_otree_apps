from otree.api import *

doc = """
Survey Player (Biodata) - Moral Environment
Data demografi dan informasi pembayaran responden
"""


class Constants(BaseConstants):
    name_in_url = 'me_survey_player'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    usia = models.IntegerField(
        label='Usia',
        min=18, max=80,
    )
    jenis_kelamin = models.StringField(
        label='Jenis Kelamin',
        choices=[
            ['Laki-laki', 'Laki-laki'],
            ['Perempuan', 'Perempuan'],
        ],
        widget=widgets.RadioSelect,
    )
    jenjang_pendidikan = models.StringField(
        label='Jenjang pendidikan yang sedang/terakhir ditempuh',
        choices=[
            ['SMA/SMK/MA', 'SMA / SMK / MA'],
            ['D1', 'D1 (Diploma 1)'],
            ['D2', 'D2 (Diploma 2)'],
            ['D3', 'D3 (Diploma 3)'],
            ['D4/S1', 'D4 / S1 (Sarjana)'],
            ['S2', 'S2 (Magister)'],
            ['S3', 'S3 (Doktor)'],
        ],
    )
    bidang_studi = models.StringField(
        label='Bidang Studi',
    )
    pengeluaran = models.StringField(
        label='Pengeluaran rata-rata sebulan',
        choices=[
            ['< Rp500.000', 'Kurang dari Rp500.000'],
            ['Rp500.000 - Rp1.000.000', 'Rp500.000 - Rp1.000.000'],
            ['Rp1.000.001 - Rp1.500.000', 'Rp1.000.001 - Rp1.500.000'],
            ['Rp1.500.001 - Rp2.000.000', 'Rp1.500.001 - Rp2.000.000'],
            ['Rp2.000.001 - Rp3.000.000', 'Rp2.000.001 - Rp3.000.000'],
            ['Rp3.000.001 - Rp5.000.000', 'Rp3.000.001 - Rp5.000.000'],
            ['> Rp5.000.000', 'Lebih dari Rp5.000.000'],
        ],
    )
    platform_pembayaran = models.StringField(
        label='Platform untuk pembayaran',
        choices=[
            ['GoPay', 'GoPay'],
            ['OVO', 'OVO'],
            ['Dana', 'Dana'],
            ['ShopeePay', 'ShopeePay'],
            ['LinkAja', 'LinkAja'],
            ['BNI', 'Bank BNI'],
            ['Mandiri', 'Bank Mandiri'],
            ['CIMB Niaga', 'Bank CIMB Niaga'],
        ],
    )
    nomor_pembayaran = models.StringField(
        label='Nomor HP/Rekening/Online Payment untuk pembayaran',
    )
