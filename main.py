import matplotlib.pyplot as plt

import sys
sys.path.append('src')

from load_mortality_table import load_mortality_table
from survival_probability import survival_probability
from life_expectancy import life_expectancy
from probability_of_death_in_year import probability_of_death_in_year
from price_life_insurance import price_life_insurance

mortality_table = load_mortality_table('mortality_table.csv')

start_age = 30
payout = 100000
r = 0.03

life_expectancy = life_expectancy(mortality_table, start_age)
price = price_life_insurance(mortality_table, start_age, payout, r)

print(f"Life expectancy from age {start_age}: {life_expectancy:.2f} years")
print(f"Fair premium: {price:.2f}")

for age in [30, 50, 70]:
    p = price_life_insurance(mortality_table, age, payout, r)
    print(f"Age {age}: Fair premium = {p:.2f}")