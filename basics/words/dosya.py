
with open("notlar.txt","r",encoding="utf8") as dosya:
    liste = dosya.read()
    print(liste)
    dosya.close()
    
with open("notlar.txt","w",encoding="utf8") as dosya:
    while True:
        print("not eklemek için 1\'e, not silmek için2\'ye çıkış için 3\'e basın")

        işlem = int(input("İşlemi seçiniz :"))
        print()

        if işlem == 1:
            karakter = input("Notunuzu giriniz :")
            dosya.write(karakter+"\n")

        if işlem == 2:
            karakter = input("Silmek istediğiniz notun numarasını giriniz :")
            for satır in dosya:
                if str(karakter+"\n") or str(karakter) in satır
                
                

        if işlem == 3:
            print("\n","işlem sonlandı")
            break

        dosya.close()

with open("notlar.txt","r",encoding="utf8") as dosya:
    liste = dosya.read()
    print(liste)
    dosya.close()
    
            
        
        
            
            
        
