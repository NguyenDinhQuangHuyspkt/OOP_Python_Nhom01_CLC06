class Animal:
    stt = 1
    def __init__(self,Ten,CanNang,ChieuCao,DoAn):
        self.Ten = Ten
        self.CanNang = CanNang
        self.ChieuCao = ChieuCao
        self.DoAn = DoAn
    def printInfo(self):
        print("Ten cua con vat la:",self.Ten)
        print("Can nang cua con vat la:",self.CanNang)
        print("Chieu cao cua con vat la:",self.ChieuCao)
        print("Do an cua con vat la:",self.DoAn)

Cat = Animal("Sima",3.4,5.6,"Ca")
Cat.printInfo()









