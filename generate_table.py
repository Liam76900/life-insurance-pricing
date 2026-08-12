import numpy as np
import pandas as pd

ages = np.arange(0, 111)
A = 0.0001
B = 0.00005
c = 1.085

qx = A + B * (c ** ages)
qx = np.clip(qx, 0, 1)

mortality_table = pd.DataFrame({'age': ages, 'qx': qx})
mortality_table.to_csv('mortality_table.csv', index=False)