import fileCleaner
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dels = fileCleaner.fileCleaner('deliveryData.txt')


dates = dels.delLines('')

"""
print(dates)

df = pd.DataFrame({'freq': dates})

df.groupby('freq', as_index=False).size().plot(kind='bar')
plt.show()
"""

df = pd.read_csv('delData.csv')
df.head()
print(df['delDates'][:175])

print(df['delDates'].value_counts())

#df['delDates'].value_counts().plot()

df['delDates'].value_counts().plot(kind='bar')

plt.tight_layout()

plt.title('Frequency of Delivery Dates')
plt.xlabel('Delivery Date')
plt.ylabel('Frequency')

plt.show()