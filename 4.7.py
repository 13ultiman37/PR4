import scipy.stats
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')


def mean_confidence_interval(data, confidence=0.95):
    x, se = np.mean(data), scipy.stats.sem(data)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., len(data) - 1)
    return [x - h, x + h]


means_charges = [np.mean(df['charges'].sample(frac=np.random.random())) for _i in range(300)]
means_bmi = [np.mean(df['bmi'].sample(frac=np.random.random())) for _i in range(300)]
print('==========charges==========')
print(f'95% доверительный интервал charges: {mean_confidence_interval(means_charges)}')
print(f'99% доверительный интервал charges: {mean_confidence_interval(means_charges, 0.99)}')
print('==========bmi==========')
print(f'95% доверительный интервал bmi: {mean_confidence_interval(means_bmi)}')
print(f'99% доверительный интервал bmi: {mean_confidence_interval(means_bmi, 0.99)}')
