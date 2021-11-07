class Animal:
    def __init__(self,Ten,CanNang,ChieuCao,DoAn):
        self.__Ten = Ten
        self._CanNang = CanNang
        self.__ChieuCao = ChieuCao
        self.__DoAn = DoAn
    def printInfo(self):
        print("Ten cua con vat la:",self.__Ten)
        print("Can nang cua con vat la:",self._CanNang)
        print("Chieu cao cua con vat la:",self.__ChieuCao)
        print("Do an cua con vat la:",self.__DoAn)
    @staticmethod
    def CheckCanNang(CanNang):
        if(CanNang >= 3):
            print("Can phai giam can")
        else:
            print("Khong can giam can")


Cat = Animal("Sima",3.4,5.6,"Ca")
Cat.__ChieuCao = 10
Cat.printInfo()
Cat.CheckCanNang(Cat._CanNang)









