#Bir sınıf oluşturun. Bu sınıf, Fibonacci dizisinin ilk n elemanını döndüren bir iterator olacak. Fibonacci dizisi: 0, 1, 1, 2, 3, 5, 8, ...

class Fibonacci:
    stepNo = 0
    lastStep = 0
    temp = 0
    def __init__(self, n): 

        '''
        _n girilecek olan sayi
        toplam verilen sayıya kadar fibonacci toplamını tutar
        negatif bir değer girilmesi durumunda hata fırlatarak çalışmayı durdurması için önce negatif sayı durumu ele alındı.
        '''

        if n<0:
            raise ValueError("n degeri sıfırdan kucuk olamaz")
        self._n = n
        self.toplam = 1
       


    @property
    def n(self):
        '''
        private olan n değerinin getirilmesi
        '''
        return self._n
        
    @n.setter
    def n(self,x):
        '''
        n değerinin obj oluşturulması dışında değiştirilmesi kontrol altına alındı.
        '''
        if x<=0:
            raise ValueError("n degeri sıfırdan kucuk olamaz")
        else:
            self._n = x



    def __iter__(self):
        return self
    
    def __next__(self):

        if self.stepNo>=self._n:
                raise StopIteration
        if self.stepNo== 0:
            self.stepNo+=1
            return 0
        elif self.stepNo == 1:
            self.stepNo+=1
            self.temp = 1
            return 1
        else:
            self.toplam += self.lastStep
            self.lastStep=self.temp
            self.temp = self.toplam
            self.stepNo +=1
            return self.toplam
# Kullanım
try:
    obj = Fibonacci(9)  
    for i in obj:
        print(i)
except ValueError as e:
    print(e)

try:

    obj1 = Fibonacci(-9)
    obj1.n = -3
except Exception as e:
    print(e)

        

