a=int(input('Değer Giriniz :'))
gün=a//86400
saat= (a%86400)//3600
dakika= ((a%86400)%3600)//60
saniye= (((a%86400)%3600)%60)
print('Girdiğiniz Değer',gün,'gün,',saat,'saat,',dakika,'dakika,',saniye,'saniye yapar')


