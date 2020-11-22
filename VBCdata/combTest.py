import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import pandas as pd

lst = [1,2,3,4,5,6]
vals = ['a','b','a','c','b','a']

ser = pd.Series(vals, lst)
dictS = dict(ser)
print(ser)
print(dictS)

prices = []
def getPrices():

    for q in lst:
        if dictS[q] == 'a':
            n = q*2
            prices.append(n)
        if dictS[q] == 'b':
            n = q * 4
            prices.append(n)
        if dictS[q] == 'c':
            n = q * 3
            prices.append(n)
    return prices

names = []
def getNames():
    for q in lst:
        if dictS[q] == 'a':
            n = 'a ' + str(q)
            names.append(n)
        if dictS[q] == 'b':
            n = 'b ' + str(q)
            names.append(n)
        if dictS[q] == 'c':
            n = 'c ' + str(q)
            names.append(n)

    return names





print(getPrices())
print(getNames())





sums = []
sumPrices = []
sumNames = []
for i in range(2, (len(lst))+1):
    #generate combinations
    comb = combinations(lst,i)
    combPrices = combinations(getPrices(), i)
    combNames = combinations(getNames(), i)
    lencomb = list(comb)
    lenP = list(combPrices)
    lenN = list(combNames)
    #print(lencomb)
    #print(list(comb))
    #print(len(list(lencomb)))
    #print(lenN)

    #sums of combinations
    for j in range(0, len(lencomb)):
        s = sum(lencomb[j])
        p = sum(lenP[j])
        #n = sum(lenN[j])
        n = ' , '.join(lenN[j])
        print(s)
        sums.append(s)
        sumPrices.append(p)
        sumNames.append(n)

print(sums)
print(sumPrices)
print(sumNames)
print(len(sums))
print(len(sumPrices))




id = []

#find combinations not meeting condition
c = 0
for i in sums:
    if (i > 10):
        #ind = sums.index(i)
        id.append(c)
        #print('yeet ' + str(i))
    c += 1
    #print(c)




print(id)

print(len(id))



#delete these indeces in all lists

for i in sorted(id, reverse=True):
    del sums[i]
    del sumPrices[i]
    del sumNames[i]

print(sums)
print(sumPrices)
print(sumNames)

print(len(sums))
print(len(sumPrices))
print(len(sumNames))

#now have all data for elements that fit the constraint

#find maximum price

m = max(sumPrices)
print(m)

pos = sumPrices.index(m)

print('The optimal combination is: ' + str(sumNames[pos]) + '. The revenue is: ' + str(m) + '.')
