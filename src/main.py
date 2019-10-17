#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import logging
import sqlite3
import webbrowser

import definir_cor
import configurar_icone
import mostrar_urls
import ajuda_redes


def main(self):
    def setTitle():
        self.title('Deep Web URL Aleatória')


    def setGeometry():
        self.geometry('500x75')
        self.grid_columnconfigure(0, weight=1)


    def blackTheme():
        self.config(bg=definir_cor.COR_PRETA)
        style = ttk.Style()
        style.configure('main.TLabel', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        font=('Times New Roman', '14'))
        style.configure('main.TButton', background=definir_cor.COR_PRETA,
                        foreground=definir_cor.COR_VERDE_CLARO,
                        width=5, relief=tk.RAISED)


    def whiteTheme():
        self.config(bg=definir_cor.COR_BRANCA)
        style = ttk.Style()
        style.configure('main.TLabel', background=definir_cor.COR_BRANCA,
                        foreground=definir_cor.COR_PRETA,
                        font=('Times New Roman', '14'))
        style.configure('main.TButton', background=definir_cor.COR_BRANCA,
                        foreground=definir_cor.COR_PRETA,
                        width=5, relief=tk.RAISED)


    def setMenus():
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        prefsMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Preferências', menu=prefsMenu)

        themesMenu = tk.Menu(menubar, tearoff=0)
        prefsMenu.add_cascade(label='Temas', menu=themesMenu)
        themesMenu.add_command(label='Tema Branco', command=whiteTheme)
        themesMenu.add_command(label='Tema Preto', command=blackTheme)

        helpMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Ajuda', menu=helpMenu)
        helpMenu.add_command(label='URLs', command=mostrar_urls.run)
        helpMenu.add_command(label='Redes', command=ajuda_redes.run)

        def aboutClicked():
            messagebox.showinfo('Sobre', 'Programa criado por João Vítor S. F.' +
                                '\nRepositório: ' +
                                'github.com/jjoaovitor7/deep-web-url-aleatoria')

        helpMenu.add_command(label='Sobre', command=aboutClicked)


    def setWidgets():
        titleLabel = ttk.Label(self, text='Deep Web URL Aleatória',
                               style='main.TLabel').grid(row=0, column=0)

        urlLabel = ttk.Label(self, text='URL', style='main.TLabel',
                             cursor='hand1')
        urlLabel.grid(row=1, column=0)

        def goButtonClicked():
            conn = sqlite3.connect('urls.db')
            cursor = conn.cursor()
            cursor.execute('SELECT url FROM urls ORDER BY RANDOM() LIMIT 1;')
            getURLAux = cursor.fetchall()
            getURL = str(getURLAux).strip('()[],\'\'')
            #print(getURL)
            urlLabel.config(text=getURL)
            conn.close()

            def URLClicked(event):
                webbrowser.open_new(getURL)
            urlLabel.bind('<Button-1>', URLClicked)

        goButton = ttk.Button(self, text='Go!',
                              style='main.TButton',
                              command=goButtonClicked).grid(row=3,
                                                            column=0)


    configurar_icone.configurar_icone(self)

    blackTheme()

    setTitle()
    setGeometry()

    setMenus()
    setWidgets()


def run():
    root = tk.Tk()
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
