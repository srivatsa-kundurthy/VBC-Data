import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('delData.csv')
df.head()

print(df.shape)

print(df['compOrders'][:176])


print(df['compOrders'].value_counts())

#df['delDates'].value_counts().plot()

df['compOrders'].value_counts().plot(kind='bar')

plt.tight_layout()

plt.title('Frequency of Company Orders')
plt.xlabel('Company')
plt.ylabel('Frequency')

plt.show()

