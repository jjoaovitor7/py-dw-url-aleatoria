from tkinter import *

fonte=('Times New Roman', '10')

def ajuda_navegadores():
    janelaNavegadores=Toplevel()
    janelaNavegadores.title('Navegadores')
    janelaNavegadores.wm_iconbitmap('dw_ico.ico')
    janelaNavegadores.configure(bg='black')
    
    redeOnion=Label(janelaNavegadores, text='Rede onion: https://www.torproject.org/download/', font=fonte)
    redeI2P=Label(janelaNavegadores, text='Rede i2p: https://geti2p.net/pt-br/download', font=fonte)
    redeOnion.configure(bg='black', fg='#00ff00')
    redeI2P.configure(bg='black', fg='#00ff00')
    redeOnion.grid(column=0, row=0, sticky=W)
    redeI2P.grid(column=0, row=1, sticky=W)
