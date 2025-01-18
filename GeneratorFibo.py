class GeneratorFibo:
    '''
    GeneratorFibo sınıfı generator kullanarak fibonacci sayi dizilerini üretmeyi sağlar
    '''

    def __init__(self, n):
        if n<0:
            raise ValueError("n değeri negatif olamaz")
        else:
            self._n = n
            self.last = 0
            self.toplam = 1
        

    @property
    def n(self):
        return self._n
    
    @n.setter
    def n(self,deger):
        if deger<0:
            raise ValueError("n değeri negatif olamaz")
        else:
            self._n = deger

    def fibo(self):
        '''
        fibo() generator kullanarak fibonacci dizisi üretir.
        self.toplam bir generator nesnesi olduğu için iter() e ve next() e sahiptir.
        '''
        for i in range(self._n):
            yield self.toplam
            self.last, self.toplam = self.toplam, self.toplam+ self.last


try:
    '''
    nesne oluşturma negatif değerler için kontrol altına alındı.
    Exception as e ile hata mesajı e' ye atanır.
    raise ile yakalanan ValueError hatasının mesajı döndürülür.
    '''
    obj1= GeneratorFibo(8)
    for i in obj1.fibo():
        print(i)
except Exception as e:
    print(e)
