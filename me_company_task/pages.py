from .models import *
import random
import json


class game(Page):
    form_model = 'player'
    form_fields = ['prospek_terpilih', 'kontribusi_persen']

    def _kontribusi_max_persen(self):
        rd = Constants.rounds_data[self.round_number - 1]
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )
        if treatment == 'by_return':
            return 100
        # By capitalisation: kontribusi dibatasi agar tidak melebihi sisa modal
        # (cc_inv), supaya hasil akhir tidak pernah negatif.
        return int(rd['cc_inv'] / rd['capital'] * 100)

    def error_message(self, values):
        if not values.get('prospek_terpilih'):
            return "Silakan pilih salah satu prospek investasi."
        if values.get('kontribusi_persen') is None:
            return "Silakan masukkan persentase kontribusi (0-100)."
        max_persen = self._kontribusi_max_persen()
        if values['kontribusi_persen'] > max_persen:
            return f"Kontribusi maksimal untuk ronde ini adalah {max_persen}%."

    def vars_for_template(self):
        rd = Constants.rounds_data[self.round_number - 1]
        is_ambiguity = rd['round_type'] == 'ambiguity'
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )

        if is_ambiguity:
            display_prob_a1 = f"minimal {int(rd['prob_a1'] * 100)}%"
            display_prob_a2 = "belum diketahui sama sekali"
            display_prob_b1 = f"minimal {int(rd['prob_b1'] * 100)}%"
            display_prob_b2 = "belum diketahui sama sekali"
            display_prob_damage = f"maksimal {int(rd['prob_damage'] * 100)}%"
        else:
            display_prob_a1 = f"{int(rd['prob_a1'] * 100)}%"
            display_prob_a2 = f"{int(rd['prob_a2'] * 100)}%"
            display_prob_b1 = f"{int(rd['prob_b1'] * 100)}%"
            display_prob_b2 = f"{int(rd['prob_b2'] * 100)}%"
            display_prob_damage = f"{int(rd['prob_damage'] * 100)}%"

        def fmt_mult(v):
            if v == int(v):
                return str(int(v))
            return str(v).replace('.', ',')

        ret_a1_display = fmt_mult(rd['ret_a1'])
        ret_a2_display = f"{int(rd['ret_a2'] * 100)}%"
        ret_b1_display = fmt_mult(rd['ret_b1'])
        ret_b2_display = f"{int(rd['ret_b2'] * 100)}%"

        if not is_ambiguity:
            a_chart = dict(
                labels=[
                    f"{ret_a1_display}x lipat (prob {display_prob_a1})",
                    f"{ret_a2_display} (prob {display_prob_a2})",
                ],
                data=[int(rd['prob_a1'] * 100), int(rd['prob_a2'] * 100)],
            )
            b_chart = dict(
                labels=[
                    f"{ret_b1_display}x lipat (prob {display_prob_b1})",
                    f"{ret_b2_display} (prob {display_prob_b2})",
                ],
                data=[int(rd['prob_b1'] * 100), int(rd['prob_b2'] * 100)],
            )
        else:
            a_chart = None
            b_chart = None

        damage_value = rd['damage_multiplier'] * rd['investasi']

        kontribusi_max_persen = self._kontribusi_max_persen()

        if treatment == 'by_return':
            kontribusi_text = "dari nilai return yang diperoleh jika tidak terjadi kerusakan lingkungan"
            kontribusi_cap_note = None
        else:
            kontribusi_text = "dari nilai kapitalisasi perusahaan Anda, terlepas dari ada atau tidaknya kerusakan lingkungan"
            kontribusi_cap_note = (
                f"Kontribusi dibatasi maksimal {kontribusi_max_persen}% pada ronde ini, "
                f"agar kontribusi yang dikurangkan dari hasil akhir Anda tidak melebihi sisa modal perusahaan."
            )

        min_prob_a1_pct = int(rd['prob_a1'] * 100)
        min_prob_b1_pct = int(rd['prob_b1'] * 100)

        return dict(
            round_type=rd['round_type'],
            range_type=rd['range_type'],
            capital=rd['capital'],
            investasi=rd['investasi'],
            cc_inv=rd['cc_inv'],
            ret_a1=ret_a1_display,
            ret_a2=ret_a2_display,
            ret_b1=ret_b1_display,
            ret_b2=ret_b2_display,
            display_prob_a1=display_prob_a1,
            display_prob_a2=display_prob_a2,
            display_prob_b1=display_prob_b1,
            display_prob_b2=display_prob_b2,
            display_prob_damage=display_prob_damage,
            damage_value=damage_value,
            damage_multiplier=rd['damage_multiplier'],
            is_ambiguity=is_ambiguity,
            a_chart_json=json.dumps(a_chart) if a_chart else 'null',
            b_chart_json=json.dumps(b_chart) if b_chart else 'null',
            treatment=treatment,
            kontribusi_text=kontribusi_text,
            kontribusi_max_persen=kontribusi_max_persen,
            kontribusi_cap_note=kontribusi_cap_note,
            min_prob_a1_pct=min_prob_a1_pct,
            min_prob_b1_pct=min_prob_b1_pct,
        )

    def before_next_page(self):
        rd = Constants.rounds_data[self.round_number - 1]
        is_ambiguity = rd['round_type'] == 'ambiguity'
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )

        # Simpan treatment ke field agar muncul di CSV export
        self.player.treatment = treatment

        if is_ambiguity:
            prob_a1 = self.player.actual_prob_a1
            prob_a2 = self.player.actual_prob_a2
            prob_b1 = self.player.actual_prob_b1
            prob_b2 = self.player.actual_prob_b2
            prob_damage = self.player.actual_prob_damage
        else:
            prob_a1 = rd['prob_a1']
            prob_a2 = rd['prob_a2']
            prob_b1 = rd['prob_b1']
            prob_b2 = rd['prob_b2']
            prob_damage = rd['prob_damage']
            # Isi actual_prob_* untuk risk rounds agar tidak kosong (0) di CSV
            self.player.actual_prob_a1 = prob_a1
            self.player.actual_prob_a2 = prob_a2
            self.player.actual_prob_b1 = prob_b1
            self.player.actual_prob_b2 = prob_b2
            self.player.actual_prob_damage = prob_damage

        # Tentukan return
        self.player.angka_keluar = random.randint(1, 10000)
        if self.player.prospek_terpilih == 'prospek-A':
            threshold = int(prob_a1 * 10000)
            self.player.return_multiplier = rd['ret_a1'] if self.player.angka_keluar <= threshold else rd['ret_a2']
        else:
            threshold = int(prob_b1 * 10000)
            self.player.return_multiplier = rd['ret_b1'] if self.player.angka_keluar <= threshold else rd['ret_b2']

        self.player.return_token = int(self.player.return_multiplier * rd['investasi'])

        # Cek bencana
        self.player.angka_damage = random.randint(1, 10000)
        self.player.bencana_terjadi = self.player.angka_damage <= int(prob_damage * 10000)

        cc_inv = rd['cc_inv']

        if self.player.bencana_terjadi:
            # Bencana: tidak dapat return, hanya sisa modal (cc_inv)
            self.player.return_token = 0

        # Kontribusi dihitung dari return (by_return) atau dari kapitalisasi
        # (by_capitalisation, terlepas dari ada/tidaknya bencana), dan selalu
        # mengurangi hasil akhir.
        if treatment == 'by_return':
            self.player.kontribusi_token = int(
                self.player.kontribusi_persen / 100 * self.player.return_token
            )
        else:
            self.player.kontribusi_token = int(
                self.player.kontribusi_persen / 100 * rd['capital']
            )

        self.player.hasil_token = cc_inv + self.player.return_token - self.player.kontribusi_token


