import logging

from app.constants import TAX_TIERS


class TaxInformation:
    
    def __init__(self, tier_level, tier_info, total_tax):
        self.tier_level = tier_level
        self.tier_info = tier_info
        self.total_tax = total_tax


class TaxCalculator:
    
    def calculate_tax(self, annual_income, bonus=0, rebates=0, donation=0):
        logging.debug("Calculating tax... | Annual: {} | Bonus: {} | Rebates: {} | Donation: {}".format(annual_income,
                                                                                                        bonus,
                                                                                                        rebates,
                                                                                                        donation))
        try:
            self._validate_input(annual_income, bonus, rebates, donation)
        except ValueError as e:
            logging.error(e)
            raise e
        
        taxable_income = annual_income + bonus - rebates - (2.5 * donation)
        total_tax = 0
        tier_level = '0'
        tier_info = TAX_TIERS['0']
        if taxable_income > 20000:
            tax_tier = list(
                filter(lambda item: item[1]['lower_limit'] < taxable_income <= item[1]['upper_limit'],
                       TAX_TIERS.items()))
            tax_tier_information = tax_tier[0]
            tier_level = tax_tier_information[0]
            tier_info = tax_tier_information[1]
            total_tax = self._get_total_tax(annual_income, tier_info)
        logging.debug("Tier: {} | Total tax: {} | Tax Info: {}".format(tier_level, total_tax, tier_info))
        result = TaxInformation(tier_level, tier_info, total_tax)
        return result
    
    def _get_total_tax(self, annual_income, tier_info):
        # Accumulated tax from previous tier + leftover * current tax rate
        return tier_info['accumulated_tax'] + ((annual_income - tier_info['lower_limit']) * tier_info['tax_rate'])
    
    def _validate_input(self, annual_income, bonus, rebates, donation):
        if annual_income < 0:
            raise ValueError("Annual income can't be negative")
        if bonus < 0:
            raise ValueError("Bonus can't be negative")
        if rebates < 0:
            raise ValueError("Tax rebates can't be negative")
        if donation < 0:
            raise ValueError("Donation can't be negative")
