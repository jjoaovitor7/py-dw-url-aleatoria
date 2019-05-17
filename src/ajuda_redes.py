# -*- coding: utf-8 -*-
from tkinter import *
import platform
import sqlite3
from mostrar_urls import mostrar_urls

def ajuda_redes():
    jRedes = Toplevel()
    jRedes.title('Redes')
    jRedes.configure(bg = 'black')

    so = platform.system()
    if so == 'Linux':
            jRedes.wm_iconbitmap('@ico/dw_ico.xbm')    
    if so == 'Windows':
            jRedes.wm_iconbitmap('ico\dw_ico.ico')
    
    menubar = Menu(jRedes)
    jRedes.config(menu = menubar)
    
    ajuda = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls)
    
    fonte = ('Times New Roman', '11')
    lOnion = Label(jRedes, text = 'Onion: https://www.torproject.org/download/', font = fonte)
    lI2p = Label(jRedes, text = 'i2p: https://geti2p.net/pt-br/download', font = fonte)
    lFreenet = Label(jRedes, text = 'Freenet: https://freenetproject.org/', font = fonte)
    
    lOnion.configure(bg = 'black', fg = '#00ff00')  
    lI2p.configure(bg = 'black', fg = '#00ff00')
    lFreenet.configure(bg = 'black', fg = '#00ff00')
    
    lOnion.grid(column = 0, row = 0, sticky = W)
    lI2p.grid(column = 0, row = 1, sticky = W)
    lFreenet.grid(column = 0, row = 2, sticky = W)
