import random
deger=int(input('Kaç Adet Sayı Gireceksiniz? :'))
Liste  = []
Liste2 = []
for i in range(deger):
    x=random.randint(-999,999)
    Liste.append(x)
print('Girdiğiniz Sayılar=','\n',Liste)

max_int = 1   
for i in range(deger):
    max_int = max(Liste)
    Liste.remove(max_int)
    Liste2.append(max_int)
print('\n','Sıralanmış Liste=','\n',Liste2)
