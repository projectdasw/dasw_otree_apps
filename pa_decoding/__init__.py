from otree.api import *
import random

doc = """
Real Effort Decoding
"""


class Constants(BaseConstants):
    name_in_url = 'pa_decoding'
    players_per_group = None
    num_rounds = 10
    endowment = cu(100)
    additional = cu(30)
    consumption = cu(35)

    # game Setup
    board_rows = 5  # Jumlah baris papan
    board_columns = 7  # Jumlah kolom papan
    price_time = 5
    target_character = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    players = subsession.get_players()
    random_ids = list(range(1, len(players) + 1))
    random.shuffle(random_ids)

    for player, random_id in zip(players, random_ids):
        player.id_in_group = random_id


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    uang_sesudah_tambah_bansos = models.CurrencyField(initial=0)
    uang_sebelum_tambah_bansos = models.CurrencyField(initial=0)
    uang_sisa_tidak_untuk_investasi = models.CurrencyField(initial=0)
    bantuan_sosial = models.CurrencyField(initial=0)
    beban_konsumsi = models.CurrencyField(initial=0)
    beli_waktu = models.IntegerField(initial=0)
    waktu_bermain = models.IntegerField(initial=0)
    total_score = models.IntegerField(initial=0)
    count_guess = models.IntegerField(label="Berapa kali huruf/angka muncul:")
    actual_count = models.IntegerField(initial=0)
    current_target = models.StringField()  # Target huruf/angka yang diacak setiap putaran
    total_akhir_score = models.CurrencyField(initial=0)
    total_akhir_beli_waktu = models.CurrencyField(initial=0)
    total_akhir_bantuan_sosial = models.CurrencyField(initial=0)
    total_akhir_beban_konsumsi = models.CurrencyField(initial=0)
    total_akhir_uang = models.CurrencyField(initial=0)
    realtime_status = models.StringField(initial="Belum Masuk Halaman")


def broadcast_status(player):
    players = [
        dict(
            id=p.id_in_group,
            status=p.realtime_status,
        )
        for p in player.group.get_players()
    ]

    return {
        0: {
            "players": players
        }
    }


def live_game(player: Player, data):
    action = data.get("action")
    allocation = data.get("allocation", 0)

    if action == "page_loaded":
        player.realtime_status = "Sudah Masuk Halaman"
        return broadcast_status(player)

    elif action == "allocation_changed":
        if allocation > 0:
            player.realtime_status = "Sedang Mengalokasikan Dana"
        else:
            player.realtime_status = "Sudah Masuk Halaman"

        return broadcast_status(player)

    elif action == "submit_buy_time":
        if allocation > 0:
            player.realtime_status = "Player membeli waktu bermain"
        else:
            player.realtime_status = "Player tidak membeli waktu bermain"

        return broadcast_status(player)

    # elif action == "start_decoding":
    #     if player.beli_waktu > 0:
    #         player.realtime_status = "Sedang Bermain Decoding"
    #     return broadcast_status(player)
    #
    # elif action == "finish_decoding":
    #     player.realtime_status = "Telah menyelesaikan Decoding"
    #     return broadcast_status(player)

    elif 'count_guess' in data:
        guess = int(data["count_guess"])

        if guess == player.actual_count:
            player.total_score += 3

        player.current_target = random.choice(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        )

        board = [
            [
                random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
                for _ in range(Constants.board_columns)
            ]
            for _ in range(Constants.board_rows)
        ]

        player.actual_count = sum(
            row.count(player.current_target)
            for row in board
        )

        return {
            player.id_in_group: {
                "new_board": board,
                "new_target_character": player.current_target,
                "new_score": player.total_score,
            },

            0: broadcast_status(player)[0],
        }


class Loading(WaitPage):
    title_text = "Ruang Tunggu Eksperimen"


