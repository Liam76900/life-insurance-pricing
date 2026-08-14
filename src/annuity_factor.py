from survival_probability import survival_probability

def annuity_factor(mortality_table, start_age, r, max_age=110):
    factor = 0
    for year in range(0, max_age - start_age):
        survival = survival_probability(mortality_table, start_age, year)
        discount = (1 + r) ** (-year)
        factor += survival * discount
    return factor