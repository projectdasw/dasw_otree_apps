from .models import *
import random
import json


class game(Page):
    form_model = 'player'
    form_fields = ['prospek_terpilih']

    def error_message(self, values):
        if not values.get('prospek_terpilih'):
            return "Silakan pilih salah satu prospek."

    def vars_for_template(self):
        round_data = Constants.rounds_data[self.round_number - 1]

        # Format outcomes untuk display di template
        a_display = []
        for payoff, prob in round_data['a_outcomes']:
            a_display.append(dict(
                payoff=payoff,
                prob=prob,
                prob_pct=int(prob * 100),
            ))

        b_display = []
        for payoff, prob in round_data['b_outcomes']:
            b_display.append(dict(
                payoff=payoff,
                prob=prob,
                prob_pct=int(prob * 100),
            ))

        # Data untuk Chart.js (JSON) — warna urutan: hijau, kuning, merah
        chart_colors = ['#28a745', '#dc3545', '#ffc107']
        a_chart = dict(
            labels=[f"{o['payoff']} token ({o['prob_pct']}%)" for o in a_display],
            data=[o['prob_pct'] for o in a_display],
            colors=chart_colors[:len(a_display)],
        )
        b_chart = dict(
            labels=[f"{o['payoff']} token ({o['prob_pct']}%)" for o in b_display],
            data=[o['prob_pct'] for o in b_display],
            colors=chart_colors[:len(b_display)],
        )

        return dict(
            a_outcomes=a_display,
            b_outcomes=b_display,
            a_chart_json=json.dumps(a_chart),
            b_chart_json=json.dumps(b_chart),
        )

    def before_next_page(self):
        round_data = Constants.rounds_data[self.round_number - 1]

        # Undian angka 1-100
        self.player.angka_keluar = random.randint(1, 100)

        # Tentukan outcomes berdasarkan prospek yang dipilih
        if self.player.prospek_terpilih == 'prospek-A':
            outcomes = round_data['a_outcomes']
        else:
            outcomes = round_data['b_outcomes']

        # Hitung hasil berdasarkan angka yang keluar
        cumulative = 0
        for payoff, prob in outcomes:
            cumulative += int(prob * 100)
            if self.player.angka_keluar <= cumulative:
                self.player.hasil_token = payoff
                break


class result(Page):
    def vars_for_template(self):
        round_data = Constants.rounds_data[self.round_number - 1]

        # Buat penjelasan range angka untuk setiap outcome
        if self.player.prospek_terpilih == 'prospek-A':
            outcomes = round_data['a_outcomes']
        else:
            outcomes = round_data['b_outcomes']

        ranges = []
        start = 1
        for payoff, prob in outcomes:
            end = start + int(prob * 100) - 1
            if end >= start:
                ranges.append(dict(
                    start=start,
                    end=end,
                    payoff=payoff,
                ))
            start = end + 1

        return dict(
            outcome_ranges=ranges,
        )


class jeda_ambiguity(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return dict()


page_sequence = [
    game, result, jeda_ambiguity
]
