from tkinter import *

root = Tk()
root.geometry("300x200")

s1 = Spinbox(root, from_=0, to=25)
s1.pack()

s2 = Spinbox(root, values=(10,20,30,40,50), wrap=True)
s2.pack()

s3 = Spinbox(root, values=("Abacate", "Morango", "Melancia", "Abacaxi"), wrap=True)
s3.pack()

def executar1():
    print(s1.get())

def executar2():
    print(s2.get())

def executar3():
    print(s3.get())

cmd1 = Button(root, text="Clique", command=executar1)
cmd2 = Button(root, text="Clique", command=executar2)
cmd3 = Button(root, text="Clique", command=executar3)
cmd1.pack()
cmd2.pack()
cmd3.pack()

root.mainloop()