from tkinter import *
import sqlite3

def mostrar_urls():      
         janelaURL=Toplevel()
         janelaURL.title('URLs')
         janelaURL.wm_iconbitmap('dw_ico.ico')
         janelaURL.configure(bg='black')
         
         conn=sqlite3.connect('urls.db')
         cursor=conn.cursor()
         cursor.execute("""
         SELECT nome, url FROM urls ;
         """)
         
         x=0
         for url in cursor.fetchall():
             urlPrograma=Label(janelaURL, text=url, font=('Times New Roman', '11'))
             urlPrograma.configure(bg='black', fg='#00ff00')
             urlPrograma.grid(column=0, row=x)
             x+=1          
         
         conn.close()
