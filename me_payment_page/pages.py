from .models import *
import random


class info_all_round(Page):
    def vars_for_template(self):
        treatment = self.participant.vars.get(
            'treatment', self.session.config.get('treatment', 'by_return')
        )

        # RISK TASK
        risk_players = []
        for p in self.participant.get_players():
            if p.__module__.startswith('me_risk_task'):
                risk_players.append(p)

        risk_data = []
        total_risk = 0
        for p in risk_players:
            risk_data.append({
                'round_number': p.round_number,
                'choice': 'Prospek A' if p.prospek_terpilih == 'prospek-A' else 'Prospek B',
                'payoff': p.hasil_token,
            })
            total_risk += p.hasil_token

        # AMBIGUITY TASK
        ambiguity_players = []
        for p in self.participant.get_players():
            if p.__module__.startswith('me_ambiguity_task'):
                ambiguity_players.append(p)

        ambiguity_data = []
        total_ambiguity = 0
        for p in ambiguity_players:
            ambiguity_data.append({
                'round_number': p.round_number,
                'choice':
                    'Prospek A (Kotak Biru)' if p.prospek_terpilih == 'prospek-A' else 'Prospek B (Kotak Merah/Kuning)',
                'drawn_color': p.bola_keluar,
                'payoff': p.hasil_token,
            })
            total_ambiguity += p.hasil_token

        # COMPANY TASK
        company_players = []
        for p in self.participant.get_players():
            if p.__module__.startswith('me_company_task'):
                company_players.append(p)

        company_data = []
        total_company = 0
        for p in company_players:
            company_data.append({
                'round_number': p.round_number,
                'choice': 'Prospek A' if p.prospek_terpilih == 'prospek-A' else 'Prospek B',
                'bencana': p.bencana_terjadi,
                'return_token': p.return_token,
                'kontribusi_persen': p.kontribusi_persen,
                'kontribusi_token': p.kontribusi_token,
                'payoff': p.hasil_token,
            })
            total_company += p.hasil_token

        return dict(
            ambiguity_data=sorted(ambiguity_data, key=lambda x: x['round_number']),
            risk_data=sorted(risk_data, key=lambda x: x['round_number']),
            company_data=sorted(company_data, key=lambda x: x['round_number']),
            total_ambiguity=total_ambiguity,
            total_risk=total_risk,
            total_company=total_company,
            treatment=treatment,
        )


class get_payment(Page):
    def vars_for_template(self):
        if self.player.field_maybe_none('chosen_risk_round') is None:
            risk_players = [p for p in self.participant.get_players()
                            if p.__module__.startswith('me_risk_task')]
            ambiguity_players = [p for p in self.participant.get_players()
                                 if p.__module__.startswith('me_ambiguity_task')]
            all_company = [p for p in self.participant.get_players()
                           if p.__module__.startswith('me_company_task')]

            risk_chosen = random.choice(risk_players)
            ambiguity_chosen = random.choice(ambiguity_players)

            # Pick 1 random round from company task (20 rounds, single treatment)
            company_chosen = random.choice(all_company)
            self.player.company_return_payoff = company_chosen.hasil_token
            self.player.company_cap_payoff = 0
            self.player.chosen_company_return_round = company_chosen.round_number
            self.player.chosen_company_cap_round = company_chosen.round_number

            self.player.chosen_risk_round = risk_chosen.round_number
            self.player.chosen_ambiguity_round = ambiguity_chosen.round_number
            self.player.risk_payoff = risk_chosen.hasil_token
            self.player.ambiguity_payoff = ambiguity_chosen.hasil_token
            self.player.company_payoff = (self.player.company_return_payoff +
                                          self.player.company_cap_payoff)
            self.player.total_token = (risk_chosen.hasil_token +
                                       ambiguity_chosen.hasil_token +
                                       self.player.company_payoff)
            self.player.total_payment = self.player.total_token + 20000

        participation_fee = 20000

        return dict(
            chosen_risk_round=self.player.chosen_risk_round,
            chosen_ambiguity_round=self.player.chosen_ambiguity_round,
            chosen_company_return_round=self.player.chosen_company_return_round,
            chosen_company_cap_round=self.player.chosen_company_cap_round,
            risk_payoff=self.player.risk_payoff,
            ambiguity_payoff=self.player.ambiguity_payoff,
            company_return_payoff=self.player.company_return_payoff,
            company_cap_payoff=self.player.company_cap_payoff,
            company_payoff=self.player.company_payoff,
            total_token=self.player.total_token,
            participation_fee=participation_fee,
            total_payment=self.player.total_token + participation_fee,
        )


class result(Page):
    def vars_for_template(self):
        participation_fee = 20000

        return dict(
            chosen_risk_round=self.player.chosen_risk_round,
            chosen_ambiguity_round=self.player.chosen_ambiguity_round,
            chosen_company_return_round=self.player.chosen_company_return_round,
            chosen_company_cap_round=self.player.chosen_company_cap_round,
            risk_payoff=self.player.risk_payoff,
            ambiguity_payoff=self.player.ambiguity_payoff,
            company_return_payoff=self.player.company_return_payoff,
            company_cap_payoff=self.player.company_cap_payoff,
            company_payoff=self.player.company_payoff,
            total_token=self.player.total_token,
            participation_fee=participation_fee,
            total_payment=self.player.total_token + participation_fee,
        )


page_sequence = [
    info_all_round,
    get_payment,
    result
]
