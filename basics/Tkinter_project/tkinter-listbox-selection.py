from tkinter import *

def print_selected():
    selected_items = lb.curselection()
    for i in selected_items:
        print(lb.get(i))

window = Tk()
lb = Listbox(window, selectmode=MULTIPLE)
lb.insert(END, "Python")
lb.insert(END, "Java")
lb.insert(END, "C++")
lb.insert(END, "Ruby")
lb.insert(END, "Go")
lb.pack()

btn = Button(window, text="Print", command=print_selected)
btn.pack()

window.mainloop()
