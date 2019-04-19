from tkinter import *
import random
import webbrowser
from mostrarURLs import *
from ajudaNavegadores import *

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.wm_iconbitmap("dw_ico.ico")
janela.geometry("280x100")
janela.configure(bg="black")

fonte1 = ("Comic Sans MS", "10")

menubar = Menu(janela)
janela.config(menu=menubar)
opcaomenu1 = Menu(menubar)
menubar.add_cascade(label='Temas', menu=opcaomenu1)
    
opcaomenu2 = Menu(menubar)
menubar.add_cascade(label='Ajuda', menu=opcaomenu2)
opcaomenu2.add_command(label='URLs', command=mostrarURLs)
opcaomenu2.add_command(label='Navegadores', command=ajudaNavegadores)

titulo = Label(janela, text="Deep Web Link Aleatório", font=("Comic Sans MS", "10", "bold"))
titulo.grid(column=0, row=0, sticky=W)
titulo.configure(bg="black", fg="#00ff00")

url = Label(janela, text="URL", font=fonte1)
url.grid(column=0, row=2)
url.configure(bg="black", fg ="#00ff00")

def botaoGoClicado():
         
        sitesDW = ["facebookcorewwwi.onion", "hss3uro2hsxfogfq.onion", "theches3nacocgsc.onion", 
                   "archivecrfip2lpi.onion", "3g2upl4pq6kufc4m.onion", "5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", 
                   "bible4u2kjgjvbxs.onion/", "xmh57jrzrnw6insl.onion", "enotegggr635n4lw.onion", "nytimes3xbfgragh.onion",
                   "duskgytldkxiuqc6.onion", "z2huz7tsxluvnxoc.onion"]
        siteDW = random.choice(sitesDW)
        def clicarLink(event):
                webbrowser.open_new(siteDW)
        url.configure(text=siteDW)
        url.bind("<Button-1>", clicarLink)
        
siteBotao = Button(janela, text="Go!", command=botaoGoClicado)
siteBotao.grid(column=0, row=4)
siteBotao.configure(bg="black", fg="#00ff00")

def TemaBranco():
         
        janela.configure(bg="white")
        titulo.configure(bg="white", fg="black")
        url.configure(bg="white", fg="black")
        siteBotao.configure(bg="white", fg="black")

def TemaPreto():
         
        janela.configure(bg="black")
        titulo.configure(bg="black", fg="#00ff00")
        url.configure(bg="black", fg="#00ff00")
        siteBotao.configure(bg="black", fg="#00ff00")

opcaomenu1.add_command(label='Tema Branco', command=TemaBranco)
opcaomenu1.add_command(label='Tema Preto', command=TemaPreto)

janela.mainloop()
