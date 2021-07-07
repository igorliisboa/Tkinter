from tkinter import *

janela = Tk()

lb1 = Label(janela, text="side1", bg="green")
lb2 = Label(janela, text="side2", bg="red")
lb3 = Label(janela, text="anchor1", bg="yellow")
lb4 = Label(janela, text="anchor2", bg="blue")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=W)
lb4.pack(anchor=W)

janela.geometry("400x300+200+200")
janela.mainloop()