from tkinter import *
import platform

fonte=('Times New Roman', '11')

def ajuda_redes():
    so=platform.system()
    jRedes=Toplevel()
    jRedes.title('Redes')
    if so=='Windows':
            jRedes.wm_iconbitmap('ico\dw_ico.ico')
    if so=='Linux':
            jRedes.wm_iconbitmap('@ico/dw_ico.xbm')    
    jRedes.configure(bg='black')
    
    lOnion=Label(jRedes, text='Onion: https://www.torproject.org/download/', font=fonte)
    lI2p=Label(jRedes, text='i2p: https://geti2p.net/pt-br/download', font=fonte)
    lFreenet=Label(jRedes, text='Freenet: https://freenetproject.org/', font=fonte)
    
    lOnion.configure(bg='black', fg='#00ff00')  
    lI2p.configure(bg='black', fg='#00ff00')
    lFreenet.configure(bg='black', fg='#00ff00')
    
    lOnion.grid(column=0, row=0, sticky=W)
    lI2p.grid(column=0, row=1, sticky=W)
    lFreenet.grid(column=0, row=2, sticky=W)
