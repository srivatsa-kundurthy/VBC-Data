import numpy as np
import matplotlib.pyplot as plt




#index array
week = np.arange(1, 10)

#read file
file = open('weeklyOrderData.txt', 'r')
lorder = file.read().split('\n')

file.close()

#cast to an int

for i in range(0, len(lorder)):
    lorder[i] = int(lorder[i])

print(lorder)

lorder.append(0)

print(lorder)

nlorder = []

asd = np.arange(0, 25, 3)
print(asd)

for i in asd:
    sum = lorder[i] + lorder[i+1] + lorder[i+2]

    nlorder.append(sum)
    print(nlorder)



nlorder = np.divide(nlorder, 15)
print(nlorder)







plt.bar(week, nlorder, width=0.2,label = 'Weeks')

plt.grid(True)
plt.title('Avg Daily Orders per 3 Weeks')
plt.xlabel('Number of Grouped Weeks')
plt.ylabel('Avg. Daily Orders')




plt.show()


