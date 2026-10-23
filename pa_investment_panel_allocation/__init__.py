from otree.api import *
import random

doc = """
Investment Panel Allocation
"""


class Constants(BaseConstants):
    name_in_url = 'pa_investment_panel_allocation'
    players_per_group = None
    num_rounds = 10
    endowment = cu(100)
    additional = cu(30)
    consumption = cu(35)
    investment_scheme = [
        {"investment_return": 1.15, "probability": 0.9},
        {"investment_return": 1.2, "probability": 0.85},
        {"investment_return": 1.25, "probability": 0.8},
        {"investment_return": 1.35, "probability": 0.75},
        {"investment_return": 1.45, "probability": 0.7},
        {"investment_return": 1.55, "probability": 0.65},
        {"investment_return": 1.67, "probability": 0.6},
        {"investment_return": 1.85, "probability": 0.55},
        {"investment_return": 2.0, "probability": 0.5},
        {"investment_return": 2.25, "probability": 0.45},
        {"investment_return": 2.5, "probability": 0.4},
        {"investment_return": 2.9, "probability": 0.35},
        {"investment_return": 3.4, "probability": 0.3},
        {"investment_return": 4.0, "probability": 0.25},
        {"investment_return": 5.0, "probability": 0.2},
        {"investment_return": 7.0, "probability": 0.15},
        {"investment_return": 10.0, "probability": 0.1},
    ]


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
    total_profit_return = models.CurrencyField(initial=0)
    total_alokasi_opsi = models.CurrencyField(initial=0)
    asian_ev_1 = models.FloatField(initial=0)
    result_asian_1 = models.FloatField(initial=0)
    asian_ev_2 = models.FloatField(initial=0)
    result_asian_2 = models.FloatField(initial=0)
    asian_ev_3 = models.FloatField(initial=0)
    result_asian_3 = models.FloatField(initial=0)
    asian_ev_4 = models.FloatField(initial=0)
    result_asian_4 = models.FloatField(initial=0)
    asian_ev_5 = models.FloatField(initial=0)
    result_asian_5 = models.FloatField(initial=0)
    asian_ev_6 = models.FloatField(initial=0)
    result_asian_6 = models.FloatField(initial=0)
    asian_ev_7 = models.FloatField(initial=0)
    result_asian_7 = models.FloatField(initial=0)
    asian_ev_8 = models.FloatField(initial=0)
    result_asian_8 = models.FloatField(initial=0)
    asian_ev_9 = models.FloatField(initial=0)
    result_asian_9 = models.FloatField(initial=0)
    asian_ev_10 = models.FloatField(initial=0)
    result_asian_10 = models.FloatField(initial=0)
    asian_ev_11 = models.FloatField(initial=0)
    result_asian_11 = models.FloatField(initial=0)
    asian_ev_12 = models.FloatField(initial=0)
    result_asian_12 = models.FloatField(initial=0)
    asian_ev_13 = models.FloatField(initial=0)
    result_asian_13 = models.FloatField(initial=0)
    asian_ev_14 = models.FloatField(initial=0)
    result_asian_14 = models.FloatField(initial=0)
    asian_ev_15 = models.FloatField(initial=0)
    result_asian_15 = models.FloatField(initial=0)
    asian_ev_16 = models.FloatField(initial=0)
    result_asian_16 = models.FloatField(initial=0)
    asian_ev_17 = models.FloatField(initial=0)
    result_asian_17 = models.FloatField(initial=0)
    total_akhir_profit_return = models.CurrencyField(initial=0)
    total_akhir_alokasi_opsi = models.CurrencyField(initial=0)
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

def live_update(player, data):
    action = data.get("action")
    if action == "page_loaded":
        player.realtime_status = "Sudah Masuk Halaman"
        return broadcast_status(player)
    elif action == "allocation_changed":
        allocations = data.get("allocations", {})
        total = sum(allocations.values())
        if total > 0:
            player.realtime_status = "Sedang Mengalokasikan Dana"
        else:
            player.realtime_status = "Sudah Masuk Halaman"

        return broadcast_status(player)

    elif action == "submit":
        allocations = data.get("allocations", {})
        total = sum(allocations.values())

        if total > 0:
            player.realtime_status = "Player telah mengalokasikan dana"
        else:
            player.realtime_status = "Player tidak mengalokasikan dana"

        return broadcast_status(player)


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


