# -*- coding: utf-8 -*-
from tkinter import *
import platform, sqlite3
from ajuda_redes import *

def mostrar_urls():
    so=platform.system()
    jURL=Toplevel()
    jURL.title('URLs')
    if so=='Windows':
            jURL.wm_iconbitmap('ico\dw_ico.ico')
    if so=='Linux':
            jURL.wm_iconbitmap('@ico/dw_ico.xbm')
    jURL.configure(bg='black')
     
    menubar=Menu(jURL)
    jURL.config(menu=menubar)
     
    ajuda=Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Ajuda', menu=ajuda)
    ajuda.add_command(label='Redes', command=ajuda_redes)

    conn=sqlite3.connect('urls.db')
    cursor=conn.cursor()
    cursor.execute("""
    SELECT nome, url FROM urls;
    """)
    x=0
    for url in cursor.fetchall():
        lURL=Label(jURL, text=url, font=('Times New Roman', '11'))
        lURL.configure(bg='black', fg='#00ff00')
        lURL.grid(column=0, row=x, sticky=W)
        x+=1
    conn.close()
