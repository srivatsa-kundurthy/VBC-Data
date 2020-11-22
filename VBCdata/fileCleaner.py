

class fileCleaner:
    def __init__(self, fileName):
        self.fileName = fileName

        global temp

        file = open(self.fileName, 'r')
        temp = file.read().split('\n')
        file.close()

        print(temp)

    def delLines(self, item):
        self.item = item
        while ("" in temp):
            temp.remove("")

        return temp










d = []
x = fileCleaner('compQ.txt')

a = x.delLines('')
print(a)
print(len(a))


def noteNew():


    with open('cleanCompQ.txt', 'w') as file:
        for item in a:
            file.write("%s\n" % item)

        file.close()

noteNew()






