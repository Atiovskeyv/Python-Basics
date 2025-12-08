girdi = input("Metin giriniz: ")
girdi = girdi.replace(" ", "")  # boşlukları kaldır

if girdi == girdi[::-1]:
    print("Bu sayı/metin palindromdur.")
else:
    print("Bu sayı/metin palindrom değildir.")
