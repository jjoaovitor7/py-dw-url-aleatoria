from tkinter import *
import sqlite3

def mostrar_urls():
         jURL=Toplevel()
         jURL.title('URLs')
         jURL.wm_iconbitmap('ico\dw_ico.ico')
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
