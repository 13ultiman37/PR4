import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')
df.hist(figsize=(10, 10))
plt.show()
