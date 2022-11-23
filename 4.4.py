import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

df = pd.read_csv('insurance.csv')
plt.figure(figsize=(8, 4))
columns = ['bmi', 'charges']
for i, column in enumerate(columns):
    df1 = df[column]
    plt.subplot(1, 2, i + 1)
    mean1 = df1.mean()
    moda1 = df1.mode().values[0]
    med1 = df1.median()
    print('==========' + column + '==========')
    print('Среднее:', mean1)
    print('Мода: ', moda1)
    print('Медиана: ', med1)
    df1.hist(legend=True)
    plt.axvline(x=mean1, color='r', label='mean')
    plt.axvline(x=moda1, color='b', label='moda')
    plt.axvline(x=med1, color='pink', label='med')
    plt.legend()

plt.show()
