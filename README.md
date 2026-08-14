# Life Table Survival Analysis & Insurance Premium Pricing

## Introduction

This Python project calcualtes survival probabilities from mortality tables as well as prices life insurance as both lump sum and the annual equivalent premium. The tables used are a synthetic mortaility table (finding qx using the Gompertz-Makeham formula) and real U.S. SSA data split between both male and female mortality rates.

## Overview

The project includes the ability to calculate death probabilties year-by-year using mortality tables as well as the number of years more a person of a given age should be able to live up until using a sum of survival proabbilties. It also helps to calcualte the fair price of a life insurance policy today by finding the discounted future payout calculated as both lump sum and annual premium. It also helps to compare how the use of differnt types of mortaility tbales differs results, where I used both the mathematical approximation of Gompertz-Makeham as well as real U.S. Social Security Administration mortality data of both male and female.

## Explanation of Components of Project

### Obtaining the Mortality Data (Mortality Tables)

A mortality table lists all the qx (probability of dying) for each age, given oyu are alive by the start of it and this project uses two types of it:

- A synthetic table formulated by the Gompertz-Makeham formula, which is a simple mathematical approximation of qx which was used to test the code first
- Real U.S. SSA data composing of both male and female qx values form the 2021 Period Life Table

### Survival Probability

```python
def survival_probability(mortality_table, start_age, years):
    survival = 1.0
    for age in range(start_age, start_age + years):
        qx = mortality_table.loc[mortality_table['age'] == age, 'qx'].values[0]
        px = 1 - qx   # probability of SURVIVING that year
        survival *= px
    return survival
```
The yearly survival probabilties consists of taking the qx and taking it from 1 to find the survival probability of that year and compounding the survival probabilties of the years up until the final year.

### Life Expectancy

```python
from survival_probability import survival_probability

def life_expectancy(mortality_table, start_age, max_age=110):
    expectancy = 0
    for years in range(1, max_age - start_age + 1):
        expectancy += survival_probability(mortality_table, start_age, years)
    return expectancy
```
This function takes the survival probabilties of the years up until the max age from your start age and takes the sum of them, which in turn returns the life expectancy.

### Probability of Death in a Specific Year

```python
from survival_probability import survival_probability

def probability_of_death_in_year(mortality_table, start_age, year):
    survive_to_year_start = survival_probability(mortality_table, start_age, year - 1)
    qx_that_year = mortality_table.loc[mortality_table['age'] == start_age + year - 1, 'qx'].values[0]
    return survive_to_year_start * qx_that_year
```
The insurance payout happens in one specific year so the prining needs the probability needs the probability of death in a speicifc year, which is what this function finds by checking the survival of every previous year and then dying in the speciifc year being checked:

### Pricing the Policy
```python
from probability_of_death_in_year import probability_of_death_in_year

def price_life_insurance(mortality_table, start_age, payout, r, max_age=110):
    total_expected_pv = 0
    for year in range(1, max_age - start_age + 1):
        prob_death_this_year = probability_of_death_in_year(mortality_table, start_age, year)
        discount_factor = (1 + r) ** (-year)
        expected_pv_this_year = prob_death_this_year * payout * discount_factor
        total_expected_pv += expected_pv_this_year
    return total_expected_pv
```
For every possible future year this function multiplies the death in year probability to the payout for that year, discounts it to today's value and sums all the payouts and returns its fair lump-sum price

### Annual Premium

```python
from survival_probability import survival_probability

def annuity_factor(mortality_table, start_age, r, max_age=110):
    factor = 0
    for year in range(0, max_age - start_age):
        survival = survival_probability(mortality_table, start_age, year)
        discount = (1 + r) ** (-year)
        factor += survival * discount
    return factor
```
```python
from price_life_insurance import price_life_insurance
from annuity_factor import annuity_factor

def annual_premium(mortality_table, start_age, payout, r, max_age=110):
    lump_sum = price_life_insurance(mortality_table, start_age, payout, r, max_age)
    factor = annuity_factor(mortality_table, start_age, r, max_age)
    return lump_sum / factor
```
The lump-sum value is a pretty large number compared to the monthly/annual premiums that is most regularly seen. So to convert it we first use a function to formulate the annuity factor to do so. Where the value of a hypothetical $1, paid every year the person is alive, is discounted to the present value. Then dividing the lump sum by the annuity factor gives the equivalent annual premium.

### Validating the Model
```python
from probability_of_death_in_year import probability_of_death_in_year

def check_death_probabilities_sum(mortality_table, start_age, max_age=110):
    total = 0
    for year in range(1, max_age - start_age + 1):
        total += probability_of_death_in_year(mortality_table, start_age, year)
    return total
```
As the policyholder will certainly die at some point or another before the table's maximum age, so summing the probability of death in every year should land really close to 1.0 if the model is working properly.

## Features

### Life Table Mechanics

- Calculates survival probabilities
- Calculates life expectancy at any starting age
- Probability of death in a specific future year

### Data Sources

- Synthetic mortality table (Gompertz-Makeham approximation)
- Real mortality data (U.S. SSA 2021 Period Life Table - Male and Female)

### Validation

- Death probability check (total should be ~1.0)
- Life expectancy crossed-checked against SSA's own published figures

### Visualisations

- Survival probability curve (synthetic vs. male vs. female)
- Probability of death by year (synthetic vs. male vs. female)
- Annual premium vs. starting age (synthetic vs. male vs. female)

## Project Structure

life-insurance-pricing/
├── src/
│   ├── load_mortality_table.py
│   ├── survival_probability.py
│   ├── life_expectancy.py
│   ├── probability_of_death_in_year.py
│   ├── price_life_insurance.py
│   ├── annuity_factor.py
│   ├── annual_premium.py
│   ├── check_death_probabilities_sum.py
│   ├── build_results_table.py
│   ├── plot_survival_curve.py
│   ├── plot_death_probability_by_year.py
│   └── plot_premium_vs_age.py
├── outputs/
│   ├── survival_curve.png
│   ├── death_probability_by_year.png
│   └── premium_vs_age.png
├── synthetic_table.py
├── real_table_male.py
├── real_table_female.py
├── mortality_table.csv
├── mortality_table_real_male.csv
├── mortality_table_real_female.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation
```bash
git clone https://github.com/yourusername/life-insurance-pricing.git
cd life-insurance-pricing
pip install -r requirements.txt
```

## Usage
```bash
python build_synthetic_table.py
python build_real_table_male.py
python build_real_table_female.py
python main.py
```
## Validation & Results

![Survival Curve](outputs/survival_curve.png)



![Death Probability by Year](outputs/death_probability_by_year.png)



![Annual Premium vs Age](outputs/premium_vs_age.png)

