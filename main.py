import matplotlib.pyplot as plt

import sys
sys.path.append('src')

from load_mortality_table import load_mortality_table
from survival_probability import survival_probability
from life_expectancy import life_expectancy
from probability_of_death_in_year import probability_of_death_in_year
from price_life_insurance import price_life_insurance
from annuity_factor import annuity_factor
from annual_premium import annual_premium
from check_death_probabilities_sum import check_death_probabilities_sum

mortality_table = load_mortality_table('mortality_table.csv')

start_age = 30
payout = 100000
r = 0.03

l_e = life_expectancy(mortality_table, start_age)
lump_sum = price_life_insurance(mortality_table, start_age, payout, r)
annual = annual_premium(mortality_table, start_age, payout, r)
total_prob = check_death_probabilities_sum(mortality_table, start_age)

print(mortality_table[mortality_table['age'].isin([30, 40, 50, 60, 70, 80, 90, 100])])

print(f"Life expectancy from age {start_age}: {l_e:.2f} years")
print(f"Lump sum premium: {lump_sum:.2f}")
print(f"Annual premium: {annual:.2f}")
print(f"\nSanity check — total death probability (should be ~1.0): {total_prob:.4f}")

print("\nPremium by age:")
for age in [30, 50, 70]:
    p_lump = price_life_insurance(mortality_table, age, payout, r)
    p_annual = annual_premium(mortality_table, age, payout, r)
    print(f"Age {age}: Lump sum = {p_lump:.2f}, Annual = {p_annual:.2f}")