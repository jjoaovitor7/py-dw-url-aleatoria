# -*- coding: utf-8 -*-
from tkinter import *
import platform
import sqlite3
import definir_cor
import main
import mostrar_urls

def ajuda_redes():
    wRedes = Toplevel()
    wRedes.title('Redes')
    wRedes.configure(bg = definir_cor.COR_PRETA)

    so = platform.system()
    try:
        if so == 'Linux':
           wRedes.wm_iconbitmap('@ico/dw_ico.xbm')
    except TclError:
        print('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
           wRedes.wm_iconbitmap('ico\dw_ico.ico')
    except TclError:
        print('dw_ico.ico não foi encontrado na pasta ico.')
        
    menubar = Menu(wRedes)
    menubar.add_command(label = 'Início', command = main.main)    
    wRedes.config(menu = menubar)
    
    ajuda = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls.mostrar_urls)
    
    fonte = ('Times New Roman', '12')
    lOnion = Label(wRedes, text = 'Onion: https://www.torproject.org/download/', 
                   font = fonte)
    lI2p = Label(wRedes, text = 'i2p: https://geti2p.net/pt-br/download', 
                 font = fonte)
    lFreenet = Label(wRedes, text = 'Freenet: https://freenetproject.org/', 
                     font = fonte)
    
    lOnion.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)  
    lI2p.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    lFreenet.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    
    lOnion.grid(column = 0, row = 0, sticky = W)
    lI2p.grid(column = 0, row = 1, sticky = W)
    lFreenet.grid(column = 0, row = 2, sticky = W)
