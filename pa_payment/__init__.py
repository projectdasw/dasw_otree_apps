from otree.api import *
import random


doc = """
Payment Page
"""


class C(BaseConstants):
    NAME_IN_URL = 'pa_payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pembayaran_akhir = models.CurrencyField(initial=0)
    sesi_terpilih = models.StringField()
    pembayaran_terpilih = models.CurrencyField(initial=0)
    uang_kehadiran = models.CurrencyField(initial=0)


class Loading(WaitPage):
    title_text = "Ruang Tunggu Eksperimen"


# PAGES
class info_sesi(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant

        # Hasil setiap ronde
        risky_purchase = participant.vars.get("results_risky_purchase", [])
        risky_allocation = participant.vars.get("results_risky_allocation", [])
        cognitive_task = participant.vars.get("results_cognitive_task", [])
        panel_allocation = participant.vars.get("results_panel_allocation", [])

        # Ringkasan akhir masing-masing app
        risky_purchase_summary = participant.vars.get(
            "summary_risky_purchase", {}
        )
        risky_allocation_summary = participant.vars.get(
            "summary_risky_allocation", {}
        )
        cognitive_task_summary = participant.vars.get(
            "summary_cognitive_task", {}
        )
        panel_allocation_summary = participant.vars.get(
            "summary_panel_allocation", {}
        )

        return dict(
            # Hasil setiap ronde
            risky_purchase=risky_purchase,
            risky_allocation=risky_allocation,
            cognitive_task=cognitive_task,
            panel_allocation=panel_allocation,

            # Jumlah ronde
            risky_purchase_rounds=len(risky_purchase),
            risky_allocation_rounds=len(risky_allocation),
            cognitive_task_rounds=len(cognitive_task),
            panel_allocation_rounds=len(panel_allocation),

            # Summary
            risky_purchase_summary=risky_purchase_summary,
            risky_allocation_summary=risky_allocation_summary,
            cognitive_task_summary=cognitive_task_summary,
            panel_allocation_summary=panel_allocation_summary,

            # Payment selected
            risky_purchase_payment_selected=risky_purchase_summary.get(
                "payment_selected", False
            ),
            risky_allocation_payment_selected=risky_allocation_summary.get(
                "payment_selected", False
            ),
            cognitive_task_payment_selected=cognitive_task_summary.get(
                "payment_selected", False
            ),
            panel_allocation_payment_selected=panel_allocation_summary.get(
                "payment_selected", False
            ),
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant

        apps = [
            ("Risky Purchase", participant.vars.get("summary_risky_purchase")),
            ("Risky Allocation", participant.vars.get("summary_risky_allocation")),
            ("Investment Panel Allocation", participant.vars.get("summary_panel_allocation")),
            ("Cognitive Task", participant.vars.get("summary_cognitive_task")),
        ]

        selected_app, summary = random.choice(apps)
        player.sesi_terpilih = selected_app
        player.pembayaran_terpilih = summary["payment_selected"]
        player.uang_kehadiran = 10000
        player.pembayaran_akhir = (player.pembayaran_terpilih * 1000) + player.uang_kehadiran


class pembayaran(Page):
    pass


class akhir_eksperimen(Page):
    pass


page_sequence = [Loading, info_sesi, pembayaran, akhir_eksperimen]
