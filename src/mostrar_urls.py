# -*- coding: utf-8 -*-
import tkinter as tk
import platform
import sqlite3
import definir_cor
import main
import ajuda_redes

def mostrar_urls():
    wURL = tk.Toplevel()
    wURL.title('URLs')
    wURL.configure(bg = definir_cor.COR_PRETA)

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
    
    menubar = tk.Menu(wURL)
    #menubar.add_command(label = 'Início', command = main.main)    
    wURL.config(menu = menubar)
     
    ajuda = tk.Menu(menubar, tearoff = 0)
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
        lURL = tk.Label(wURL, text = url, font = fonte)
        lURL.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
        lURL.grid(column = 0, row = x, sticky = tk.W)
        x += 1
    
    conn.close()
