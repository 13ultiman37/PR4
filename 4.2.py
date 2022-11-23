import pandas as pd
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')
print(df.describe())
