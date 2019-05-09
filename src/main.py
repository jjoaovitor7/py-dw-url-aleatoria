from tkinter import *
import random, webbrowser
from mostrar_urls import *
from ajuda_redes import *

jMain=Tk()
jMain.title('Deep Web Link Aleatório')
jMain.wm_iconbitmap('ico\dw_ico.ico')
jMain.configure(bg='black')

menubar=Menu(jMain)
jMain.config(menu=menubar)

temas=Menu(menubar)
menubar.add_cascade(label='Temas', menu=temas)

def tema_branco():        
        jMain.configure(bg='white')
        lTitulo.configure(bg='white', fg='black')
        lURL.configure(bg='white', fg='black')
        botao_go.configure(bg='white', fg='black')

def tema_preto():      
        jMain.configure(bg='black')
        lTitulo.configure(bg='black', fg='#00ff00')
        lURL.configure(bg='black', fg='#00ff00')
        botao_go.configure(bg='black', fg='#00ff00')

temas.add_command(label='Tema Branco', command=tema_branco)
temas.add_command(label='Tema Preto', command=tema_preto)

ajuda=Menu(menubar)
menubar.add_cascade(label='Ajuda', menu=ajuda)
ajuda.add_command(label='URLs', command=mostrar_urls)
ajuda.add_command(label='Redes', command=ajuda_redes)

lTitulo=Label(jMain, text='Deep Web Link Aleatório', font=('Comic Sans MS', '10', 'bold'))
lTitulo.grid(column=0, row=0, sticky=N)
lTitulo.configure(bg='black', fg='#00ff00')

lURL=Label(jMain, text='URL', font=('Comic Sans MS', '10'))
lURL.grid(column=0, row=2)
lURL.configure(bg='black', fg ='#00ff00')

def botao_go_clicado():        
        conn=sqlite3.connect('urls.db')
        cursor=conn.cursor()
        cursor.execute("""
        SELECT url FROM urls  ORDER BY RANDOM() LIMIT 1;
        """)
        url_=cursor.fetchall()
        url2_=str(url_).strip('()[],\'\'')
        lURL.configure(text=url_)
        conn.close()
        def clicar_url(event):
                webbrowser.open_new(url2_)
        lURL.bind('<Button-1>', clicar_url)
        
botao_go=Button(jMain, text='Go!', command=botao_go_clicado)
botao_go.grid(column=0, row=4)
botao_go.configure(bg='black', fg='#00ff00')

jMain.mainloop()