class result(Page):
    def vars_for_template(self):
        rd = Constants.rounds_data[self.round_number - 1]
        is_ambiguity = rd['round_type'] == 'ambiguity'
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )

        if is_ambiguity:
            actual_prob_a1_pct = round(self.player.actual_prob_a1 * 100, 1)
            actual_prob_a2_pct = round(self.player.actual_prob_a2 * 100, 1)
            actual_prob_b1_pct = round(self.player.actual_prob_b1 * 100, 1)
            actual_prob_b2_pct = round(self.player.actual_prob_b2 * 100, 1)
            actual_prob_damage_pct = round(self.player.actual_prob_damage * 100, 2)
        else:
            actual_prob_a1_pct = int(rd['prob_a1'] * 100)
            actual_prob_a2_pct = int(rd['prob_a2'] * 100)
            actual_prob_b1_pct = int(rd['prob_b1'] * 100)
            actual_prob_b2_pct = int(rd['prob_b2'] * 100)
            actual_prob_damage_pct = int(rd['prob_damage'] * 100)

        def fmt_mult(v):
            if v == int(v):
                return str(int(v))
            return str(v).replace('.', ',')

        ret_a1 = fmt_mult(rd['ret_a1'])
        ret_a2 = f"{int(rd['ret_a2'] * 100)}%"
        ret_b1 = fmt_mult(rd['ret_b1'])
        ret_b2 = f"{int(rd['ret_b2'] * 100)}%"

        rm = self.player.return_multiplier
        if self.player.prospek_terpilih == 'prospek-A':
            is_outcome1 = (rm == rd['ret_a1'])
        else:
            is_outcome1 = (rm == rd['ret_b1'])
        return_mult = fmt_mult(rm) + 'x lipat' if is_outcome1 else f"{int(rm * 100)}%"

        return dict(
            round_type=rd['round_type'],
            range_type=rd['range_type'],
            capital=rd['capital'],
            investasi=rd['investasi'],
            cc_inv=rd['cc_inv'],
            ret_a1=ret_a1,
            ret_a2=ret_a2,
            ret_b1=ret_b1,
            ret_b2=ret_b2,
            actual_prob_a1_pct=actual_prob_a1_pct,
            actual_prob_a2_pct=actual_prob_a2_pct,
            actual_prob_b1_pct=actual_prob_b1_pct,
            actual_prob_b2_pct=actual_prob_b2_pct,
            actual_prob_damage_pct=actual_prob_damage_pct,
            damage_value=rd['damage_multiplier'] * rd['investasi'],
            is_ambiguity=is_ambiguity,
            treatment=treatment,
            return_mult=return_mult,
        )


page_sequence = [game, result]
