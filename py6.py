
class Info():
    def __init__(self,hesabNo,balans,*args):
        self.hesabNo=hesabNo
        self.balans=balans
    def artir(self,mebleg):
        self.balans+=mebleg
        print("Balans artirildi , balans {} azn".format(self.balans))

    def cixar(self,mebleg):
        self.mebleg=mebleg
        if self.balans > self.mebleg or self.balans==self.mebleg:
            self.balans-=self.mebleg
            print("Balansdan {} azn pul cixarildi, balans {} azn".format(self.mebleg,self.balans))
        else:
            print("Balansda kifayet qeder mebleg yoxdur")
    def goster(self):
        if self.kreditMebleg:
            print("Kredit borcunuz {} azn".format(self.kreditMebleg))
        else:
            print("Borcunuz yoxdur")
        if self.kreditMebleg ==0:
            print("Kredit borcunuz tam odenib")
                  

class Kredit(Info):
    
    def __init__(self,*args):
        super().__init__(*args)
        
    def kreditAl(self,kreditMebleg):
        self.kreditMebleg=kreditMebleg
        self.balans+=self.kreditMebleg
        print("Kredit alindi, balansiniz {} azn, borcunuz {} azn".format(self.balans,self.kreditMebleg))
        
    def kreditOde(self):
        self.odenen=(self.kreditMebleg/12)    
        if not self.balans <self.odenen:
            self.balans-=self.odenen
            print("Kredit odendi ,balans {} azn,qaliq borc {} azn".format(self.balans,self.kreditMebleg-self.odenen))
        else:
            print("Kredit odemek ucun balansinizda kifayet qeder vesait yoxdur ,balansiniz {} azn".format(self.balans))
            



#kredit=Kredit(844,3000)   

        
        
