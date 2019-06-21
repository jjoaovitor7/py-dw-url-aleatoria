# -*- coding: utf-8 -*-
from tkinter import *
import platform
import sqlite3
import main
import ajuda_redes

def mostrar_urls():
    wURL = Toplevel()
    wURL.title('URLs')
    wURL.configure(bg = 'black')

    so = platform.system()
    try:
        if so == 'Linux':
           wURL.wm_iconbitmap('@ico/dw_ico.xbm')
    except TclError:
        print('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
           wURL.wm_iconbitmap('ico\dw_ico.ico')
    except TclError:
        print('dw_ico.ico não foi encontrado na pasta ico.')
    
    menubar = Menu(wURL)
    menubar.add_command(label = 'Início', command = main.main)    
    wURL.config(menu = menubar)
     
    ajuda = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'Redes', command = ajuda_redes.ajuda_redes)

    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nome, url FROM urls;
    """)
    
    x = 0
    fonte = ('Times New Roman', '12')
    for url in cursor.fetchall():
        lURL = Label(wURL, text = url, font = fonte)
        lURL.configure(bg = 'black', fg = '#00ff00')
        lURL.grid(column = 0, row = x, sticky = W)
        x += 1
    
    conn.close()
