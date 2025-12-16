class Personel:
    __numberofstuff = 0

    def __init__(self,a,b):

        self.name = a
        self.salary = b
        Personel.__numberofstuff += 1
        print(self.name,"added succesfully","\n")
        

    def __del__(self):
        Personel.__numberofstuff -=1
        print(self.name,"deleted succesfully","\n")


    def query(self):
        print("Name :",self.name," Salary :",self.salary)

    @staticmethod
    def StuffNumber():
        print("Number of Personel: ",Personel.__numberofstuff)
        
P1 = Personel("Ahmet",24000)
P2 = Personel("George",18000)
P3 = Personel("Jhames",32000)
Personel.query(P3)
Personel.StuffNumber()
del P1
Personel.StuffNumber()
del P2
Personel.StuffNumber()
del P3
Personel.StuffNumber()

