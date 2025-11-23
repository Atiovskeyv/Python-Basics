from tkinter import *

def yazdir():
    secilenler = lb.curselection()
    for i in secilenler:
        print(lb.get(i))

window = Tk()
lb = Listbox(window, selectmode=MULTIPLE)
lb.insert(END, "Python")
lb.insert(END, "Java")
lb.insert(END, "C++")
lb.insert(END, "Ruby")
lb.insert(END, "Go")
lb.pack()

btn = Button(window, text="Yazdır", command=yazdir)
btn.pack()

window.mainloop()
