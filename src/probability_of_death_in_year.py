from survival_probability import survival_probability

def probability_of_death_in_year(mortality_table, start_age, year):
    survive_to_year_start = survival_probability(mortality_table, start_age, year - 1)
    qx_that_year = mortality_table.loc[mortality_table['age'] == start_age + year - 1, 'qx'].values[0]
    return survive_to_year_start * qx_that_year