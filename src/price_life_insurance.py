from probability_of_death_in_year import probability_of_death_in_year

def price_life_insurance(mortality_table, start_age, payout, r, max_age=110):
    total_expected_pv = 0
    for year in range(1, max_age - start_age + 1):
        prob_death_this_year = probability_of_death_in_year(mortality_table, start_age, year)
        discount_factor = (1 + r) ** (-year)
        expected_pv_this_year = prob_death_this_year * payout * discount_factor
        total_expected_pv += expected_pv_this_year
    return total_expected_pv