class game(Page):
    form_model = "player"
    form_fields = [f"asian_ev_{i}" for i in range(1, 18)]
    live_method = live_update

    @staticmethod
    def vars_for_template(player: Player):
        # Ambil sisa uang subjek dari ronde sebelumnya
        if player.round_number > 1:
            previous_round_endowment = player.in_round(player.round_number - 1).payoff
            player.uang_sebelum_tambah_bansos = previous_round_endowment
            player.bantuan_sosial = Constants.additional
            player.uang_sesudah_tambah_bansos = player.uang_sebelum_tambah_bansos + player.bantuan_sosial
            player.beban_konsumsi = Constants.consumption

        # Mengonversi probabilitas menjadi persentase
        investment_scheme_with_percentage = [
            {
                "investment_return": scheme["investment_return"],
                "probability": int(scheme["probability"] * 100)  # Konversi ke persentase
            }
            for scheme in Constants.investment_scheme
        ]

        return {
            'investment_scheme': investment_scheme_with_percentage,
            "my_id": player.id_in_group,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Random drawing untuk setiap opsi
        for i, investment_scheme in enumerate(Constants.investment_scheme, start=1):
            draw = random.randint(1, 100)  # Angka random 1-100
            probability = investment_scheme["probability"] * 100
            if draw <= probability:
                # Subjek mendapatkan return
                setattr(player, f"result_asian_{i}", investment_scheme["investment_return"])
            else:
                # Subjek tidak mendapatkan return
                setattr(player, f"result_asian_{i}", 0)

        player.total_profit_return = sum(
            getattr(player, f"asian_ev_{i}") *
            getattr(player, f"result_asian_{i}")
            for i in range(1, 18)
        )

    @staticmethod
    def error_message(player: Player, values):
        allocations = [
            values[f'asian_ev_{i}'] or 0
            for i in range(1, 18)
        ]

        total_allocation = sum(allocations)

        error_msgs = []
        if player.uang_sebelum_tambah_bansos >= 0:
            if total_allocation > player.uang_sesudah_tambah_bansos:
                error_msgs.append(
                    f"Uang Anda tidak mencukupi untuk melakukan alokasi sebesar {total_allocation}"
                )
        elif player.uang_sebelum_tambah_bansos < 0:
            if total_allocation > player.bantuan_sosial:
                error_msgs.append(
                    f"Uang Bantuan Anda tidak mencukupi melakukan alokasi sebesar {total_allocation}"
                )

        # Jika ada pesan kesalahan, gabungkan dan kembalikan
        if error_msgs:
            return "<br>".join(error_msgs)
        return ""


class single_results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        investment_results = [
            {
                "no": i,
                "allocation": allocation,
                "return": result,
                "profit": allocation * result,
            }
            for i in range(1, 18)
            for allocation, result in [(
                getattr(player, f"asian_ev_{i}"),
                getattr(player, f"result_asian_{i}")
            )]
            if allocation > 0
        ]

        player.total_profit_return = sum(
            item["profit"] for item in investment_results
        )

        player.total_alokasi_opsi = sum(
            item["allocation"] for item in investment_results
        )

        # Perhitungan jika Uang Utama subjek kurang dari 0 (minus) - menjadi Hutang
        if player.uang_sebelum_tambah_bansos >= 0:
            player.payoff = ((player.uang_sesudah_tambah_bansos + player.total_profit_return) -
                             player.total_alokasi_opsi - player.beban_konsumsi)
        elif player.uang_sebelum_tambah_bansos < 0:
            player.uang_sisa_tidak_untuk_investasi = player.bantuan_sosial - player.total_alokasi_opsi
            player.payoff = ((player.uang_sisa_tidak_untuk_investasi + player.total_profit_return) +
                             player.uang_sebelum_tambah_bansos - player.total_alokasi_opsi - player.beban_konsumsi)

        return dict(
            investment_results=investment_results,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        total_cost = sum(
            getattr(player, f"asian_ev_{i}")
            for i in range(1, 18)
        )

        player.total_alokasi_opsi = total_cost

        player.participant.vars.setdefault("results_panel_allocation", []).append({
            "round_number_panel_allocation": player.round_number,
            "endowment_round": player.uang_sebelum_tambah_bansos,
            "profit_panel_allocation": player.total_profit_return,
            "cost_panel_allocation": player.total_alokasi_opsi,
            "endowment_panel_allocation": player.payoff,
            "additional_panel_allocation": player.bantuan_sosial,
            "charge_additional_panel_allocation": player.uang_sisa_tidak_untuk_investasi,
            "consumption_panel_allocation": player.beban_konsumsi,
        })


class final_results(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

        results_panel_allocation = participant.vars.get("results_panel_allocation", [])
        last_round_panel_allocation = (
            participant.vars.get("last_round_played_panel_allocation", 1)
            if participant.vars.get("end_game", False)
            else player.round_number
        )

        player.total_akhir_profit_return = sum(item["profit_panel_allocation"] for item in results_panel_allocation)
        player.total_akhir_alokasi_opsi = sum(item["cost_panel_allocation"] for item in results_panel_allocation)
        player.total_akhir_bantuan_sosial = sum(
            item["additional_panel_allocation"]
            for item in results_panel_allocation
        )
        player.total_akhir_beban_konsumsi = sum(
            item["consumption_panel_allocation"]
            for item in results_panel_allocation
        )
        player.total_akhir_uang = sum(item["endowment_panel_allocation"]for item in results_panel_allocation)

        # Menentukan Final Payment
        if player.in_round(player.round_number).payoff < 0:
            final_payment = 0
            final_round_endowment = player.in_round(player.round_number).payoff
        else:
            final_payment = player.in_round(player.round_number).payoff
            final_round_endowment = player.in_round(player.round_number).payoff

        participant.vars["summary_panel_allocation"] = {
            "profit": player.total_akhir_profit_return,
            "cost": player.total_akhir_alokasi_opsi,
            "additional": player.total_akhir_bantuan_sosial,
            "consumption": player.total_akhir_beban_konsumsi,
            "endowment": player.total_akhir_uang,
            "payment_selected": final_payment,
        }

        return dict(
            results_panel_allocation=results_panel_allocation,
            last_round_panel_allocation=last_round_panel_allocation,
            final_payment=final_round_endowment,
        )


class end_session(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

page_sequence = [endowment_information, Loading, game, single_results, final_results, end_session]
