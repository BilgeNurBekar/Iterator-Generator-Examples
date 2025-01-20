class InfiniteGenerator:

    def __init__(self, num:int):
        if not isinstance(num,int):
            raise TypeError("num must be an integer")
        self.num = num
        self.step = 0

    def genInfinite(self):
        '''
        yield bir fonksiyonun çalışmasını durdurur ve değeri dışarıya geri döndürür, fakat fonksiyonun çalışmasını tamamen sonlandırmaz. 
        Bu, generator fonksiyonları için çok önemli bir özelliktir, çünkü fonksiyonun durduğu yerden devam edebilmesini sağlar. 
        Yani, yield bir değer döndürdüğünde, fonksiyonun o noktada durmasına yol açar ve fonksiyon çağrılmaya devam ederse, yield tekrar çalıştırılır ve kaldığı yerden devam eder.
        '''

        if self.num>=0:
            while True:
                if self.step <= self.num:
                    yield self.step
                    self.step +=1
                else:
                    break
        else:
            while True:
                if self.step >= self.num:
                    yield self.step
                    self.step -=1
                else: 
                    break


try:
    infinitePositive = InfiniteGenerator(100000)
    for i in infinitePositive.genInfinite():
        print(i)
except Exception as e:
    print(f"error: {e}")
    

try:
    infiniteNegative = InfiniteGenerator(-9)
    for i in infiniteNegative.genInfinite():
        print(i)

except Exception as e:
    print(f"error: {e}")

try:
    infiniteType = InfiniteGenerator([1,2,3,4,4])
    for i in infiniteType.genInfinite():
        print(i)

except Exception as e:
    print(f"error: {e}")



