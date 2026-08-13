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
from plot_survival_curve import plot_survival_curve
from plot_death_probability_by_year import plot_death_probability_by_year

synthetic_table = load_mortality_table("mortality_table.csv")
real_table_male = load_mortality_table("mortality_table_real_male.csv")
real_table_female = load_mortality_table("mortality_table_real_female.csv")

ages = range(20, 91, 5)
payout = 100000
r=0.03

results_synthetic = build_results_table(synthetic_table, ages, payout, r)
results_real_male = build_results_table(real_table_male, ages, payout, r)
results_real_female = build_results_table(real_table_female, ages, payout, r)

tables_dict = {
    'Synthetic': synthetic_table,
    'Real (Male)': real_table_male,
    'Real (Female)': real_table_female
}

print("Synthetic Results Table:")
print(results_synthetic)

print("Real Results Table (Male):")
print(results_real_male)

print("Real Results Table (Female):")
print(results_real_female)

plot_survival_curve(tables_dict, start_age=30)
plot_death_probability_by_year(tables_dict, start_age=30)