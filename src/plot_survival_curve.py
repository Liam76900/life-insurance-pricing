import matplotlib.pyplot as plt
from survival_probability import survival_probability

def plot_survival_curve(tables_dict, start_age, max_age=110):
    plt.figure(figsize=(9,5))
    for label, table in tables_dict.items():
        ages = list(range(start_age, max_age))
        survival = [survival_probability(table, start_age, y - start_age) for y in ages]
        plt.plot(ages, survival, label=label)

    plt.xlabel('Age')
    plt.ylabel('Survival Probability')
    plt.title(f'Survival Probability from Age {start_age}')
    plt.legend()
    plt.savefig('outputs/survival_curve.png', dpi=150, bbox_inches='tight')
    plt.show()