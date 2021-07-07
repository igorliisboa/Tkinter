from tkinter import *

janela = Tk()

lb = Label(janela, text="Teste", bg="green")
lb2 = Label(janela, text="Teste", bg="red")
lb3 = Label(janela, text="Teste", bg="yellow")

lb.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry("400x300+250+250")
janela.mainloop()