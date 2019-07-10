#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import sqlite3
import webbrowser

import definir_cor
import mostrar_urls
import ajuda_redes


def main(self):
    def configurar_janela():
        self.title('Deep Web URL Aleatória')
        self.geometry('500x75')
        self.grid_columnconfigure(0, weight=1)

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
        self.config(bg=definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('main.TLabel', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        font=('Times New Roman', '14'))
        style.configure('main.TButton', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        width=5, relief=tk.RAISED)

    def tema_branco():
        self.config(bg=definir_cor.COR_BRANCA)
        style = ttk.Style()
        style.configure('main.TLabel', background=definir_cor.COR_BRANCA,
                        foreground=definir_cor.COR_PRETA,
                        font=('Times New Roman', '14'))
        style.configure('main.TButton', background=definir_cor.COR_BRANCA,
                        foreground=definir_cor.COR_PRETA,
                        width=5, relief=tk.RAISED)

    configurar_janela()
    configurar_icone()

    tema_preto()

    menubar = tk.Menu(self)
    self.config(menu=menubar)

    preferencias = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Preferências', menu=preferencias)

    temas = tk.Menu(menubar, tearoff=0)
    preferencias.add_cascade(label='Temas', menu=temas)

    temas.add_command(label='Tema Branco', command=tema_branco)
    temas.add_command(label='Tema Preto', command=tema_preto)

    ajuda = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Ajuda', menu=ajuda)
    ajuda.add_command(label='URLs', command=mostrar_urls.run)
    ajuda.add_command(label='Redes', command=ajuda_redes.run)

    l_titulo = ttk.Label(self, text='Deep Web URL Aleatória',
                         style='main.TLabel')
    l_titulo.grid(row=0, column=0)

    l_url = ttk.Label(self, text='URL', style='main.TLabel')
    l_url.grid(row=1, column=0)

    def b_go_clicado():
        conn = sqlite3.connect('urls.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT url FROM urls  ORDER BY RANDOM() LIMIT 1;
        """)
        get_url = cursor.fetchall()
        get_url_ = str(get_url).strip('()[],\'\'')
        l_url.config(text=get_url)
        conn.close()
        
        def clicar_url(event):
            webbrowser.open_new(get_url_)
        l_url.bind('<Button-1>', clicar_url)

    b_go = ttk.Button(self, text='Go!',
                      style='main.TButton',
                      command=b_go_clicado)
    b_go.grid(row=3, column=0)


def run():
    root = tk.Tk()
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
