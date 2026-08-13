import matplotlib.pyplot as plt

from probability_of_death_in_year import probability_of_death_in_year

def plot_death_probability_by_year(tables_dict, start_age, max_age=110):
    plt.figure(figsize=(9,5))
    for label, table in tables_dict.items():
        years = list(range(1, max_age - start_age + 1))
        probs = [probability_of_death_in_year(table, start_age, y) for y in years]
        plt.plot(years, probs, label=label)

    plt.xlabel('Years from Now')
    plt.ylabel('Probability of Death in That Year')
    plt.title(f'Probability of Death by Year (Starting Age {start_age})')
    plt.legend()
    plt.savefig('outputs/death_probability_by_year.png', dpi=150, bbox_inches='tight')
    plt.show()