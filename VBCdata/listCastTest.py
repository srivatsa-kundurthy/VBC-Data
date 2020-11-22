import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


series = pd.Series([10,20,30,40,50], ['A','B','C','D', 'A'])

print(series)


series = dict(series)
#print(series['A'])

k = 0
for k in series['A']:
    print(k)

d = sum(series['A'])
print(d)

#print(k)

