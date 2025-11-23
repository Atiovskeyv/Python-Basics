while True:
    print('Toplama için 1i, Çıkarma için 2yi, Çarpma için 3ü, Bölme için 4ü seçin')

    islem=int(input('İşlemi seçiniz:'))

    while islem not in range(1,5):
        print('Hatalı İşlem Yaptınız')
        islem=int(input('İşlemi seçiniz:'))
    
    a=float(input('İlk sayıyı giriniz :'))
    b=float(input('İkinci sayıyı giriniz :'))
    if islem==1:
        print('Toplam =', a+b)
    elif islem==2:
        print('Fark =', a-b)
    elif islem==3:
        print('Çarpım =',a*b)
    elif islem==4:
        if b==0:
            print('Cevap sonsuz çıakr')
        else:
            print('Bölüm =', a/b,'\n','Bölüm =:',a//b,'\n','Kalan =',a%b)
    if a or b =='bitir':
        break

