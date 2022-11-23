import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')
means = [np.mean(df['charges'].sample(frac=np.random.random() * 0.9)) for _i in range(300)]
plt.hist(means, bins=10)
print(f' std: {np.std(means)},\n mean: {np.mean(means)}')
plt.show()
