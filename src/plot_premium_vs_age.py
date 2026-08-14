import matplotlib.pyplot as plt

def plot_premium_vs_age(results_dict):
    plt.figure(figsize=(9,5))
    for label, results_df in results_dict.items():
        plt.plot(results_df['age'], results_df['annual_premium'], marker='o', label=label)

    plt.xlabel('Starting Age')
    plt.ylabel('Annual Premium ($)')
    plt.title('Annual Premium vs. Starting Age')
    plt.legend()
    plt.savefig('outputs/premium_vs_age.png', dpi=150, bbox_inches='tight')
    plt.show()