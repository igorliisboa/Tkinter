from tkinter import *

def bt_click():
    print(ed.get())
    lb["text"] =  ed.get()

janela = Tk()

ed = Entry(janela)
ed.place(x=80, y=100)
bt = Button(janela, width=20, text="Ok", command=bt_click)
bt.place(x=80, y=140)

lb = Label(janela, text="Teste")
lb.place(x=80, y=180)

janela.geometry("300x300+200+200")
janela.mainloop()