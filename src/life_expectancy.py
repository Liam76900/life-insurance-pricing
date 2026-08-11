from survival_probability import survival_probability

def life_expectancy(mortality_table, start_age, max_age=110):
    expectancy = 0
    for years in range(1, max_age - start_age + 1):
        expectancy += survival_probability(mortality_table, start_age, years)
    return expectancy