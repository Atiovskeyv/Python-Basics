#There are 100 men standing in order, each with a number on them, and there are doors. 
# Each man toggles (opens if closed, closes if open) the doors whose positions are multiples of his number. 
# In the end, which doors will be open and which will be closed?

Sum = 0
for a in range(1,101):
    for x in range(1,a+1):
        if a%x == 0:
            Sum +=1
    if Sum%2 == 0:
        print('\n',a,'. door is closed')
    else:
        print('\n',a,'. door is open')
    Sum=0
            
        
    
