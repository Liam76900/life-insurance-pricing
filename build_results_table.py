import pandas as pd
from life_expectancy import life_expectancy
from price_life_insurance import price_life_insurance
from annual_premium import annual_premium
from check_death_probabilities_sum import check_death_probabilities_sum

def build_results_table(mortality_table, ages, payout, r):
    results = []
    for age in ages:
        le = life_expectancy(mortality_table, age)
        lump = price_life_insurance(mortality_table, age, payout, r)
        annual = annual_premium(mortality_table, age, payout, r)
        prob_check = check_death_probabilities_sum(mortality_table, age)
        results.append({
            'age': age,
            'life_expectancy': le,
            'lump_sum_premium': lump,
            'annual_premium': annual,
            'total_death_probability': prob_check
        })
    return pd.DataFrame(results)