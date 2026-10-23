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

        # Tentukan bola yang ditampilkan (sebelum memilih)
        if round_data['procedure'] == 'ellsberg':
            display_balls = dict(red=30, yellow=0, blue=0, grey=70)
        elif round_data['procedure'] == 'partial':
            display_balls = dict(red=10, yellow=10, blue=10, grey=70)
        else:  # unknown
            display_balls = dict(red=0, yellow=0, blue=0, grey=100)

        return dict(
            round_data=round_data,
            choice_type=round_data['choice_type'],
            info_text=round_data['info_text'],
            display_balls_json=json.dumps(display_balls),
        )

    def before_next_page(self):
        # Buat pool bola berdasarkan komposisi sebenarnya, lalu undi 1
        pool = []
        pool.extend(['Merah'] * self.player.comp_red)
        pool.extend(['Kuning'] * self.player.comp_yellow)
        pool.extend(['Biru'] * self.player.comp_blue)

        self.player.bola_keluar = random.choice(pool)

        # Tentukan menang/kalah
        round_data = Constants.rounds_data[self.round_number - 1]
        chosen = self.player.prospek_terpilih
        drawn = self.player.bola_keluar

        if round_data['choice_type'] == 'single':
            # Peserta pilih 1 warna — menang jika warna yang keluar = pilihan
            if drawn == chosen:
                self.player.hasil_token = Constants.payoff_win
            else:
                self.player.hasil_token = 0
        else:
            # Peserta pilih kombinasi 2 warna
            if chosen == 'merah-kuning':
                if drawn in ['Merah', 'Kuning']:
                    self.player.hasil_token = Constants.payoff_win
                else:
                    self.player.hasil_token = 0
            elif chosen == 'biru-kuning':
                if drawn in ['Biru', 'Kuning']:
                    self.player.hasil_token = Constants.payoff_win
                else:
                    self.player.hasil_token = 0


class result(Page):
    def vars_for_template(self):
        round_data = Constants.rounds_data[self.round_number - 1]

        # Label pilihan peserta (human-readable)
        chosen = self.player.prospek_terpilih
        if round_data['choice_type'] == 'single':
            chosen_display = f"Kotak {chosen}"
        else:
            if chosen == 'merah-kuning':
                chosen_display = "Kotak Merah atau Kuning"
            else:
                chosen_display = "Kotak Biru atau Kuning"

        # CSS class untuk warna bola yang keluar
        color_css_map = {'Merah': 'red', 'Kuning': 'yellow', 'Biru': 'blue'}
        color_text_map = {'Merah': 'text-danger', 'Kuning': 'text-warning', 'Biru': 'text-primary'}

        return dict(
            win=self.player.hasil_token > 0,
            chosen_display=chosen_display,
            drawn_color=self.player.bola_keluar,
            drawn_color_css=color_css_map[self.player.bola_keluar],
            drawn_color_text=color_text_map[self.player.bola_keluar],
            comp_json=json.dumps(dict(
                red=self.player.comp_red,
                yellow=self.player.comp_yellow,
                blue=self.player.comp_blue,
            )),
        )


page_sequence = [game, result]
