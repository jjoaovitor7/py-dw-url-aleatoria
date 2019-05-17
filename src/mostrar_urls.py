# -*- coding: utf-8 -*-
from tkinter import *
import platform
import sqlite3
from ajuda_redes import ajuda_redes

def mostrar_urls():
    jURL = Toplevel()
    jURL.title('URLs')
    jURL.configure(bg = 'black')

    so = platform.system()
    if so == 'Linux':
       jURL.wm_iconbitmap('@ico/dw_ico.xbm')
    if so == 'Windows':
       jURL.wm_iconbitmap('ico\dw_ico.ico')
    
    menubar = Menu(jURL)
    jURL.config(menu = menubar)
     
    ajuda = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'Redes', command = ajuda_redes)

    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nome, url FROM urls;
    """)
    
    x = 0
    fonte = ('Times New Roman', '11')
    for url in cursor.fetchall():
        lURL = Label(jURL, text = url, font = fonte)
        lURL.configure(bg = 'black', fg = '#00ff00')
        lURL.grid(column = 0, row = x, sticky = W)
        x += 1
    
    conn.close()
