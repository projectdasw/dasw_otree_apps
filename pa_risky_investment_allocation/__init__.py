from otree.api import *
import random

doc = """
Risky Investment Allocation
"""


class Constants(BaseConstants):
    name_in_url = 'pa_risky_investment_allocation'
    players_per_group = None
    num_rounds = 10
    endowment = cu(100)
    additional = cu(30)
    consumption = cu(35)
    options_data_allocation = [
        {'name': 'Opsi 1', 'outcomes': [(1.5, 0.65), (0.25, 0.1), (0, 0.25)]},
        {'name': 'Opsi 2', 'outcomes': [(1.5, 0.6), (0.5, 0.2), (0, 0.2)]},
        {'name': 'Opsi 3', 'outcomes': [(1.5, 0.55), (0.75, 0.25), (0, 0.3)]},
        {'name': 'Opsi 4', 'outcomes': [(1.5, 0.4), (1, 0.4), (0, 0.2)]},
        {'name': 'Opsi 5', 'outcomes': [(1.5, 0.5), (1.25, 0.2), (0, 0.3)]},
        {'name': 'Opsi 6', 'outcomes': [(2, 0.4), (0.5, 0.4), (0, 0.2)]},
        {'name': 'Opsi 7', 'outcomes': [(2, 0.35), (0.75, 0.4), (0, 0.25)]},
        {'name': 'Opsi 8', 'outcomes': [(2, 0.45), (0.25, 0.4), (0, 0.05)]},
        {'name': 'Opsi 9', 'outcomes': [(2, 0.4), (1, 0.2), (0, 0.4)]},
        {'name': 'Opsi 10', 'outcomes': [(2, 0.35), (1.5, 0.2), (0, 0.45)]},
        {'name': 'Opsi 11', 'outcomes': [(2.5, 0.35), (0.25, 0.5), (0, 0.15)]},
        {'name': 'Opsi 12', 'outcomes': [(2.5, 0.3), (0.5, 0.5), (0, 0.2)]},
        {'name': 'Opsi 13', 'outcomes': [(2.5, 0.3), (0.75, 0.35), (0, 0.35)]},
        {'name': 'Opsi 14', 'outcomes': [(2.5, 0.2), (1, 0.5), (0, 0.3)]},
        {'name': 'Opsi 15', 'outcomes': [(2.5, 0.1), (1.25, 0.6), (0, 0.3)]},
        {'name': 'Opsi 16', 'outcomes': [(3, 0.3), (0.5, 0.2), (0, 0.5)]},
        {'name': 'Opsi 17', 'outcomes': [(3, 0.3), (0.25, 0.4), (0, 0.3)]},
        {'name': 'Opsi 18', 'outcomes': [(3, 0.2), (1, 0.4), (0, 0.4)]},
        {'name': 'Opsi 19', 'outcomes': [(3, 0.25), (1.25, 0.25), (0, 0.55)]},
        {'name': 'Opsi 20', 'outcomes': [(3, 0.15), (0.75, 0.75), (0, 0.1)]},
        {'name': 'Opsi 21', 'outcomes': [(3.5, 0.25), (0.5, 0.25), (0, 0.5)]},
        {'name': 'Opsi 22', 'outcomes': [(3.5, 0.25), (0.25, 0.5), (0, 0.25)]},
        {'name': 'Opsi 23', 'outcomes': [(3.5, 0.2), (1, 0.3), (0, 0.5)]},
        {'name': 'Opsi 24', 'outcomes': [(3.5, 0.2), (1.25, 0.25), (0, 0.55)]},
        {'name': 'Opsi 25', 'outcomes': [(3.5, 0.2), (0.75, 0.4), (0, 0.4)]},
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
    total_profit = models.CurrencyField(initial=0)
    total_alokasi_opsi = models.CurrencyField(initial=0)
    opsi_1 = models.StringField(blank=True, initial="")
    alokasi_opsi_1 = models.FloatField(initial=0)
    hasil_opsi_1 = models.FloatField(initial=0)
    opsi_2 = models.StringField(blank=True, initial="")
    alokasi_opsi_2 = models.FloatField(initial=0)
    hasil_opsi_2 = models.FloatField(initial=0)
    opsi_3 = models.StringField(blank=True, initial="")
    alokasi_opsi_3 = models.FloatField(initial=0)
    hasil_opsi_3 = models.FloatField(initial=0)
    opsi_4 = models.StringField(blank=True, initial="")
    alokasi_opsi_4 = models.FloatField(initial=0)
    hasil_opsi_4 = models.FloatField(initial=0)
    opsi_5 = models.StringField(blank=True, initial="")
    alokasi_opsi_5 = models.FloatField(initial=0)
    hasil_opsi_5 = models.FloatField(initial=0)
    total_akhir_profit = models.CurrencyField(initial=0)
    total_akhir_alokasi_opsi = models.CurrencyField(initial=0)
    total_akhir_bantuan_sosial = models.CurrencyField(initial=0)
    total_akhir_beban_konsumsi = models.CurrencyField(initial=0)
    total_akhir_uang = models.CurrencyField(initial=0)
    realtime_status = models.StringField(initial="Belum Masuk Halaman")

def live_update(player, data):
    if data["action"] == "page_loaded":
        player.realtime_status = "Sudah Masuk Halaman"

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

    elif data["action"] == "allocation_changed":
        allocations = data.get("allocations", {})

        if sum(allocations.values()) > 0:
            player.realtime_status = "Sedang Mengalokasikan Dana"
        else:
            player.realtime_status = "Sudah Masuk Halaman"

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

    elif data["action"] == "submit":
        allocations = data.get("allocations", {})

        if sum(allocations.values()) > 0:
            player.realtime_status = "Player telah mengalokasikan dana"
        else:
            player.realtime_status = "Player tidak mengalokasikan dana"

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
    form_fields = [
        'opsi_1', 'alokasi_opsi_1',
        'opsi_2', 'alokasi_opsi_2',
        'opsi_3', 'alokasi_opsi_3',
        'opsi_4', 'alokasi_opsi_4',
        'opsi_5', 'alokasi_opsi_5',
    ]

    live_method = live_update

    @staticmethod
    def vars_for_template(player: Player):
        # Key berdasarkan ronde
        key = f'random_options_round_{player.round_number}'

        # Ambil sisa uang subjek dari ronde sebelumnya
        if player.round_number > 1:
            previous_round_endowment = player.in_round(player.round_number - 1).payoff
            player.uang_sebelum_tambah_bansos = previous_round_endowment
            player.bantuan_sosial = Constants.additional
            player.uang_sesudah_tambah_bansos = player.uang_sebelum_tambah_bansos + player.bantuan_sosial
            player.beban_konsumsi = Constants.consumption

        # Acak hanya sekali untuk ronde ini
        if key not in player.participant.vars:
            # Mendapatkan 5 pilihan acak unik dari daftar opsi
            random_options = random.sample(Constants.options_data_allocation, 5)

            # Membuat teks yang terstruktur untuk setiap opsi
            for option in random_options:
                option_outcomes = option['outcomes']
                formatted_outcomes = []
                for j, (value, probability) in enumerate(option_outcomes):
                    formatted_outcomes.append(f"Anda mendapatkan {value}x dengan peluang {int(probability * 100)}%")
                option['formatted_outcomes'] = formatted_outcomes  # List of outcomes for each option

            player.participant.vars[key] = random_options

        random_options = player.participant.vars[key]

        return {
            'random_options': random_options,
            'my_id': player.id_in_group,
        }

    @staticmethod
    def error_message(player: Player, values):
        allocations = [
            values[f'alokasi_opsi_{i}']
            for i in range(1, 6)
        ]

        total_allocation = sum(allocation or 0 for allocation in allocations)

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Key berdasarkan ronde
        key = f'random_options_round_{player.round_number}'

        for i in range(1, 6):
            selected_name = getattr(player, f"opsi_{i}")
            allocation = getattr(player, f"alokasi_opsi_{i}")

            if not selected_name or allocation == 0:
                continue

            selected_option = next(
                (
                    option
                    for option in Constants.options_data_allocation
                    if option["name"] == selected_name
                ),
                None,
            )

            if not selected_option:
                continue

            draw = random.randint(1, 100)
            cumulative_probability = 0

            for outcome, probability in selected_option["outcomes"]:
                cumulative_probability += probability * 100

                if draw <= cumulative_probability:
                    setattr(player, f"hasil_opsi_{i}", outcome)
                    break

        # Hapus data acakan ronde ini
        player.participant.vars.pop(key, None)


class single_results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        allocations = [
            {
                "no": i,
                "option": getattr(player, f"opsi_{i}"),
                "allocation": allocation,
                "result": result,
                "profit": allocation * result,
            }
            for i in range(1, 6)
            for allocation, result in [(
                getattr(player, f"alokasi_opsi_{i}"),
                getattr(player, f"hasil_opsi_{i}")
            )]
            if allocation != 0
        ]

        player.total_profit = sum(item["profit"] for item in allocations)
        player.total_alokasi_opsi = sum(item["allocation"] for item in allocations)

        # Perhitungan jika Uang Utama subjek kurang dari 0 (minus) - menjadi Hutang
        if player.uang_sebelum_tambah_bansos >= 0:
            player.payoff = ((player.uang_sesudah_tambah_bansos + player.total_profit) - player.total_alokasi_opsi -
                             player.beban_konsumsi)
        elif player.uang_sebelum_tambah_bansos < 0:
            player.uang_sisa_tidak_untuk_investasi = player.bantuan_sosial - player.total_alokasi_opsi
            player.payoff = ((player.uang_sisa_tidak_untuk_investasi + player.total_profit) +
                             player.uang_sebelum_tambah_bansos - player.total_alokasi_opsi - player.beban_konsumsi)

        return {
            "allocations": allocations,
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars.setdefault("results_risky_allocation", []).append({
            "round_number_risky_allocation": player.round_number,
            "endowment_round": player.uang_sebelum_tambah_bansos,
            "profit_risky_allocation": player.total_profit,
            "cost_risky_allocation": player.total_alokasi_opsi,
            "endowment_risky_allocation": player.payoff,
            "additional_risky_allocation": player.bantuan_sosial,
            "charge_additional_risky_allocation": player.uang_sisa_tidak_untuk_investasi,
            "consumption_risky_allocation": player.beban_konsumsi,
        })


class final_results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        results_risky_allocation = participant.vars.get(
            "results_risky_allocation", []
        )

        last_round_risky_allocation = (
            participant.vars.get("last_round_played_risky_allocation", 1)
            if participant.vars.get("end_game", False)
            else player.round_number
        )

        # Total Akhir Semua Pendapatan
        player.total_akhir_profit = sum(item["profit_risky_allocation"] for item in results_risky_allocation)
        player.total_akhir_alokasi_opsi = sum(item["cost_risky_allocation"] for item in results_risky_allocation)
        player.total_akhir_bantuan_sosial = sum(item["additional_risky_allocation"] for item in results_risky_allocation)
        player.total_akhir_beban_konsumsi = sum(item["consumption_risky_allocation"] for item in results_risky_allocation)
        player.total_akhir_uang = sum(item["endowment_risky_allocation"] for item in results_risky_allocation)

        # Menentukan Final Payment
        if player.in_round(player.round_number).payoff < 0:
            final_payment = 0
            final_round_endowment = player.in_round(player.round_number).payoff
        else:
            final_payment = player.in_round(player.round_number).payoff
            final_round_endowment = player.in_round(player.round_number).payoff

        participant.vars["summary_risky_allocation"] = {
            "profit": player.total_akhir_profit,
            "cost": player.total_akhir_alokasi_opsi,
            "additional": player.total_akhir_bantuan_sosial,
            "consumption": player.total_akhir_beban_konsumsi,
            "endowment": player.total_akhir_uang,
            "payment_selected": final_payment,
        }

        return {
            "results_risky_allocation": results_risky_allocation,
            "last_round_risky_allocation": last_round_risky_allocation,
            "final_payment": final_round_endowment,
        }

class end_session(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [endowment_information, Loading, game, single_results, final_results, end_session]
