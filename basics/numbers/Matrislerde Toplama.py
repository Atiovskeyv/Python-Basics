matris1 = [[0 for x in range(3)] for y in range(3)]
matris2 = [[0 for x in range(3)] for y in range(3)]
for i in range(3):
    for j in range(3):
        matris1[i][j] = int(input('İlk Matrisin '+str(i+1)+'. Satır '+str(j+1)+'. Sütun Elemanı:'))
        
for i in range(3):
    for j in range(3):
        matris2[i][j] = int(input('İkinci Matrisin '+str(i+1)+'. Satır '+str(j+1)+'. Sütun Elemanı:'))

print(matris1,'\n',matris2)
for i in range(3):
    for j in range(3):
        print('%5d' %(matris1[i][j] + matris2[i][j]),end='')
    print()
