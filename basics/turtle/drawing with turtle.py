from turtle import*
shape('turtle')
pensize(4)
w= Screen()
w.setup(500,500)

def soladön():
    left(90)
def sağadön():
    right(90)

def ileri ():
    forward(10)

def geri():
    backward(10)

w.onkeypress(soladön,'Left')
w.onkeypress(sağadön,'Right')
w.onkeypress(ileri,'Up')
w.onkeypress(geri,'Down')

w.listen()
w.mainloop()
