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

rCalvin = calvin * 73.14
rAnne = anne * 84.07
rRoland = roland * 109.29
rCharlene = charlene * 100.88
rAnthony = 70.62 * anthony
rSharon = sharon * 75.66
rEverett = everett * 82.39

print('Calvin:' + str(rCalvin))

print('Anne:' + str(rAnne))

print('Roland:' + str(rRoland))

print('Charlene:' + str(rCharlene))

print('Anthony:' + str(rAnthony))

print('Sharon:' + str(rSharon))

print('Everett:' + str(rEverett))

revenues = [rCalvin, rAnne, rRoland, rCharlene, rAnthony, rSharon, rEverett]
names = ['Calvin', 'Anne', 'Roland', 'Charlene', 'Anthony', 'Sharon', 'Everett']



plt.bar(names, revenues, width=0.2,label = 'Weeks')

plt.grid(True)
plt.title('Total Revenue Potential per Company')
plt.xlabel('Company')
plt.ylabel('Total Revenue Potential')

plt.show()