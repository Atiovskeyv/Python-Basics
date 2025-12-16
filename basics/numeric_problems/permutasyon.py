

a = int(input('İlk Sayıyı Girin:'))
b = int(input('İkinci Sayıyı Girin:'))

if a<b:
    a,b = b,a

def per(a,b):
    üst = 1
    alt = 1
    islem = 1
    for a in range(a,a-b,-1):
        üst = üst*a
        
        for b in range(b,0,-1):
            
            alt = alt*b
    islem = int(üst/alt)
    print('Sonuç:',islem)

per(a,b)
            
            
        
    
