def survival_probability(mortality_table, start_age, years):
    survival = 1.0
    for age in range(start_age, start_age + years):
        qx = mortality_table.loc[mortality_table['age'] == age, 'qx'].values[0]
        px = 1 - qx   # probability of SURVIVING that year
        survival *= px
    return survival