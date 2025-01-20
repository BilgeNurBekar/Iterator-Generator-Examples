import sys
'''
Çalışma generator ve klasik listede veri tutmanın bellek boyutunu gösterir
'''

class MemoryManagementGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.step = 0

    def squared(self):
        return self.step ** 2

    def generatorSquare(self):
        while True:
            if self.step<= self.stop:
                yield self.squared()
                self.step += 1
            else: 
                break
    def objectSize(self):
        return f"Generator object size: {sys.getsizeof(self.generatorSquare())}"



class MemoryManagementList:
    def __init__(self, liste):
        self.liste = liste
        

    def squared(self):
        squaredListe = [i**2 for i in self.liste]
        return(f"{squaredListe} \n sizeof: {sys.getsizeof(squaredListe)}")
    

if __name__ == '__main__': 
    try:

        obj1 = MemoryManagementGenerator(10000)

        for i in obj1.generatorSquare():
            print(i)
        print(obj1.objectSize())

    except Exception as e:
        print(e)


    try:
        liste = [i for i in range(10000)]

        obj2 = MemoryManagementList(liste)

        print(obj2.squared())

    except Exception as e:
        print(e)
