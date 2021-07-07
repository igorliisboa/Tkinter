from tkinter import *

def soma():
    if(str(num1.get()).isnumeric() and str(num2.get()).isnumeric()):
        numero1 = int(num1.get())
        numero2 = int(num2.get())
        soma = numero1 + numero2
        lb["text"] = soma
    else:
        lb["text"] = "Valor informado inválido!"

janela = Tk()

num1 = Entry(janela)
num1.place(x=80, y=100)
num2 = Entry(janela)
num2.place(x=80, y=130)
bt = Button(janela, width=20, text="Soma", command=soma)
bt.place(x=80, y=170)

lb = Label(janela, text="Somar 2 valores")
lb.place(x=80, y=210)

janela.geometry("300x300+200+200")
janela.mainloop()