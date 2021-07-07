from tkinter import *

def button1_click():
    lb["text"] = "Botão 1 clicado!"
def button2_click():
    lb["text"] = "Botão 2 clicado!"

janela = Tk()


bt1 = Button(janela, width=20, text="Botão 1", command=button1_click)
bt1.place(x=100, y=100)
bt2 = Button(janela, width=20, text="Botão 2", command=button2_click)
bt2.place(x=100, y=140)

lb = Label(janela, text="Testando funções")
lb.place(x=100, y=180)


janela.geometry("300x300+200+200")
janela.mainloop()