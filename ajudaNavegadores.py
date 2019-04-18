from tkinter import *

def ajudaNavegadores():

    janelaNavegadores = Tk()
    janelaNavegadores.title('Navegadores')

    redeOnion = Label(janelaNavegadores, text="Rede onion: https://www.torproject.org/download/", font=("Times New Roman", "11"))
    redeI2P = Label(janelaNavegadores, text="Rede i2p: https://geti2p.net/pt-br/download", font=("Times New Roman", "11"))

    redeOnion.grid(column=0, row=0)
    redeI2P.grid(column=0, row=1)
