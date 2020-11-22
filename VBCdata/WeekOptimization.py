from itertools import combinations
import pandas as pd

daily_production_limit = 700


file = open('lastWeekNames.txt', 'r')
vals = file.read().split('\n')



file2 = open('lastWeekQuantity.txt', 'r')
lst = file2.read().split('\n')


for i in range(0, len(lst)):
    lst[i] = int(lst[i])


ser = pd.Series(vals, lst)
dictS = dict(ser)
print(ser)
print(dictS)

print(lst)
print(vals)

prices = []
def getPrices():

    for q in lst:
        if dictS[q] == 'Calvin':
            n = q*73.14

            prices.append(n)
        if dictS[q] == 'Anne':
            n = q * 84.07

            prices.append(n)
        if dictS[q] == 'Roland':
            n = q * 109.29

            prices.append(n)
        if dictS[q] == 'Charlene':
            n = q * 100.88

            prices.append(n)
        if dictS[q] == 'Anthony':
            n = q * 70.62

            prices.append(n)
        if dictS[q] == 'Sharon':
            n = q * 75.66

            prices.append(n)
        if dictS[q] == 'Everett':
            n = q * 82.39

            prices.append(n)
    return prices

names = []
def getNames():
    for q in lst:
        if dictS[q] == 'Calvin':
            n = 'Calvin: ' + str(q)
            names.append(n)
        if dictS[q] == 'Anne':
            n = 'Anne: ' + str(q)
            names.append(n)
        if dictS[q] == 'Roland':
            n = 'Roland ' + str(q)
            names.append(n)
        if dictS[q] == 'Charlene':
            n = 'Charlene: ' + str(q)
            names.append(n)
        if dictS[q] == 'Anthony':
            n = 'Anthony: ' + str(q)
            names.append(n)
        if dictS[q] == 'Sharon':
            n = 'Sharon: ' + str(q)
            names.append(n)
        if dictS[q] == 'Everett':
            n = 'Everett: ' + str(q)
            names.append(n)

    return names



#p = getPrices()
#n = getNames()

print(getPrices())
print(getNames())





sums = []
sumPrices = []
sumNames = []
for i in range(0, len(lst)+1):
    #generate combinations
    comb = combinations(lst, i)
    combPrices = combinations(prices, i)
    combNames = combinations(names, i)
    lencomb = list(comb)
    lenP = list(combPrices)
    lenN = list(combNames)

    print(lencomb)
    print(list(comb))
    print(len(list(lencomb)))
    print(len)
    #print(lenN)


    #sums of combinations
    for j in range(0, len(lencomb)):
        s = sum(lencomb[j])
        p = sum(lenP[j])
        #n = sum(lenN[j])
        n = ' , '.join(lenN[j])

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
    if (i > daily_production_limit*5):
        #ind = sums.index(i)
        id.append(c)
        #print('yeet ' + str(i))
    c += 1
    #print(c)


print(sumPrices)

#print(id)

#print(len(id))



#delete these indeces in all lists

for i in sorted(id, reverse=True):
    del sums[i]
    del sumPrices[i]
    del sumNames[i]



print(sums)
print(sumPrices)
print(sumNames)


"""
print(len(sums))
print(len(sumPrices))
print(len(sumNames))

"""

#now have all data for elements that fit the constraint

#find maximum price

m = max(sumPrices)
print(m)

pos = sumPrices.index(m)

print('The optimal combination is: ' + str(sumNames[pos]) + '. The revenue is: ' + str(m) + '.')





