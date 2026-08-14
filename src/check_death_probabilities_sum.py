from probability_of_death_in_year import probability_of_death_in_year

def check_death_probabilities_sum(mortality_table, start_age, max_age=110):
    total = 0
    for year in range(1, max_age - start_age + 1):
        total += probability_of_death_in_year(mortality_table, start_age, year)
    return total