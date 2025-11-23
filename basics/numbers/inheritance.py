class Rectangle:
   __objectnumber = 0
   def __init__(object,a,b):

       object.shortside = a
       object.longside = b
       Rectangle.__objectnumber +=1
       print("Object added succesfully","\n")

   def __del__(object):
       Rectangle.__objectnumber -=1
       print("Object deleted succesfully","\n")

   @staticmethod
   def count():
       print("Number of total created rectangles :",Rectangle.__objectnumber)
       
   
   def area(input):
       print("Objects area :",input.shortside*input.longside)

   def çevre(input):
       print("Objects perimeter :",2*(input.shortside+input.longside))

class Square(Rectangle):
   __objectnumber = 0
   def __init__(object,a):
       object.longside = a
       object.shortside = a
       Square.__objectnumber += 1
       print("Object added succesfully","\n")

   def __del__(object):
       Square.__objectnumber -=1
       print("Object deleted succesfully","\n")
       

   @staticmethod
   def count():
       print("Number of total created squares :",Square.__objectnumber)

d1 = Rectangle(5,8)
d2 = Rectangle(6,10)
d3 = Rectangle(8,15)
d4 = Rectangle(80,50)
k1 = Square(5)
k2 = Square(8)



        
    
        

    
    


    
