# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3, platform

def mostrar_urls():
         so=platform.system()
         jURL=Toplevel()
         jURL.title('URLs')
         if so=='Windows':
                 jURL.wm_iconbitmap('ico\dw_ico.ico')
         if so=='Linux':
                 jURL.wm_iconbitmap('@ico/dw_ico.xbm')
         jURL.configure(bg='black')

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
