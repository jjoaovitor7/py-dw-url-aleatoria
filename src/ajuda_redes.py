#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import logging
import sqlite3

import definir_cor
import configurar_icone


def ajuda_redes(self):
    def setTitle():
        self.title('Redes')


    def blackTheme():
        self.config(bg=definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('redes.TLabel', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        font=('Times New Roman', '14'))


    def setWidgets():
        #Rede Onion (.onion)
        l_onion = ttk.Label(self,
                            text='Onion: https://www.torproject.org/download',
                            style='redes.TLabel').grid(row=0, column=0,
                            sticky=tk.W)

        #Rede i2p (.i2p)
        l_i2p = ttk.Label(self,
                          text='i2p: https://geti2p.net/pt-br/download',
                          style='redes.TLabel').grid(row=1, column=0,
                          sticky=tk.W)

        #Rede Freenet
        l_freenet = ttk.Label(self,
                          text='Freenet: https://freenetproject.org',
                          style='redes.TLabel').grid(row=2, column=0,
                          sticky=tk.W)


    setTitle()
    configurar_icone.configurar_icone(self)
    blackTheme()

    setWidgets()


def run():
    root = tk.Toplevel()
    ajuda_redes(root)
    root.mainloop()


#if __name__ == '__main__':
    #run()
