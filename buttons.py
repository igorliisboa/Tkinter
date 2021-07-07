from tkinter import *

janela = Tk()

def bt_click():
    print("Botão clicado!")
    lb["text"] = "Funcionou!"

bt = Button(janela, width=20, text="Ok", command=bt_click)
bt.place(x=80, y=100)
lb = Label(janela, text="Teste")
lb.place(x=100, y=150)


janela.geometry("300x300+200+200")
janela.mainloop()