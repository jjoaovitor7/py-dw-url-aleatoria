from tkinter import *

fonte=('Times New Roman', '10')

def ajuda_navegadores():
    janelaNavegadores=Toplevel()
    janelaNavegadores.title('Navegadores')
    janelaNavegadores.wm_iconbitmap('dw_ico.ico')
    janelaNavegadores.configure(bg='black')
    
    lOnion=Label(janelaNavegadores, text='Rede onion: https://www.torproject.org/download/', font=fonte)
    lI2p=Label(janelaNavegadores, text='Rede i2p: https://geti2p.net/pt-br/download', font=fonte)
    lOnion.configure(bg='black', fg='#00ff00')
    lI2p.configure(bg='black', fg='#00ff00')
    lOnion.grid(column=0, row=0, sticky=W)
    lI2p.grid(column=0, row=1, sticky=W)
