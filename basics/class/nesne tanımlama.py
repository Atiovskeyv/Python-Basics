class dıkdortgen:
    def __init__(self,a,b):
        self.yuk = a
        self.gen = b
    def alan(self):
        return self.yuk*self.gen
    def cevre(self):
        return (self.yuk+self.gen)*2
    def cizme(self):
        for i in range(self.yuk):
            print('* '*self.gen)

x=int(input('Dikdörtgenin Yüksekliğini Girin:'))
y=int(input('Dikdörgenin Genişliğini  Girin:'))
print()
a = dıkdortgen(x,y)
print("Dikdörtgen alanı  :",a.alan())
print("Dikdörtgen çevresi:",a.cevre())
a.cizme()
print()

class kare(dıkdortgen):
    def __init__(self,kenar):
        self.yuk = kenar
        self.gen = kenar

    def cizme(self):
        for i in range(self.yuk):
            print('* '*self.yuk)

x=int(input('Karenin Kenar Uzunluğunu Giriniz:'))
print()

b = kare(x)
print("Karnenin Alanı   :",b.alan())
print("Karnenin Çevresi :",b.cevre())
b.cizme()
print()

class paralelkenar(dıkdortgen):
    def __init__(self,a,b):
        self.yuk = a
        self.gen = b

    def cevre(self):
        return 2*(self.gen + self.yuk*1.4)

    def cizme(self):
        for i in range(0,self.yuk):
            print(' '*(self.yuk-i-1) + '* '*self.gen)

    #def cevre(self):               # eğer dikdörtgenin ceçvre fonksiyonunu kullanmak istersem böyle yaparım  
     #   super().cevre(self)

h = int(input('Paralelkenarın Yükseklik :'))
t = int(input('Paralelkenarın Tabanını  :'))
print()

p = paralelkenar(h,t)

print('Paralelkenarın çevresi :',round(p.cevre()))
print('Paralelkenarın alanı   :',p.alan(),'\n')
p.cizme()
print()

class ikizkenarucken(paralelkenar):

    def alan(self):
        return (self.yuk*self.gen)*0.5

    def cevre(self):
        return self.gen + (self.yuk*1.4)*2

    def cizme(self):
        for i in range(self.yuk):
            print(' ' * int(i * 0.7) + '*' * self.gen)

h = int(input('Üçgenin Yükseklik :'))
t = int(input('Üçgenin Tabanını  :'))
print()

ucken = ikizkenarucken(h,t)

print('İkizkenar Üçkenin çevresi :',round(ucken.cevre()))
print('İkizkenar Üçkenin alanı   :',round(ucken.alan()))
ucken.cizme()
print()





    







        
