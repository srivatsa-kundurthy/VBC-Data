import numpy as np
import matplotlib.pyplot as plt


#[1, 268,], [2, 96], [3, 421], [4, 771]

#index array
week = np.arange(1, 14)

#read file
file = open('weeklyOrderData.txt', 'r')
lorder = file.read().split('\n')

file.close()

#cast to an int

for i in range(0, len(lorder)):
    lorder[i] = int(lorder[i])

print(lorder)

nlorder = []

for i in range(len(lorder)-1):
    sum = lorder[i] + lorder[i+1]
    nlorder.append(sum)

print(nlorder)

del nlorder[1::2]
print(lorder)

nlorder = np.divide(nlorder, 10)
print(nlorder)







plt.bar(week, nlorder, width=0.2,label = 'Weeks')

plt.grid(True)
plt.title('Avg Daily Orders per 2 weeks')
plt.xlabel('Number of Grouped Weeks')
plt.ylabel('Avg. Daily Orders')




plt.show()


