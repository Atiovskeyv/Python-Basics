A=input('Enter a text:')
A = list(A)

print(A,'\n')


B = set(A)
if " " in B:
    B.remove(' ')

for i in B:
    print(i,'Harfinden Listede ',A.count(i),'Adet Var')
    
    