class endowment_information(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        player.uang_sebelum_tambah_bansos = Constants.endowment
        player.bantuan_sosial = Constants.additional
        player.beban_konsumsi = Constants.consumption
        player.uang_sesudah_tambah_bansos = player.uang_sebelum_tambah_bansos + player.bantuan_sosial


class buy_time(Page):
    form_model = 'player'
    form_fields = ['beli_waktu']

    live_method = live_game

    @staticmethod
    def vars_for_template(player: Player):
        # Ambil sisa uang subjek dari ronde sebelumnya
        if player.round_number > 1:
            previous_round_endowment = player.in_round(player.round_number - 1).payoff
            player.uang_sebelum_tambah_bansos = previous_round_endowment
            player.bantuan_sosial = Constants.additional
            player.uang_sesudah_tambah_bansos = player.uang_sebelum_tambah_bansos + player.bantuan_sosial
            player.beban_konsumsi = Constants.consumption

        return {
            'my_id': player.id_in_group,
        }

    @staticmethod
    def error_message(player: Player, values):
        error_msgs = []
        if player.uang_sebelum_tambah_bansos >= 0:
            if values['beli_waktu'] % Constants.price_time != 0:
                error_msgs.append(
                    f"Jumlah uang yang dibelanjakan harus dalam kelipatan 5."
                )
            elif values['beli_waktu'] > player.uang_sesudah_tambah_bansos:
                error_msgs.append(
                    f"Uang Anda tidak mencukupi untuk membeli waktu bermain."
                )
        elif player.uang_sebelum_tambah_bansos < 0:
            if values['beli_waktu'] % Constants.price_time != 0:
                error_msgs.append(
                    f"Jumlah uang yang dibelanjakan harus dalam kelipatan 5."
                )
            elif values['beli_waktu'] > player.bantuan_sosial:
                error_msgs.append(
                    f"Uang Bantuan Anda tidak mencukupi untuk membeli waktu bermain."
                )

        # Jika ada pesan kesalahan, gabungkan dan kembalikan
        if error_msgs:
            return "<br>".join(error_msgs)
        return ""

class game(Page):
    form_model = 'player'
    form_fields = ['count_guess']
    live_method = live_game

    @staticmethod
    def is_displayed(player):
        return player.beli_waktu > 0

    # Menggunakan waktu yang dibeli oleh pemain
    @staticmethod
    def get_timeout_seconds(player: Player):
        return (player.beli_waktu // Constants.price_time) * 20

    @staticmethod
    def vars_for_template(player: Player):
        board = [
            [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(Constants.board_columns)]
            for _ in range(Constants.board_rows)
        ]
        player.current_target = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        player.actual_count = sum(row.count(player.current_target) for row in board)

        return {
            'board': board,
            'target_character': player.current_target,
            'player_score': player.total_score,
            'my_id': player.id_in_group,
        }

class single_results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Perhitungan jika Uang Utama subjek kurang dari 0 (minus) - menjadi Hutang
        if player.uang_sebelum_tambah_bansos >= 0:
            player.payoff = ((player.uang_sesudah_tambah_bansos + player.total_score) - player.beli_waktu -
                             player.beban_konsumsi)
        elif player.uang_sebelum_tambah_bansos < 0:
            player.uang_sisa_tidak_untuk_investasi = player.bantuan_sosial - player.beli_waktu
            player.payoff = ((player.uang_sisa_tidak_untuk_investasi + player.total_score) +
                             player.uang_sebelum_tambah_bansos - player.beli_waktu - player.beban_konsumsi)

        return {
            'final_score': player.total_score,
            'get_time': (player.beli_waktu // Constants.price_time) * 20,
            'sum_profit': player.uang_sesudah_tambah_bansos + player.total_score
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Simpan hasil ronde ke participant.vars
        if 'results_cognitive_task' not in player.participant.vars:
            player.participant.vars['results_cognitive_task'] = []

        player.participant.vars['results_cognitive_task'].append({
            'round_number_cognitive': player.round_number,
            "endowment_round": player.uang_sebelum_tambah_bansos,
            'score_cognitive': player.total_score,
            'time_cost_cognitive': player.beli_waktu,
            'endowment_cognitive': player.payoff,
            'additional_cognitive': player.bantuan_sosial,
            'charge_additional_cognitive': player.uang_sisa_tidak_untuk_investasi,
            'consumption_cognitive': player.beban_konsumsi
        })


class final_results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        results_cognitive_task = participant.vars.get(
            "results_cognitive_task", []
        )

        last_round_cognitive = (
            participant.vars.get("last_round_played_cognitive", 1)
            if participant.vars.get("end_game", False)
            else player.round_number
        )

        player.total_akhir_score = sum(item["score_cognitive"] for item in results_cognitive_task)
        player.total_akhir_beli_waktu = sum(item["time_cost_cognitive"] for item in results_cognitive_task)
        player.total_akhir_bantuan_sosial = sum(item["additional_cognitive"] for item in results_cognitive_task)
        player.total_akhir_beban_konsumsi = sum(item["consumption_cognitive"] for item in results_cognitive_task)
        player.total_akhir_uang = sum(item["endowment_cognitive"] for item in results_cognitive_task)

        # Menentukan Final Payment
        if player.in_round(player.round_number).payoff < 0:
            final_payment = 0
            final_round_endowment = player.in_round(player.round_number).payoff
        else:
            final_payment = player.in_round(player.round_number).payoff
            final_round_endowment = player.in_round(player.round_number).payoff

        participant.vars["summary_cognitive_task"] = {
            "profit": player.total_akhir_score,
            "cost": player.total_akhir_beli_waktu,
            "additional": player.total_akhir_bantuan_sosial,
            "consumption": player.total_akhir_beban_konsumsi,
            "endowment": player.total_akhir_uang,
            "payment_selected": final_payment,
        }

        return {
            "results_cognitive_task": results_cognitive_task,
            "last_round_cognitive": last_round_cognitive,
            "final_payment": final_round_endowment,
        }


class end_session(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [endowment_information, Loading, buy_time, game, single_results, final_results, end_session]
