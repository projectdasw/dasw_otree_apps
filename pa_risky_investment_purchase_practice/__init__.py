from otree.api import *
import random

doc = """
Risky Investment Purchase - Sesi Latihan
"""


class Constants(BaseConstants):
    name_in_url = 'pa_risky_investment_purchase_practice'
    players_per_group = None
    num_rounds = 2
    endowment = cu(100)
    additional = cu(30)
    consumption = cu(35)
    cost_per_option = cu(20)
    options_data_price = [
        {'name': 'Opsi 1', 'outcomes': [(45, 0.5), (10, 0.25), (0, 0.25)]},
        {'name': 'Opsi 2', 'outcomes': [(45, 0.4), (20, 0.35), (0, 0.25)]},
        {'name': 'Opsi 3', 'outcomes': [(45, 0.4), (15, 0.4), (5, 0.2)]},
        {'name': 'Opsi 4', 'outcomes': [(45, 0.35), (15, 0.55), (10, 0.1)]},
        {'name': 'Opsi 5', 'outcomes': [(45, 0.45), (10, 0.40), (5, 0.15)]},
        {'name': 'Opsi 6', 'outcomes': [(40, 0.5), (10, 0.5), (0, 0)]},
        {'name': 'Opsi 7', 'outcomes': [(40, 0.4), (20, 0.4), (5, 0.2)]},
        {'name': 'Opsi 8', 'outcomes': [(40, 0.6), (5, 0.2), (0, 0.2)]},
        {'name': 'Opsi 9', 'outcomes': [(40, 0.45), (20, 0.35), (0, 0.2)]},
        {'name': 'Opsi 10', 'outcomes': [(40, 0.5), (15, 0.25), (5, 0.25)]},
        {'name': 'Opsi 11', 'outcomes': [(35, 0.4), (20, 0.4), (15, 0.2)]},
        {'name': 'Opsi 12', 'outcomes': [(35, 0.5), (25, 0.25), (5, 0.25)]},
        {'name': 'Opsi 13', 'outcomes': [(35, 0.6), (15, 0.2), (5, 0.5)]},
        {'name': 'Opsi 14', 'outcomes': [(35, 0.25), (25, 0.65), (0, 0.1)]},
        {'name': 'Opsi 15', 'outcomes': [(35, 0.5), (20, 0.25), (10, 0.25)]},
        {'name': 'Opsi 16', 'outcomes': [(30, 0.7), (20, 0.2), (0, 0.1)]},
        {'name': 'Opsi 17', 'outcomes': [(30, 0.5), (25, 0.4), (0, 0.1)]},
        {'name': 'Opsi 18', 'outcomes': [(30, 0.6), (20, 0.3), (10, 0.1)]},
        {'name': 'Opsi 19', 'outcomes': [(30, 0.7), (15, 0.25), (5, 0.05)]},
        {'name': 'Opsi 20', 'outcomes': [(30, 0.6), (25, 0.25), (5, 0.15)]},
        {'name': 'Opsi 21', 'outcomes': [(50, 0.5), (0, 0.25), (0, 0.25)]},
        {'name': 'Opsi 22', 'outcomes': [(50, 0.4), (10, 0.35), (6, 0.25)]},
        {'name': 'Opsi 23', 'outcomes': [(50, 0.4), (11, 0.4), (3, 0.2)]},
        {'name': 'Opsi 24', 'outcomes': [(50, 0.35), (12, 0.55), (9, 0.1)]},
        {'name': 'Opsi 25', 'outcomes': [(50, 0.45), (4, 0.4), (6, 0.15)]},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    uang_sesudah_tambah_bansos = models.CurrencyField(initial=0)
    uang_sebelum_tambah_bansos = models.CurrencyField(initial=0)
    uang_sisa_tidak_untuk_investasi = models.CurrencyField(initial=0)
    bantuan_sosial = models.CurrencyField(initial=0)
    beban_konsumsi = models.CurrencyField(initial=0)
    total_profit = models.CurrencyField(initial=0)
    total_biaya_beli_opsi = models.CurrencyField(initial=0)
    opsi_1 = models.StringField(blank=True, initial="")
    hasil_opsi_1 = models.FloatField(initial=0)
    opsi_2 = models.StringField(blank=True, initial="")
    hasil_opsi_2 = models.FloatField(initial=0)
    opsi_3 = models.StringField(blank=True, initial="")
    hasil_opsi_3 = models.FloatField(initial=0)
    opsi_4 = models.StringField(blank=True, initial="")
    hasil_opsi_4 = models.FloatField(initial=0)
    opsi_5 = models.StringField(blank=True, initial="")
    hasil_opsi_5 = models.FloatField(initial=0)
    total_akhir_profit = models.CurrencyField(initial=0)
    total_akhir_beli_opsi = models.CurrencyField(initial=0)
    total_akhir_bantuan_sosial = models.CurrencyField(initial=0)
    total_akhir_beban_konsumsi = models.CurrencyField(initial=0)
    total_akhir_uang = models.CurrencyField(initial=0)


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
    form_model = 'player'
    form_fields = ['opsi_1', 'opsi_2', 'opsi_3', 'opsi_4', 'opsi_5']

    @staticmethod
    def vars_for_template(player: Player):
        # Key berdasarkan ronde
        key = f'random_options_round_{player.round_number}'

        # Acak hanya sekali untuk ronde ini
        if key not in player.participant.vars:
            random_options = random.sample(Constants.options_data_price, 5)
            for option in random_options:
                option['formatted_outcomes'] = [
                    f"Anda mendapatkan {value} poin dengan peluang {int(probability * 100)}%"
                    for value, probability in option['outcomes']
                ]

            player.participant.vars[key] = random_options

        random_options = player.participant.vars[key]

        # Ambil sisa uang subjek dari ronde sebelumnya
        if player.round_number > 1:
            previous_round_endowment = player.in_round(player.round_number - 1).payoff
            player.uang_sebelum_tambah_bansos = previous_round_endowment
            player.bantuan_sosial = Constants.additional
            player.beban_konsumsi = Constants.consumption
            player.uang_sesudah_tambah_bansos = player.uang_sebelum_tambah_bansos + player.bantuan_sosial

        return {
            'random_options': random_options,
        }

    @staticmethod
    def error_message(player: Player, values):
        selected_options = [
            values[f'opsi_{i}']
            for i in range(1, 6)
        ]
        selected_count = sum(1 for option in selected_options if option)
        total_cost = selected_count * Constants.cost_per_option

        error_msgs = []
        if player.uang_sebelum_tambah_bansos >= 0:
            if total_cost > player.uang_sesudah_tambah_bansos:
                error_msgs.append(
                    f"Uang Anda tidak mencukupi untuk membeli {selected_count} opsi"
                    f" (Total biaya: {total_cost})."
                )
        elif player.uang_sebelum_tambah_bansos < 0:
            if total_cost > player.bantuan_sosial:
                error_msgs.append(
                    f"Uang Bantuan Anda tidak mencukupi untuk membeli {selected_count} opsi"
                    f" (Total biaya: {total_cost})."
                )

        # Jika ada pesan kesalahan, gabungkan dan kembalikan
        if error_msgs:
            return "<br>".join(error_msgs)
        return ""

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Key berdasarkan ronde
        key = f'random_options_round_{player.round_number}'

        # Daftar pilihan opsi
        selected_options = [
            (getattr(player, f"opsi_{i}"), f"hasil_opsi_{i}")
            for i in range(1, 6)
        ]

        # Proses setiap pilihan
        for selected_option_name, result_field in selected_options:
            selected_option = next(
                (
                    option
                    for option in Constants.options_data_price
                    if option['name'] == selected_option_name
                ),
                None
            )

            if selected_option:
                draw = random.randint(1, 100)
                cumulative_probability = 0

                for outcome, probability in selected_option['outcomes']:
                    cumulative_probability += probability * 100

                    if draw <= cumulative_probability:
                        setattr(player, result_field, outcome)
                        player.total_profit += outcome
                        break

        # Hapus data acakan ronde ini
        player.participant.vars.pop(key, None)


class single_results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        selected_options = [
            (getattr(player, f"opsi_{i}"), f"hasil_opsi_{i}")
            for i in range(1, 6)
        ]

        selected_count = sum(1 for option, _ in selected_options if option)
        player.total_biaya_beli_opsi = (selected_count * Constants.cost_per_option)

        # Perhitungan jika Uang Utama subjek kurang dari 0 (minus) - menjadi Hutang
        if player.uang_sebelum_tambah_bansos >= 0:
            player.payoff = ((player.uang_sesudah_tambah_bansos + player.total_profit) - player.total_biaya_beli_opsi -
                             player.beban_konsumsi)
        elif player.uang_sebelum_tambah_bansos < 0:
            player.uang_sisa_tidak_untuk_investasi = player.bantuan_sosial - player.total_biaya_beli_opsi
            player.payoff = ((player.uang_sisa_tidak_untuk_investasi + player.total_profit) +
                             player.uang_sebelum_tambah_bansos - player.total_biaya_beli_opsi - player.beban_konsumsi)

        return {
            "options": [
                {
                    "no": i,
                    "result": getattr(player, f"hasil_opsi_{i}"),
                }
                for i in range(1, 6)
                if getattr(player, f"opsi_{i}")
            ]
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Simpan hasil ronde
        player.participant.vars.setdefault("results_risky_purchase_practice", []).append({
            "round_number_risky_purchase": player.round_number,
            "endowment_round": player.uang_sebelum_tambah_bansos,
            "profit_risky_purchase": player.total_profit,
            "cost_risky_purchase": player.total_biaya_beli_opsi,
            "endowment_risky_purchase": player.payoff,
            "additional_risky_purchase": player.bantuan_sosial,
            "charge_additional_risky_purchase": player.uang_sisa_tidak_untuk_investasi,
            "consumption_risky_purchase": player.beban_konsumsi,
        })


class final_results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        results_risky_purchase = participant.vars.get("results_risky_purchase_practice", [])

        last_round_risky_purchase = (
            participant.vars.get("last_round_played_risky_purchase_practice", 1)
            if participant.vars.get("end_game", False)
            else player.round_number
        )

        # Total Akhir Semua Pendapatan
        player.total_akhir_profit = sum(item["profit_risky_purchase"] for item in results_risky_purchase)
        player.total_akhir_beli_opsi = sum(item["cost_risky_purchase"] for item in results_risky_purchase)
        player.total_akhir_bantuan_sosial = sum(item["additional_risky_purchase"] for item in results_risky_purchase)
        player.total_akhir_beban_konsumsi = sum(item["consumption_risky_purchase"] for item in results_risky_purchase)
        player.total_akhir_uang = sum(item["endowment_risky_purchase"] for item in results_risky_purchase)

        # Menentukan Final Payment
        if player.in_round(player.round_number).payoff < 0:
            final_payment = player.in_round(player.round_number).payoff
            final_round_endowment = player.in_round(player.round_number).payoff
        else:
            final_payment = 0
            final_round_endowment = player.in_round(player.round_number).payoff

        participant.vars["summary_risky_purchase_practice"] = {
            "profit": player.total_akhir_profit,
            "cost": player.total_akhir_beli_opsi,
            "additional": player.total_akhir_bantuan_sosial,
            "consumption": player.total_akhir_beban_konsumsi,
            "endowment": player.total_akhir_uang,
            "payment_selected": final_payment,
        }

        return {
            "results_risky_purchase_practice": results_risky_purchase,
            "last_round_played_risky_purchase_practice": last_round_risky_purchase,
            "final_payment_practice": final_round_endowment,
        }


class end_practice(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [endowment_information, Loading, game, single_results, final_results, end_practice]
