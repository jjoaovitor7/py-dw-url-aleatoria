#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import platform
import logging

def configurar_icone(self):
    so = platform.system()
    try:
        if so == 'Linux':
            self.wm_iconbitmap('@ico/dw_ico.xbm')
    except tk.TclError:
        logging.basicConfig(filename='warning.log',
                            format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.WARN)
        logging.warning('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
            self.wm_iconbitmap('ico\dw_ico.ico')
    except tk.TclError:
        logging.basicConfig(filename='warning.log',
                            format='[%(asctime)s] %(levelname)s: %(message)s',
                            level=logging.WARN)
        logging.warning('dw_ico.ico não foi encontrado na pasta ico.')
