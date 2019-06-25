# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import sqlite3

import definir_cor
import ajuda_redes

def mostrar_urls(self):
    
    def configurar_janela():
        self.title('URLs')

    def configurar_icone():
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
                
    def tema_preto():
        self.config(bg = definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('urls.TLabel', background = definir_cor.COR_PRETA, 
                        foreground = definir_cor.COR_VERDE_CLARO, 
                        font = ('Times New Roman', '14'))
    
    configurar_janela()
    configurar_icone()
    
    tema_preto()
    
    menubar = tk.Menu(self)
    self.config(menu = menubar)
     
    ajuda = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'Redes', command = ajuda_redes.run)

    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nome, url FROM urls;
    """)
    
    x = 0
    for url in cursor.fetchall():
        l_url = ttk.Label(self, text = url, 
                          style = 'urls.TLabel')
        l_url.grid(column = 0, row = x, sticky = tk.W)
        x += 1
    
    conn.close()

def run():
    root = tk.Toplevel()
    mostrar_urls(root)
    root.mainloop()
