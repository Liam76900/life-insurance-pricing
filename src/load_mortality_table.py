import pandas as pd

def load_mortality_table(filepath):
    mortality_table = pd.read_csv(filepath)   # <- this is a variable, not the function name
    return mortality_table