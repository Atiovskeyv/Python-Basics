vize=int(input('Vize notunu giriniz:'))
final=int(input('Final notunu giriniz:'))
basarinotu= int(vize*0.3 + final*0.7 + 0.5)
print('Başarı Notu =',basarinotu)

if basarinotu >=50:
    print('\n','Sınavı Geçtin')
    
else:
    print('\n','Sınavdan Kaldın, Geçmek için:', int(1.42*(50-vize*0.3)),'Almalıydın')
    büt= int(input('Büt notunuzu Girin'))
    basarinotu= int(vize*0.3 + büt*0.7 + 0.5)
    print('Başarı Notu =',basarinotu,)
    if basarinotu >=50:
        print('\n','Sınavı Geçtin')
    else:
        print('\n','Sınavdan Kaldın')
        
        
        

    
    
