#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import logging
import sqlite3

import definir_cor
import configurar_icone
import ajuda_redes


def mostrar_urls(self):
    def setTitle():
        self.title('URLs')


    def blackTheme():
        self.config(bg=definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('urls.TLabel', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        font=('Times New Roman', '14'))


    def setWidgets(url, x):
        l_url = ttk.Label(self, text=url,
                          style='urls.TLabel').grid(row=x,
                                                    column=0,
                                                    sticky=tk.W)


    def readDB():
        conn = sqlite3.connect('urls.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nome, url FROM urls;')

        x=0
        for url in cursor.fetchall():
            setWidgets(url, x)
            x+=1

        conn.close()


    setTitle()
    configurar_icone.configurar_icone(self)

    blackTheme()

    readDB()


def run():
    root = tk.Toplevel()
    mostrar_urls(root)
    root.mainloop()


#if __name__ == '__main__':
    #run()
