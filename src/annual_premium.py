from price_life_insurance import price_life_insurance
from annuity_factor import annuity_factor

def annual_premium(mortality_table, start_age, payout, r, max_age=110):
    lump_sum = price_life_insurance(mortality_table, start_age, payout, r, max_age)
    factor = annuity_factor(mortality_table, start_age, r, max_age)
    return lump_sum / factor