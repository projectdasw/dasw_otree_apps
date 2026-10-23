from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'pa_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Define form fields based on the questions
    q1 = models.StringField(
        label="Saya selalu bisa menyelesaikan masalah sulit jika saya berusaha cukup keras.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q2 = models.StringField(
        label="Jika seseorang menentang saya, saya dapat menemukan cara dan sarana untuk mendapatkan apa yang saya"
              " inginkan.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q3 = models.StringField(
        label="Saya yakin bahwa saya dapat mencapai tujuan saya.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q4 = models.StringField(
        label="Saya yakin bahwa saya dapat menangani kejadian tak terduga dengan efisien.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q5 = models.StringField(
        label="Berkat kemampuan saya dalam mengatasi berbagai situasi, saya bisa menangani keadaan yang tak terduga.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q6 = models.StringField(
        label="Saya bisa menyelesaikan sebagian besar masalah jika saya mengerahkan upaya yang diperlukan.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q7 = models.StringField(
        label="Saya bisa tetap tenang saat menghadapi kesulitan karena saya bisa mengandalkan kemampuan saya untuk"
              " mengatasi masalah.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q8 = models.StringField(
        label="Ketika saya dihadapkan dengan suatu masalah, saya dapat menemukan beberapa solusi.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q9 = models.StringField(
        label="Jika saya sedang dalam kesulitan, saya bisa memikirkan solusi yang baik.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q10 = models.StringField(
        label="Saya bisa mengatasi apa pun yang datang menghampiri saya.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q11 = models.StringField(
        label="Saya sering menetapkan tujuan tetapi kemudian memilih untuk mengejar tujuan yang berbeda.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q12 = models.StringField(
        label="Ide-ide baru dan proyek-proyek baru terkadang mengalihkan perhatian saya dari yang sebelumnya.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q13 = models.StringField(
        label="Saya tertarik pada kegiatan baru setiap beberapa bulan sekali.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q14 = models.StringField(
        label="Minat saya berubah dari tahun ke tahun.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q15 = models.StringField(
        label="Saya pernah terobsesi dengan ide atau proyek tertentu untuk waktu yang singkat, tetapi kemudian"
              " kehilangan minat.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q16 = models.StringField(
        label="Saya kesulitan mempertahankan fokus pada proyek yang membutuhkan waktu lebih dari beberapa bulan untuk"
              " diselesaikan.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q17 = models.StringField(
        label="Saya telah mencapai tujuan yang membutuhkan kerja keras selama bertahun-tahun.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q18 = models.StringField(
        label="Saya telah mengatasi berbagai rintangan untuk menaklukkan tantangan penting.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q19 = models.StringField(
        label="Saya menyelesaikan apa pun yang saya mulai.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q20 = models.StringField(
        label="Kemunduran tidak membuatku patah semangat.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q21 = models.StringField(
        label="Saya seorang pekerja keras.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )
    q22 = models.StringField(
        label="Saya seorang yang rajin.",
        choices=['Sama Sekali Tidak Benar', 'Tidak Benar', 'Netral', 'Benar', 'Sangat Benar'],
        widget=widgets.RadioSelect
    )

    # Demographic questions
    usia = models.IntegerField(
        label="Usia Anda (dalam tahun):"
    )
    jenis_kelamin = models.StringField(
        label="Jenis kelamin Anda:",
        choices=['Laki-laki', 'Perempuan'],
        widget=widgets.RadioSelect
    )
    pendidikan = models.StringField(
        label="Tingkat pendidikan yang sedang atau telah Anda tempuh:",
        choices=['Sarjana (S1/D4)', 'Magister (S2)', 'Doktoral (S3)'],
        widget=widgets.RadioSelect
    )
    aktivitas = models.StringField(
        label="Aktivitas utama Anda saat ini:",
        choices=['Kuliah', 'Lulus belum bekerja', 'Bekerja'],
        widget=widgets.RadioSelect
    )
    bidang_studi = models.StringField(
        label="Cakupan bidang studi yang sedang atau telah Anda tempuh:",
        choices=['Ilmu Pendidikan (Bimbingan Konseling, Teknologi Pendidika, Administratsi Pendidikan, PGSD, PGPAUD,'
                 ' PLB, PLS)',
                 'Sastra (Pendidikan Bahasa, Ilmu Perpustakaan, Seni & Desain)',
                 'MIPA (Matematika, Fisika, Kimia, Biologi, Bioteknologi, Gizi, Pendidikan IPA)',
                 'Ekonomi & Bisnis (Manajemen, Akuntansi, Ekonomi Pembangunan, Pendidikan Bisnis, Pendidikan'
                 ' Administrasi Perkantoran)',
                 'Teknik (Mesin, Sipil, Elektro, Informatika, Otomotif, Tata Boga, Rias, Busana)',
                 'Ilmu Keolaragaan (Pendidikan Jasmani, Kesehatan, Rekreasi (PJKR), Ilmu Olahraga, Pendidikan'
                 ' Kepelatihan Olahraga)',
                 'Ilmu Sosial (Hukun & Kewarganegaraan, Geografi, Sejaran, Sosiologi, Ilmu Komunikasi)',
                 'Psikologi',
                 'Vokasi (Perpustakaan Digital, Animasi, Manajemen Pemasaran & Akuntansi, Teknologi Rekayasa)',
                 'Kedokteran (Kedokteran & Ilmu Kesehatan Masyarakat)',
                 ],
        widget=widgets.RadioSelect
    )
    metode_pembayaran = models.StringField(
        label="Metode pembayaran online yang Anda gunakan:",
        choices=['OVO', 'GoPay', 'Shopee Pay', 'Bank BNI', 'Bank Mandiri'],
        widget=widgets.RadioSelect
    )
    no_hp_rekening = models.StringField(
        label="No. HP untuk online payment/No. Rekening:"
    )
    menariknya_eksperimen = models.StringField(
        label="Seberapa menariknya eksperimen ini bagi Anda:",
        choices=['Tidak menarik', 'Cukup menarik', 'Menarik', 'Sangat menarik'],
        widget=widgets.RadioSelect
    )

class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15',
                   'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22']

class Demographic(Page):
    form_model = 'player'
    form_fields = ['usia', 'jenis_kelamin', 'pendidikan', 'aktivitas', 'bidang_studi', 'metode_pembayaran',
                   'no_hp_rekening', 'menariknya_eksperimen']

page_sequence = [Demographic, Survey]
