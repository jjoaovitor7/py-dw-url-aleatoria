# -*- coding: utf-8 -*-
import tkinter as tk
import platform
import sqlite3
import definir_cor
import main
import mostrar_urls

def ajuda_redes():
    wRedes = tk.Toplevel()
    wRedes.title('Redes')
    wRedes.config(bg = definir_cor.COR_PRETA)

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
        
    menubar = tk.Menu(wRedes)
    menubar.add_command(label = 'Início', command = main.run)    
    wRedes.config(menu = menubar)
    
    ajuda = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls.mostrar_urls)
    
    fonte = ('Times New Roman', '12')
    lOnion = tk.Label(wRedes, text = 'Onion: https://www.torproject.org/download/', 
                   font = fonte)
    lI2p = tk.Label(wRedes, text = 'i2p: https://geti2p.net/pt-br/download', 
                 font = fonte)
    lFreenet = tk.Label(wRedes, text = 'Freenet: https://freenetproject.org/', 
                     font = fonte)
    
    lOnion.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)  
    lI2p.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    lFreenet.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    
    lOnion.grid(column = 0, row = 0, sticky = tk.W)
    lI2p.grid(column = 0, row = 1, sticky = tk.W)
    lFreenet.grid(column = 0, row = 2, sticky = tk.W)
