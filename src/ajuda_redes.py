#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import logging
import sqlite3

import definir_cor
import mostrar_urls


def ajuda_redes(self):
    def configurar_janela():
        self.title('Redes')

    def tema_preto():
        self.config(bg=definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('redes.TLabel', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        font=('Times New Roman', '14'))

    configurar_janela()
    configurar_icone.configurar_icone()

    tema_preto()

    menubar = tk.Menu(self)
    self.config(menu=menubar)

    ajuda = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Ajuda', menu=ajuda)
    ajuda.add_command(label='URLs', command=mostrar_urls.run)

    l_onion = ttk.Label(self,
                        text='Onion: https://www.torproject.org/download',
                        style='redes.TLabel')
    l_i2p = ttk.Label(self,
                      text='i2p: https://geti2p.net/pt-br/download',
                      style='redes.TLabel')
    l_freenet = ttk.Label(self,
                          text='Freenet: https://freenetproject.org',
                          style='redes.TLabel')

    l_onion.grid(row=0, column=0, sticky=tk.W)
    l_i2p.grid(row=1, column=0, sticky=tk.W)
    l_freenet.grid(row=2, column=0, sticky=tk.W)


def run():
    root = tk.Toplevel()
    ajuda_redes(root)
    root.mainloop()
