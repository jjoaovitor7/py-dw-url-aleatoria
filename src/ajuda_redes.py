# -*- coding: utf-8 -*-
import tkinter as tk
import platform
import sqlite3
import definir_cor
import main
import mostrar_urls

def ajuda_redes(self):
    self.title('Redes')
    self.config(bg = definir_cor.COR_PRETA)

    so = platform.system()
    try:
        if so == 'Linux':
           self.wm_iconbitmap('@ico/dw_ico.xbm')
    except TclError:
        print('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
           self.wm_iconbitmap('ico\dw_ico.ico')
    except TclError:
        print('dw_ico.ico não foi encontrado na pasta ico.')
        
    menubar = tk.Menu(self)
    menubar.add_command(label = 'Início', command = main.run)    
    self.config(menu = menubar)
    
    ajuda = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls.run)
    
    fonte = ('Times New Roman', '12')
    lOnion = tk.Label(self, text = 'Onion: https://www.torproject.org/download/', 
                   font = fonte)
    lI2p = tk.Label(self, text = 'i2p: https://geti2p.net/pt-br/download', 
                 font = fonte)
    lFreenet = tk.Label(self, text = 'Freenet: https://freenetproject.org/', 
                     font = fonte)
    
    lOnion.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)  
    lI2p.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    lFreenet.config(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    
    lOnion.grid(column = 0, row = 0, sticky = tk.W)
    lI2p.grid(column = 0, row = 1, sticky = tk.W)
    lFreenet.grid(column = 0, row = 2, sticky = tk.W)

def run():
    root = tk.Toplevel()
    ajuda_redes(root)
    root.mainloop()
