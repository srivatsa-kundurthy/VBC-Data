import pandas as pd
import matplotlib.pyplot as plt

file = open('cleanCompNames.txt', 'r')
cleanCompF = file.read().split('\n')

file2 = open('cleanCompQ.txt', 'r')
cleanCompQF = file2.read().split('\n')

for i in range(0, len(cleanCompQF)):
    cleanCompQF[i] = int(cleanCompQF[i])

dictValues = pd.Series(cleanCompQF, cleanCompF)

print(dictValues)

#Roland sum
print(sum(dictValues['Roland']))

roland = sum(dictValues['Roland'])
print('Roland: ' + str(roland))

calvin = sum(dictValues['Calvin'])
print('Calvin: ' + str(calvin))

anne = sum(dictValues['Anne'])
print('Anne: ' + str(anne))

charlene = sum(dictValues['Charlene'])
print('Charlene: ' + str(charlene))

anthony = sum(dictValues['Anthony'])
print('Anthony: ' + str(anthony))

sharon = sum(dictValues['Sharon'])
print('Sharon: ' + str(sharon))

everett = sum(dictValues['Everett'])
print('Everett: ' + str(everett))

print(calvin + anne + roland + charlene + anthony + sharon + everett)

orders = [calvin, anne, roland, charlene, anthony, sharon, everett]
names = ['Calvin', 'Anne', 'Roland', 'Charlene', 'Anthony', 'Sharon', 'Everett']


print(sum(dictValues['Roland']))

roland = sum(dictValues['Roland'])
print('Roland: ' + str(roland))

calvin = sum(dictValues['Calvin'])
print('Calvin: ' + str(calvin))

anne = sum(dictValues['Anne'])
print('Anne: ' + str(anne))

charlene = sum(dictValues['Charlene'])
print('Charlene: ' + str(charlene))

anthony = sum(dictValues['Anthony'])
print('Anthony: ' + str(anthony))

sharon = sum(dictValues['Sharon'])
print('Sharon: ' + str(sharon))

everett = sum(dictValues['Everett'])
print('Everett: ' + str(everett))



plt.bar(names, orders, width=0.2,label = 'Weeks')

plt.title('Total Orders per Company')
plt.xlabel('Company')
plt.ylabel('Total Orders')

plt.show()