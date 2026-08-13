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
from build_results_table import build_results_table

synthetic_table = load_mortality_table('mortality_table.csv')
real_table = load_mortality_table("mortality_table_real.csv")

ages = range(20, 91, 5)
payout = 100000
r=0.03

results_synthetic = build_results_table(synthetic_table, ages, payout, r)

print(results_synthetic)