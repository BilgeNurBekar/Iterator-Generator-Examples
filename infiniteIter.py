class InfiniteIter:
    '''
    InfiniteIter sinifi negatif ve pozitif sonsuz sayiyinin üretilmesini sağlar. Bu sayilar üretilirken stackoverflow hatasi alinmamis olur.
    '''
    def __init__(self, num:int):
        '''
        num: stop sayisi
        if not karar yapisi: type kontrolü sağlar. Nesne olustururken doğru çalişma saglanir
        '''
        if not isinstance(num, int):
            raise TypeError("num must be an integer")
        self.num = num
        self.step = 0

    def __iter__(self):
        return self
     

    def __next__(self):
        if self.num >= 0:
            if self.step<=self.num:
                temp = self.step
                self.step += 1
                return temp
        else:
            if self.step>=self.num:
                temp = self.step
                self.step -= 1
                return temp
        
        raise StopIteration("the loops are stopped")

                    
#pozitif sayi için örnek
try:
    infinitePositive = InfiniteIter(100000)
    #for number in infinitePositive:
    while True:
        try:
            print(next(infinitePositive))
        except StopIteration:
            break
except Exception as e:
    print(f"Error: {e}")

#negatif sayi için örnek
try:
    infiniteNegative = InfiniteIter(-99)
    for i in infiniteNegative:
        print(i)
except Exception as e:
    print(f"Error: {e}")

#type kontrolü için örnek
try:
    infiniteType = InfiniteIter("a")
    for b in infiniteType:
        print(b)
except Exception as e:
    print(f"Error: {e}")


