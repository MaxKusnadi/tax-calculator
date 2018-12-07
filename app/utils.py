
class Utils:
    
    @staticmethod
    def get_taxable_income(annual_income, bonus, rebates, donation):
        return annual_income + bonus - rebates - (2.5 * donation)
    
    @staticmethod
    def get_annual_income(monthly_income):
        return 12 * monthly_income
