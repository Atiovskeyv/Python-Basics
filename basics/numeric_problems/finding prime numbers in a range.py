Liste=[]
x=int(input("Enter the starting value :"))
y=int(input("Enter the ending value :"))

if x>y:
    x,y=y,x

for i in range(x,y+1):
    if i<2:
        continue
    for a in range(2,int(i**(0.5))+1):
        if i%a == 0:
            break
    else:
        Liste.append(i)

print(Liste)

Sum = sum(Liste)/len(Liste)

print('Sum=',Sum)

total=0
for i in Liste:
    total +=(Sum-i)**2

variance = total/(len(Liste)-1)
deflection = variance**(0.5)

print('Variance = {} and Standart Deflection = {}'.format(str(variance),str(deflection)))
   


        




    
    
            

        
