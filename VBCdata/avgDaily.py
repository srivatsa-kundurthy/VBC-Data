import numpy as np
import matplotlib.pyplot as plt


#[1, 268,], [2, 96], [3, 421], [4, 771]

week = np.arange(1, 27)

file = open('weeklyOrderData.txt', 'r')
lorder = file.read().split('\n')

file.close()

for i in range(0, len(lorder)):
    lorder[i] = int(lorder[i])

print(lorder)

lorder = np.array(lorder)
lorder = np.divide(lorder, 5)
print(lorder)



#orders = (268,96,421,771,529,596,910,1315,780,748,2212,1890,1885,2007,2794,1968,1084,2405,2816, 1979, 2610, 3980)





plt.bar(week, lorder, width=0.2,label = 'Weeks')

plt.grid(True)
plt.title('Avg Daily Orders per week')
plt.xlabel('Number of Weeks')
plt.ylabel('Avg. Daily Orders')




plt.show()


