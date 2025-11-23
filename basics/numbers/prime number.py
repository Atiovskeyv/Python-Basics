variable = int(input("Enter the number :"))

for i in range(2,variable//2+2):
    if variable%i==0: break

if i > variable//2:
    print("This is a prime number.")

else:
    print("Not a prime number.")
    
